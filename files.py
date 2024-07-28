import os
import re
import shutil
import sys
from pathlib import Path

from deco import FileError


class File:
    """
    文件操作类，提供文件和目录的处理功能。
    """

    @staticmethod
    def show(path: str):
        """
        列出指定路径下的所有文件和目录。

        :param path: 字符串，指定的路径。
        """
        names = os.listdir(path)
        for name in names:
            print(name)

    @staticmethod
    def load_format_names(filename: Path) -> list[str]:
        """
        从文件中加载格式化后的姓名列表。

        :param filename: pathlib.Path对象，指定的文件路径。
        :return: 格式化后的姓名列表。
        """
        try:
            with open(f"{filename}", "r", encoding="utf-8") as f:
                formated_names = f.readlines()
        except FileNotFoundError:
            print("请创建文件./res/formated_names.txt 并将预设名单存入其中")
            sys.exit()
        except Exception as e:
            print(e)

        formated_names = [name.strip() for name in formated_names]  # 去除空白符

        return formated_names

    @staticmethod
    def remove_other_elements(input_string):
        """
        去除字符串中的非姓名元素。

        :param input_string: 待处理的字符串。
        :return: 处理后的字符串。
        """
        # TODO: 需优化正则表达式，防止误删除姓名中的合法字符
        input_string = re.sub(r'[号页设计期末班物联网]', '', input_string)
        result = "".join(re.findall(r'[\u4e00-\u9fff]', string=input_string))

        return result

    @staticmethod
    def match_names(names: list, formated_names: list):
        """
        将原始姓名列表与格式化姓名列表进行匹配。

        :param names: 原始姓名列表。
        :param formated_names: 格式化后的姓名列表。
        :return: 匹配成功的原始姓名与格式化姓名的元组列表。
        """
        matched_names = []
        matched_formated_names = []

        for name in names:
            obvious_name = File.remove_other_elements(name)
            for formated_name in formated_names:
                if obvious_name in formated_name and obvious_name != "":
                    matched_names.append(name)
                    matched_formated_names.append(formated_name)

        return matched_names, matched_formated_names

    @staticmethod
    def chinese_to_arabic(name_list: list[str]) -> tuple[list, list]:
        """
        将姓名中的中文数字转换为阿拉伯数字。

        :param name_list: 姓名列表。
        :return: 原始姓名列表和转换后的姓名列表。
        """
        chinese_nums = {'零': '0', '一': '1', '二': '2', '三': '3', '四': '4',
                        '五': '5', '六': '6', '七': '7', '八': '8', '九': '9',
                        '十': '10'}
        old_name_list = []
        new_name_list = []
        for str_with_digital in name_list:

            pattern = r'[零一二三四五六七八九十]+'
            matches = re.findall(pattern, str_with_digital)  # 匹配到的中文数字
            if len(matches) > 0:
                old_name_list.append(str_with_digital)
                for word in matches:
                    for char in word:
                        str_with_digital = str_with_digital.replace(char, chinese_nums[char])

                new_name_list.append(str_with_digital)  # 将转换后的字符串加入新列表
            else:
                pass

        return old_name_list, new_name_list

    def convert(self, name_list: list[str], file_path: str):
        """
        对文件或目录中的文件进行命名转换。

        :param name_list: 需要转换的文件名列表。
        :param file_path: 文件或目录的路径。
        """
        old_name_list, new_name_list = self.chinese_to_arabic(name_list)
        if len(old_name_list) == 0:
            print("没有要转换的文件")

        for src, dst in zip(old_name_list, new_name_list):

            src_path = Path(file_path) / src
            dst_path = Path(file_path) / dst

            if dst_path.exists():
                response = input(f"File '{dst}' already exists. Do you want to overwrite it? (y/n): ")
                if response.lower() == 'y':
                    shutil.rmtree(dst_path)
                    try:
                        shutil.move(src_path, dst_path)
                    except Exception as e:
                        print(e)
                else:
                    sys.exit()
            else:
                try:
                    os.rename(src_path, dst_path)
                    print(f"{src}\t->\t{dst}")
                except FileNotFoundError:
                    print(f"File '{src}' not found.")
                except PermissionError:
                    print(f"Permission denied to rename '{src}'.")
                except Exception as e:
                    print(e)

    @staticmethod
    @FileError.output
    def command_format(target: str, exe_path_absolute: Path) -> int:
        """
        根据命令行参数对文件或目录进行格式化处理。

        :param target: 需要处理的目标文件或目录。
        :param exe_path_absolute: 执行程序的绝对路径。
        """
        names = os.listdir(target)
        # new_names = [name for name in names if Path(name).is_dir()]
        new_names = []
        for name in names:

            if Path(target, name).is_dir():
                new_names.append(name)
            else:
                print("format:跳过", name)

        filename = exe_path_absolute.parent / "res/formated_names.txt"

        formated_names = File.load_format_names(filename)
        if len(formated_names) == 0:
            print(f"{filename}内容为空")
            sys.exit()

        # 将目录中的文件名与预定义的格式化文件名进行匹配
        matched_names, matched_formated_names = File.match_names(new_names, formated_names)

        # 检查是否有相同数量的匹配文件名
        if len(matched_names) == len(matched_formated_names):
            formated_times = 0
            for i, name in enumerate(matched_names):
                res = Path(target) / name
                des = Path(target) / matched_formated_names[i]
                if res == des:
                    continue
                else:
                    shutil.move(res, des)
                    formated_times += 1

                print(f"{name}\t->\t{matched_formated_names[i]}")
            return formated_times
