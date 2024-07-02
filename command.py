import os

from files import File


class Command:
    def __init__(self):
        self.command1 = None
        self.command2 = None
        self.command3 = None
        self.command4 = None
        self.selected = None
        self.command_list = None
        self.argv = None
        self.file = File()
        self.init_commands()

    def init_commands(self):
        self.command1 = {"command": "help", "description": "Show this help message"}
        self.command2 = {"command": "show", "description": "Show all files in the directory"}
        self.command3 = {"command": "simplify", "description": "Simplified folder structure"}
        self.command4 = {"command": "format", "description": "Formate the folder name"}

        self.command_list = [
            self.command1,
            self.command2,
            self.command3,
            self.command4
        ]

    def read_command(self):
        command_found = False
        for command in self.command_list:
            if self.selected in command["command"]:
                command_found = True

        if not command_found:
            print("无命令")
            return
        # TODO:优化命令调用
        if self.selected == "help":
            self.help()
        elif self.selected == "show":
            self.show()
        elif self.selected == "simplify":
            self.file.simplify_file_path(self.argv)
        elif self.selected == "format":
            self.file.command_format(self.argv)

    def help(self):
        for item in self.command_list:
            for command, description in item.items():
                print(f"command:{command}\tdescription:{description}")

    def show(self):
        names = os.listdir(self.argv)
        for _ in names:
            print(_)
