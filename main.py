from sys import argv

from command import Command

# test -----------------
# argv = ["", "show", r"C:\Users\Alddp\Desktop\movetest"]
# ------------------------

command = Command()

command.selected = argv[1]
try:
    command.argv = argv[2]
except IndexError as e:

    if command.selected != "help":
        print("请输入参数")

command.read_command()
