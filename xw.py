from sys import argv

from command import CommandManager

# 初始化命令管理器，准备处理命令
command_manager = CommandManager()
# 设置命令管理器的参数为系统传入的命令行参数
# argv = ['xw', "convert", r"C:\Users\Administrator\Desktop\test"]
command_manager.argv = argv
command_manager.init_argv()
# 初始化命令管理器中的命令
success = command_manager.init_commands()

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
