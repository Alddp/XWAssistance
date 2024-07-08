import json
import os
from pathlib import Path
from sys import argv

from files import File
from simplify_file import FileSimplifier


# 命令管理类，负责处理和执行不同的命令
class CommandManager:
    def __init__(self):
        # 初始化绝对执行路径
        self.exe_path_absolute: Path = Path()
        # 初始化选中的命令
        self.selected: str = ""
        # 初始化文件路径
        self.file_path: str = ""
        # 初始化文件名列表
        self.name_list: list[str] = []
        # 初始化命令行参数列表
        self.argv: list[str] = argv
        # 初始化命令行参数
        self.init_argv()
        # 初始化命令列表
        self.command_list = []
        # 初始化文件操作类实例
        self.file = File()  # 文件操作工具类实例
        # 加载命令列表
        self.init_commands()

    # 初始化命令行参数
    def init_argv(self):
        # 获取执行程序的绝对路径
        self.exe_path_absolute = Path(os.path.realpath(self.argv[0]))  # 执行程序的路径
        # 获取用户选择的命令
        self.selected = self.argv[1]  # 用户选择的命令
        # 如果选择的不是帮助命令，则获取文件路径和文件名列表
        # TODO: 优化help输入错误提示词
        if self.selected != "help":
            self.file_path = self.argv[2]  # 文件或目录路径
            self.name_list = os.listdir(self.file_path)

    # 初始化命令列表
    def init_commands(self, commands_data_relative=r'data/commands.json'):
        # 构建命令数据的绝对路径
        commands_data_absolute = self.exe_path_absolute.parent / commands_data_relative
        try:
            # 加载命令数据文件
            # 加载命令数据文件
            with open(commands_data_absolute, 'r') as file:
                commands = json.load(file)
            # 检查加载的数据是否为列表
            # 检查加载的数据是否为列表
            if not isinstance(commands, list):
                raise ValueError("命令文件应包含一个列表")
            # 更新命令列表
            self.command_list = commands
            return True
        except FileNotFoundError:
            print(f"无法找到命令文件: {commands_data_absolute}")
        except json.JSONDecodeError:
            print(f"无法解析命令文件 {commands_data_absolute} 的内容")
        except ValueError as e:
            print(e)
        return False

    # 打印帮助信息
    def help(self):
        """
        打印除帮助命令外的所有命令及其描述。
        """
        for item in self.command_list:
            if item["command"] == "help":
                continue
            print(f"command: {item['command']}\ndescription: {item['description']}\n")

    # 根据选择的命令执行相应的操作
    def read_command(self):
        # 根据选择执行相应的命令处理
        if self.selected == "help":
            self.help()
        elif self.selected == "show":
            self.show(self.file_path)
        elif self.selected == "simplify":
            sp = FileSimplifier(self.file_path)
            sp.simplify()
        elif self.selected == "format":
            self.file.command_format(self.file_path, self.exe_path_absolute)
        elif self.selected == "convert":
            self.file.convert(self.name_list, self.file_path)

    # 打印指定路径下的文件和目录列表
    @staticmethod
    def show(path: str):
        """
        打印指定路径下的文件和目录列表。

        :param path: str 要列出内容的路径。
        """
        names = os.listdir(path)
        for name in names:
            print(name)
