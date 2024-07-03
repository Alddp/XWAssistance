from sys import argv

from command import CommandManager

# test -----------------
# argv = ["", "simplify", r"C:\Users\Alddp\Desktop\simplify_test"]
# ------------------------

command_manager = CommandManager()
success = command_manager.init_commands()

command_manager.selected = argv[1]

command_found = False

for command in command_manager.command_list:
    if command_manager.selected in command["command"]:
        command_found = True

if command_found:
    try:
        command_manager.init_listdir(argv[2])
        command_manager.read_command()

    except IndexError as e:

        if command_manager.selected != "help":
            print("没有输入参数\n")
        elif command_manager.selected == "help":
            command_manager.help()
        else:
            print(e)

else:
    print("命令错误")
    command_manager.help()
