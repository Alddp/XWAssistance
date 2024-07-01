from files import File
from sys import argv

file = File()

# argv = ["main.py", "fix", r"C:\Users\Alddp\Desktop\html压缩包"]
# command = argv[1]
command = argv[1]
if (len(argv) == 2) and (argv[1] == "help"):
    print("command:\n1.show [path]\n2.fix [path]")

if len(argv) == 3:  # 读取第二个参数
    target = str(argv[2])
    if command == ("show" or 1):
        names = file.get_child_dirs(path=target)
        for _ in names:
            print(_)
    elif command == ("fix" or 2):
        file.command_2(target=target)
    else:
        print("命令错误")
else:
    print("无参数")
