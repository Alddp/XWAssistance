import os

from files import File


class Command:
    def __init__(self):
        self.selected = ""
        self.name_list: list[str] = []
        self.command1 = ""
        self.command2 = ""
        self.command3 = ""
        self.command4 = ""
        self.command5 = ""
        self.command_list: list[dict[str]:[str]] = []
        self.argv = ""
        self.file = File()
        self.init_commands()

    def init_commands(self):
        self.command1 = {"command": "help", "description": "Show this help message"}
        self.command2 = {"command": "show", "description": "Show all files in the directory"}
        self.command3 = {"command": "simplify", "description": "Simplified folder structure"}
        self.command4 = {"command": "format", "description": "Formate the folder name"}
        self.command5 = {"command": "convert", "description": "Convert Chinese numbers to Arabic numerals"}
        self.command_list = [
            self.command1,
            self.command2,
            self.command3,
            self.command4,
            self.command5
        ]

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

    def help(self):
        for item in self.command_list:
            if item["command"] == "help":
                continue
            print(f"command: {item["command"]}\ndescription: {item["description"]}\n")

    @staticmethod
    def show(path: str):
        names = os.listdir(path)
        for _ in names:
            print(_)
