import json
import os
import sys

from files import File
from simplify_file import FileSimplifier


class CommandManager:
    """
    命令管理器类，负责初始化命令列表，解析并执行命令。
    """

    def __init__(self):
        """
        初始化命令管理器，包括命令列表和当前选择的命令。
        """
        self.name_list = None
        self.argv = None
        self.command_list = []
        self.selected = ""
        self.file = File()
        self.init_commands()

    def init_commands(self, commands_file=r'data/commands.json'):
        """
        从指定的JSON文件中初始化可用的命令列表。

        :param commands_file: 包含命令列表的JSON文件路径，默认为'data/commands.json'。
        :return: 成功初始化返回True，否则返回False。
        """
        """
        初始化可用命令列表。

        参数:
        commands_file: 包含命令和描述的JSON文件路径。

        返回:
        成功初始化返回True，否则返回False。

        异常:
        - FileNotFoundError: 如果命令文件不存在。
        - json.JSONDecodeError: 如果无法解析命令文件。
        """
        # 将相对路径转换为绝对路径
        commands_file = os.path.join(CommandManager.get_exe_path(), r"data/commands.json")
        try:
            with open(commands_file, 'r') as file:
                commands = json.load(file)

            # 确保加载的内容是列表
            if not isinstance(commands, list):
                raise ValueError("命令文件应包含一个列表")

            self.command_list = commands
            return True
        except FileNotFoundError:
            print(f"无法找到命令文件: {commands_file}")
        except json.JSONDecodeError:
            print(f"无法解析命令文件 {commands_file} 的内容")
        except ValueError as e:
            print(e)

        return False

    @staticmethod
    def get_exe_path():
        """
        获取当前执行程序的路径。

        :return: 执行程序的路径。
        """
        # 尝试从环境变量中获取可执行文件的路径
        self_path = ""

        # PyInstaller创建的可执行文件会在环境变量PATH中临时包含_MEIPASS路径
        meipass = os.environ.get('_MEIPASS', '')
        if meipass:  # _MEIPASS存在，则_exe位于此目录
            self_path = os.path.abspath(meipass)
        else:  # 否则尝试从sys.executable获取
            self_path = os.path.dirname(os.path.abspath(sys.executable))

        if self_path:
            return self_path
        else:
            print("无法确定程序所在路径。")

    def help(self):
        """
        打印除帮助命令外的所有命令及其描述。
        """
        for item in self.command_list:
            if item["command"] == "help":
                continue
            print(f"command: {item['command']}\ndescription: {item['description']}\n")

    def init_listdir(self, argv):
        """
        初始化目录列表。

        :param argv: 命令行参数，用于指定目录。
        """
        self.argv = argv
        self.name_list = os.listdir(argv)

    def read_command(self):
        """
        根据当前选择的命令，执行相应的操作。
        """
        # TODO:优化命令调用
        if self.selected == "help":
            self.help()

        elif self.selected == "show":
            self.show(self.argv)

        elif self.selected == "simplify":
            sp = FileSimplifier(self.argv)
            sp.simplify()

        elif self.selected == "format":
            self.file.command_format(self.argv)

        elif self.selected == "convert":
            self.file.convert(self.name_list, self.argv)

    @staticmethod
    def show(path: str):
        """
        打印指定路径下的文件和目录列表。

        :param path: 要列出的目录路径。
        """
        names = os.listdir(path)
        for _ in names:
            print(_)
