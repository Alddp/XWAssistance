import csv
import shutil
from pathlib import Path


class File:
    def __init__(self):
        self._work_space = Path()

    @property
    def work_space(self):
        return self._work_space

    @work_space.setter
    def work_space(self, value: str):
        self._work_space = Path(value)

    def init(self, work_space: str = ''):
        ...

    def start(self):
        ...


class FileFormater(File):
    config_path = "config/data.csv"

    def __init__(self):
        super().__init__()
        self.p_names: list[str] = []  # 准备处理的名
        self.f_names: list[str] = []  # 标准名
        self.names: list[str] = []  # 学生名
        self.target_data: dict[str, str] = {}  # {'待处理名':'标准名', ...}

    def init(self, work_space: str = '', fp: str = config_path):
        """
        初始化函数，直接加载所有属性
        """
        self.work_space = work_space or self.work_space

        self.get_names_instances()
        self.read_data(fp)
        self.match_name()

    def get_names_instances(self) -> list[Path]:
        """
        获取目录下所有文件的Path实例

        :return: 目录下所有文件Path实例列表
        """
        names_instances: list[Path] = [i for i in self.work_space.iterdir()]
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

    def start(self):
        for k, value in self.target_data.items():
            (self.work_space / k).rename(self.work_space / value)


class FileSimplifier(File):

    def __init__(self):
        super().__init__()

        self.map: dict[Path, Path] = {}
        self.log: dict[Path, list[Path]] = {}

    def init(self, work_space: str = ''):
        """
        简化文件路径的主方法，包括加载映射、日志和解析日志。
        """
        self.work_space = work_space or self.work_space

        self.load_map()
        self.load_log()

    def start(self):
        """
        解析日志并处理文件移动过程中可能出现的冲突。
        """
        for main_folder, inner_files in self.log.items():
            crack_name = None
            renamed_file = None
            # 文件中有特殊文件无法移动  --bug
            for inner_file in inner_files:
                try:
                    shutil.move(inner_file, main_folder)
                except shutil.Error:
                    temp_name = main_folder / (inner_file.name + ".tmp")
                    crack_name = main_folder / inner_file.name
                    # 重命名冲突的文件为temp_name并移出
                    renamed_file = inner_file.rename(temp_name)
                except Exception as e:
                    print(f"移动文件时发生错误：{e}")

            # 删除空文件夹
            if crack_name and crack_name.exists() and not any(crack_name.iterdir()):
                crack_name.rmdir()
                # 恢复文件名为inner_file.name
                if renamed_file:
                    renamed_file.rename(renamed_file.parent / renamed_file.name.removesuffix(".tmp"))
            else:
                try:
                    self.map[main_folder].rmdir()
                except PermissionError as p:
                    # TODO: 存储错误日志
                    print(p)
                except Exception as e:
                    print(e)

    def load_log(self) -> dict[Path, list[Path]]:
        """
        加载日志，记录每个文件夹及其对应的文件。

        :return: 包含文件夹及其文件的字典。
        """
        # 重置self.map和self.log 修复第二次使用simplify无法更新表格的bug --bug
        self.log = {}
        for folder_p, final_folder_p in self.map.items():
            self.log[folder_p] = [file for file in final_folder_p.iterdir()]
        return self.log

    def load_map(self) -> dict[Path, Path]:
        """
        存储一层路径和深层路径的映射。
        键是一层路径，值是深层路径。

        :return: 包含路径映射的字典。
        """
        # 重置self.map和self.log 修复第二次使用simplify无法更新表格的bug --bug
        self.map = {}
        for folder_p in self.work_space.iterdir():
            if not folder_p.is_dir():
                continue
            if (final_folder_p := self.got_to_final(folder_p)) != folder_p:
                self.map[folder_p] = final_folder_p
        return self.map

    def got_to_final(self, folder_p: str | Path) -> Path:
        """
        递归查找最终的文件夹。

        :param folder_p: 文件夹路径。
        :return: 最终的文件夹路径。
        """
        folder_p = Path(folder_p) if isinstance(folder_p, str) else folder_p

        files = [folder for folder in folder_p.iterdir() if folder.is_dir() or folder.is_file()]
        return folder_p if len(files) != 1 else self.got_to_final(files[0])
