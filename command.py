import json
import os

from files import File


class CommandManager:
    def __init__(self):
        self.name_list = None
        self.argv = None
        self.command_list = []
        self.selected = ""
        self.file = File()
        self.init_commands()

    def init_commands(self, commands_file=r'data/commands.json'):
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

    def help(self):
        for item in self.command_list:
            if item["command"] == "help":
                continue
            print(f"command: {item["command"]}\ndescription: {item["description"]}\n")

    def init_listdir(self, argv):
        self.argv = argv
        self.name_list = os.listdir(argv)

    def read_command(self):

        # TODO:优化命令调用
        if self.selected == "help":
            self.help()

        elif self.selected == "show":
            self.show(self.argv)

        elif self.selected == "simplify":
            self.file.simplify_file_path(self.argv)

        elif self.selected == "format":
            self.file.command_format(self.argv)

        elif self.selected == "convert":
            self.file.convert(self.name_list, self.argv)

    @staticmethod
    def show(path: str):
        names = os.listdir(path)
        for _ in names:
            print(_)


if __name__ == '__main__':
    cmd = CommandManager()
    cmd.selected = "show"
    cmd.argv = r"C:\Users\Alddp\Desktop\movetest"
    cmd.read_command()
