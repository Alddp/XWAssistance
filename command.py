import json
import os
import sys
from pathlib import Path

from files import File
from simplify_file import FileSimplifier
from solitaire import Solitaire


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
        self.argv: list[str] = []

        # json格式命令
        self.commands: dict = {}
        # 初始化文件操作类实例
        self.file = File()  # 文件操作工具类实例

        self.export_path = ""

    # 初始化命令行参数
    def init_argv(self):
        # 如果选择的不是帮助命令，则获取文件路径和文件名列表
        # TODO: 优化提示
        selected = self.argv[1]

        self.exe_path_absolute = Path(os.path.realpath(self.argv[0]))  # 执行程序的路径
        self.selected = self.argv[1]  # 用户选择的命令

        if selected != "help" and selected != "config":
            try:
                self.file_path = self.argv[2]  # 文件或目录路径
            except IndexError:
                print("缺少参数")
                sys.exit()

    # 初始化命令列表
    def init_commands(self, commands_data_relative=r'data/commands.json'):
        # 构建命令数据的绝对路径
        commands_data_absolute = self.exe_path_absolute.parent / commands_data_relative
        try:
            # 加载命令数据文件
            with open(commands_data_absolute, "r", encoding="utf-8") as f:
                data = json.load(f)

            # 更新命令列表
            self.commands = data
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
        print()
        for key, value in self.commands.items():
            print(key)
            for command, description in value.items():
                print(f"    {command} : {description}")

    # 根据选择的命令执行相应的操作
    def read_command(self):
        # 根据选择执行相应的命令处理
        match self.selected:
            case "help":
                self.help()
            case "show":
                self.file.show(self.file_path)
            case "simplify":
                sp = FileSimplifier(self.file_path)
                sp.simplify()
            case "format":
                formated_times = self.file.command_format(self.file_path, self.exe_path_absolute)

                print("文件都格式化了") if formated_times == 0 else print(f"处理了 {formated_times} 个文件")

            case "convert":
                self.name_list = os.listdir(self.file_path)
                self.file.convert(self.name_list, self.file_path)
            case "export":
                form_id = self.argv[2]
                save_path = self.argv[3]
                sol = Solitaire(form_id)
                sol.exe_path_absolute = self.argv[0]
                sol.export_files(save_path)

            case "config":
                app_id = input("Please enter your appid:")
                secret = input("Please enter your secret:")

                with open(self.exe_path_absolute.parent / "data/solitaire.json", "w", encoding="utf-8") as f:
                    json.dump({"app_id": app_id, "secret": secret}, f, ensure_ascii=False, indent=4)
            case _:
                print("无效命令")
                sys.exit()
