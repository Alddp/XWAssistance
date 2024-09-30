import csv
from pathlib import Path


class FormateFile:
    config_path = "./res/data.csv"

    def __init__(self):
        self.p_names: list[str] = []  # 准备处理的名
        self.f_names: list[str] = []  # 标准名
        self.names: list[str] = []  # 学生名
        self.target_data: dict[str, str] = {}  # {'待处理名':'标准名', ...}

    def init(self, path: str, fp: str = config_path):
        """
        初始化函数，直接加载所有属性
        """
        self.get_names_instances(path)
        self.read_data(fp)
        self.match_name()

    def get_names_instances(self, path: str) -> list[Path]:
        """
        获取目录下所有文件的Path实例

        :param path: 要格式化文件夹的目录
        :return: 目录下所有文件Path实例列表
        """
        names_instances: list[Path] = [i for i in Path(path).iterdir()]
        self.p_names = [i.name for i in names_instances]
        return names_instances

    def read_data(self, fp: str = config_path) -> tuple[list[str], list[str]]:
        """
        读取csv文件
        :param fp: csv文件路径
        :return: 姓名列表，标准名列表
        """
        with open(fp, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            rows = list(reader)  # 一次性读取所有行

            self.names = [row[0] for row in rows]  # 第一列
            self.f_names = [row[1] for row in rows]  # 第二列

        return self.names, self.f_names

    def match_name(self) -> dict[str, str]:
        # 通过一次性字典推导式替换之前的循环，提高效率
        # 将部分名称与名字列表进行匹配，找到对应的索引
        data = {p: index for index, n in enumerate(self.names) for p in self.p_names if n in p}
        # 根据匹配到的部分名称，从文件名列表中提取对应的目标数据
        self.target_data = {key: self.f_names[data[key]] for key in data.keys()}
        return self.target_data

    @staticmethod
    def write_formate_config(names: list[str], f_names: list[str], config_path: str = config_path):
        # 将名称和文件名列表写入指定的配置文件中
        if len(names) != len(f_names):
            raise ValueError("长度不一")

        with open(config_path, 'w', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            try:
                for name, f_name in zip(names, f_names):
                    if name in f_name:
                        writer.writerow([name, f_name])
                    else:
                        raise IndexError("一个名称未找到对应的文件名")
            except IndexError:
                # 如果有错误，记录所有匹配的行
                rows = [[name, f_name] for name in names for f_name in f_names if name in f_name]
                writer.writerows(rows)
