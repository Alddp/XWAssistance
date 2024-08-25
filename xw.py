import sys

from command import CommandManager


def main(argv):
    command_manager = CommandManager()

    if len(argv) < 2:
        print("没有输入参数")
        sys.exit(0)

    command_manager.argv = argv

    command_manager.init_argv()

    command_manager.init_commands(commands_data_relative=r'data/commands.json')

    try:
        # 执行匹配的命令
        command_manager.read_command()

    # 捕获IndexError异常
    except IndexError as e:

        print(e)
