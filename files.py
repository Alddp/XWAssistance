import os
import re
import shutil
import sys
from pathlib import Path


class File:
    """
    提供文件操作相关的方法，包括文件名格式化、中文数字转阿拉伯数字等。
    """

    @staticmethod
    def show(path: str):
        """
        打印指定路径下的文件和目录列表。

        :param path: str 要列出内容的路径。
        """
        names = os.listdir(path)
        for name in names:
            print(name)

    @staticmethod
    def load_format_names(filename: Path) -> list[str]:
        """
        从指定文件中加载格式化后的姓名列表。

        :param filename: 包含格式化姓名的文件路径。
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

        formated_names = [s.strip() for s in formated_names]  # 去除空白符

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

        for src, dst in zip(old_name_list, new_name_list):
            src_path = os.path.join(file_path, src)
            dst_path = os.path.join(file_path, dst)

            if os.path.exists(dst_path):
                response = input(f"File '{dst}' already exists. Do you want to overwrite it? (y/n): ")
                if response.lower() == 'y':
                    shutil.rmtree(dst_path)
                    try:
                        shutil.move(src_path, dst_path)
                    except Exception as e:
                        print(e)
                else:
                    pass
            else:
                try:
                    os.rename(src_path, dst_path)
                    print(f"{src_path}\t->\t{dst_path}")
                except FileNotFoundError:
                    print(f"File '{src}' not found.")
                except PermissionError:
                    print(f"Permission denied to rename '{src}'.")
                except Exception as e:
                    print(e)

    @staticmethod
    def command_format(target: str, exe_path_absolute: Path):
        """
        根据命令行参数对文件或目录进行格式化处理。

        :param target: 需要处理的目标文件或目录。
        :param exe_path_absolute: 执行程序的绝对路径。
        """
        names = os.listdir(target)
        # 加载预定义的格式化文件名列表
        formated_names = File.load_format_names(exe_path_absolute.parent / "res/formated_names.txt")

        # 将目录中的文件名与预定义的格式化文件名进行匹配
        matched_names, matched_formated_names = File.match_names(names, formated_names)

        # 检查是否有相同数量的匹配文件名
        if len(matched_names) == len(matched_formated_names):
            formated_times = 0
            for i, name in enumerate(matched_names):
                res = os.path.join(target, name)
                des = os.path.join(target, matched_formated_names[i])
                if res == des:
                    continue
                else:
                    try:
                        shutil.move(res, des)
                        formated_times += 1
                    except Exception as e:
                        print(f"Error: {e}")

                    print(f"{name}\t->\t{matched_formated_names[i]}")
            if formated_times == 0:
                print("文件都格式化了")
        else:
            print("长度不一")
