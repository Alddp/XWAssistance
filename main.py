from sys import argv
from command import CommandManager

# 初始化命令管理器，准备处理命令
command_manager = CommandManager()

# 设置命令管理器的参数为系统传入的命令行参数
command_manager.argv = argv
# 初始化命令管理器中的命令
success = command_manager.init_commands()

# 初始化是否找到命令的标志
command_found = False

# 遍历命令列表，寻找匹配的命令
for command in command_manager.command_list:
    # 如果已经找到命令，则不再搜索
    if command_found:
        break

    # 如果当前命令匹配选定的命令，设置标志为True
    if command_manager.selected in command["command"]:
        command_found = True

# 如果找到了匹配的命令

if command_found:
    try:
        # 执行匹配的命令
        command_manager.read_command()

    # 捕获IndexError异常
    except IndexError as e:

        # 如果选定的命令不是帮助命令，提示没有输入参数
        if command_manager.selected != "help":
            # 提示没有输入参数
            print("没有输入参数\n")

        # 如果选定的是帮助命令，执行帮助函数
        elif command_manager.selected == "help":
            # 执行帮助命令
            command_manager.help()

        # 如果是其他异常，打印异常信息
        else:
            # 打印异常信息
            print(e)

# 如果没有找到选定的命令，提示命令错误，并执行帮助函数
else:
    # 提示命令错误
    print("命令错误")
    # 执行帮助命令
    command_manager.help()
