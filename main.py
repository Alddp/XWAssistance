# 导入系统模块，用于获取命令行参数
from sys import argv

# 导入命令管理器类，用于处理不同命令
from command import CommandManager

# 初始化命令管理器
command_manager = CommandManager()
# 初始化命令管理器中的命令
success = command_manager.init_commands()

# 从命令行参数中获取选定的命令
command_manager.selected = argv[1]

# 初始化命令是否找到的标志
command_found = False

# 遍历命令列表，查找选定的命令
for command in command_manager.command_list:
    # 如果命令已找到，跳出循环
    if command_found:
        break
    # 如果当前命令匹配选定的命令，设置标志为True
    if command_manager.selected in command["command"]:
        command_found = True

# 如果找到了选定的命令
if command_found:
    try:
        # 初始化目录列表，准备处理命令
        command_manager.init_listdir(argv[2])
        # 执行选定的命令
        command_manager.read_command()
    # 捕获IndexError异常
    except IndexError as e:
        # 如果选定的命令不是帮助命令，提示没有输入参数
        if command_manager.selected != "help":
            print("没有输入参数\n")
        # 如果选定的是帮助命令，执行帮助函数
        elif command_manager.selected == "help":
            command_manager.help()
        # 如果是其他异常，打印异常信息
        else:
            print(e)
# 如果没有找到选定的命令，提示命令错误，并执行帮助函数
else:
    print("命令错误")
    command_manager.help()
