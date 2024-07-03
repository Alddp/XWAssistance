from sys import argv

from command import Command

# test -----------------
# argv = ["", "simplify", r"C:\Users\Alddp\Desktop\simplify_test"]
# ------------------------

cmd = Command()

cmd.selected = argv[1]

command_found = False

for command in cmd.command_list:
    if cmd.selected in command["command"]:
        command_found = True

if command_found:
    try:
        cmd.init_listdir(argv[2])
        cmd.read_command()

    except IndexError as e:

        if cmd.selected != "help":
            print("没有输入参数\n")
        elif cmd.selected == "help":
            cmd.help()
        else:
            print(e)

else:
    print("命令错误")
    cmd.help()
