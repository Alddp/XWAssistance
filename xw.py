import sys

from command import CommandManager


def main():
    command_manager = CommandManager()

    if len(sys.argv) < 2:
        print("没有输入参数")
        sys.exit(0)

    command_manager.argv = sys.argv

    command_manager.init_argv()

    command_manager.init_commands()

    try:
        # 执行匹配的命令
        command_manager.read_command()

    # 捕获IndexError异常
    except IndexError as e:

        print(e)


# sys.argv = [r'D:\Codes\Python\XwAssistance\xw.py', 'format', r"C:\Users\Alddp\Desktop\test"]
main()
