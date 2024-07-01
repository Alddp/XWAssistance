import os
import shutil
import re


class File:

    @staticmethod
    def load_formate_names(filename: str):
        """读取姓名模板"""

        with open(f"{filename}", "r", encoding="utf-8") as f:
            formated_names = f.readlines()
        formated_names = [s.strip() for s in formated_names]  # 去除空白符
        print(f"{filename}Loading formated names...")
        return formated_names

    @staticmethod
    def get_child_dirs(path: str):
        """列出所有文件名"""
        dirs = os.listdir(path)
        return dirs

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
                if obvious_name in formated_name:
                    # 返回匹配的名字对
                    matched_names.append(name)
                    matched_formated_names.append(formated_name)

        return matched_names, matched_formated_names

    @staticmethod
    def command_2(target: str):
        names = File.get_child_dirs(path=target)
        formated_names = File.load_formate_names("res/formated_names.txt")
        matched_names, matched_formated_names = File.match_names(names, formated_names)

        if len(matched_names) == len(matched_formated_names):
            for i, name in enumerate(matched_names):
                shutil.move(target + "\\" + name, target + "\\" + matched_formated_names[i])
                print(f"{name}\t->\t{matched_formated_names[i]}")
        else:
            print("长度不一")
