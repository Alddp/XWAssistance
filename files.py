import os
import re
import shutil


class File:
    """文件操作类"""

    @staticmethod
    def load_formate_names(filename: str):
        """读取姓名模板"""

        with open(f"{filename}", "r", encoding="utf-8") as f:
            formated_names = f.readlines()
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
        """
        如果文件夹下只有一个同名文件夹,则将同名文件夹下的所有文件移动到当前文件夹，删除同名空文件夹
        :param path: 要简化的文件路径
        """
        file_names = os.listdir(path)  # 获取路径下的文件
        len_is_one = len(file_names) == 1  # 内层只有一个文件

        if len_is_one:
            inner_filename = os.path.join(path, file_names[0])  # 获取内层同名文件路径

            isdir = os.path.isdir(inner_filename)  # 判断这个文件是否为文件夹
            if isdir:
                dst = path
                for item in os.listdir(inner_filename):
                    shutil.move(os.path.join(inner_filename, item), dst)
                    shutil.rmtree(inner_filename) if len(os.listdir(inner_filename)) == 0 else None

                    print(f"简化嵌套文件{path}")
            else:
                print(f"{inner_filename}不是文件夹")
        else:
            print(f"{path}是空文件夹")

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
