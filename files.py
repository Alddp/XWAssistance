import os
import re
import shutil
import sys


class File:
    """文件操作类"""

    @staticmethod
    def load_formate_names(filename: str) -> list[str]:
        """读取姓名模板"""
        try:
            with open(f"{filename}", "r", encoding="utf-8") as f:
                formated_names = f.readlines()
        except FileNotFoundError:
            print("请创建文件./res/formated_names.txt 将预设名单存入formated_names.txt")
            sys.exit()
        except Exception as e:
            print(e)

        formated_names = [s.strip() for s in formated_names]  # 去除空白符
        print(f"{filename}Loading formated names...")
        return formated_names

    @staticmethod
    def remove_other_elements(input_string):
        """去除无关元素只留下姓名"""
        # TODO: 防止去除的字符串包含姓名
        input_string = re.sub(r'[号页设计期末班物联网]', '', input_string)
        result = "".join(re.findall(r'[\u4e00-\u9fff]', string=input_string))

        return result

    @staticmethod
    def match_names(names: list, formated_names: list):
        """匹配姓名后格式化命名"""
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
    def simplify_file_path(path: str):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isdir(file_path):
                File.simplify_file(path, filename)
            else:
                print(f"{file_path}不是文件夹")

    @staticmethod
    def simplify_file(path, filename: str):
        """
        如果文件夹下只有一个文件夹,则将文件夹下的所有文件移动到当前文件夹，删除同名文件夹
        :param path: 文件路径  path/filename
        :param filename: 要简化的文件名
        """
        file_names = os.listdir(os.path.join(path, filename))  # 获取子目录列表
        listdir_len = len(file_names)

        if listdir_len == 1:  # 内层只有一个文件
            inner_filename = os.path.join(path, filename, file_names[0])  # 获取内层文件路径

            isdir = os.path.isdir(inner_filename)  # 判断这个文件是否为文件夹
            if isdir:
                dst = os.path.join(path, filename)
                for item in os.listdir(inner_filename):
                    shutil.move(os.path.join(inner_filename, item), dst)
                    shutil.rmtree(inner_filename) if len(os.listdir(inner_filename)) == 0 else None

                    print(f"简化嵌套文件{os.path.join(filename, file_names[0], item)}\t->\t{dst}")
                print()
        elif listdir_len == 0:
            print(f"{filename}是空文件夹")

    @staticmethod
    def chinese_to_arabic(name_list: list[str]) -> tuple[list, list]:
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
        old_name_list, new_name_list = self.chinese_to_arabic(name_list)

        for src, dst in zip(old_name_list, new_name_list):
            src_path = os.path.join(file_path, src)
            dst_path = os.path.join(file_path, dst)

            if os.path.exists(dst_path):
                response = input(f"File '{dst}' already exists. Do you want to overwrite it? (y/n): ")
                if response.lower() == 'y':
                    shutil.rmtree(dst_path)
                    shutil.move(src_path, dst_path)
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
        names = os.listdir(target)
        formated_names = File.load_formate_names("res/formated_names.txt")
        matched_names, matched_formated_names = File.match_names(names, formated_names)

        if len(matched_names) == len(matched_formated_names):
            for i, name in enumerate(matched_names):
                res = os.path.join(target, name)
                des = os.path.join(target, matched_formated_names[i])
                try:
                    shutil.move(res, des)
                except Exception as e:
                    print(f"Error: {e}")

                print(f"{name}\t->\t{matched_formated_names[i]}")
        else:
            print("长度不一")
