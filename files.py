import os
import re
import shutil
import sys

class File:
    """
    文件操作类，提供文件名格式化、中文数字转阿拉伯数字等功能。
    """

    @staticmethod
    def load_format_names(filename: str) -> list[str]:
        """
        从指定文件中加载格式化后的姓名列表。

        :param filename: 文件名，包含路径。
        :return: 格式化后的姓名列表。
        """
        try:
            with open(f"{filename}", "r", encoding="utf-8") as f:
                formated_names = f.readlines()
        except FileNotFoundError:
            print("请创建文件./res/formated_names.txt 将预设名单存入formated_names.txt")
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
        # TODO: 防止去除的字符串包含姓名
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
                    # 返回匹配的名字对
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
                    # TODO:处理文件子目录中的文件移动时文件同名无法移动
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
    def command_format(target: str):
        """
        格式化指定目录下的文件名。

        :param target: 目标目录的路径。
        """
        # 列出目标目录中的所有文件名
        names = os.listdir(target)
        # 加载预定义的格式化文件名列表
        formated_names = File.load_format_names("res/formated_names.txt")
        # 将目录中的文件名与预定义的格式化文件名进行匹配
        matched_names, matched_formated_names = File.match_names(names, formated_names)

        # 检查是否有相同数量的匹配文件名
        if len(matched_names) == len(matched_formated_names):
            # 遍历匹配的文件名列表
            formated_times = 0
            for i, name in enumerate(matched_names):
                # 构建原始文件路径和目标文件路径
                res = os.path.join(target, name)
                des = os.path.join(target, matched_formated_names[i])
                if res == des:
                    continue
                else:
                    try:
                        # 尝试将文件重命名为格式化后的文件名
                        shutil.move(res, des)
                        formated_times += 1
                    except Exception as e:
                        # 如果重命名过程中发生错误，打印错误信息
                        print(f"Error: {e}")

                    # 打印文件重命名的结果
                    print(f"{name}\t->\t{matched_formated_names[i]}")
            if formated_times == 0:
                print("文件都格式化了")
        else:
            # 如果匹配的文件名数量不一致，提示用户
            print("长度不一")

