import shutil
from pathlib import Path


class FileSimplifier:
    """
    该类旨在简化文件路径，通过将复杂的目录结构映射到简单的文件名，
    以减少文件路径的复杂性，方便文件管理和访问。
    """

    def __init__(self, path: str):
        """
        初始化文件简化器，设定初始路径。

        :param path: 需要简化的文件或目录的路径。
        """
        self.map: dict[Path, Path] = {}
        self.filename = Path(path)
        self.temps: list[Path] = []

    def simplify(self):
        """
        简化路径中的所有文件和目录。

        此方法遍历初始路径下的所有文件和目录，对每个文件或只包含一个文件的目录
        创建一个映射关系，最终将复杂的路径简化为直接指向最终文件的简单路径。
        """

        for file in self.filename.iterdir():

            # 排除其他类型文件
            if not file.is_dir():
                print("simplify:跳过", file.name)
                continue

            relative_path = []
            relative_path = self.__goto_final(file, relative_path)

            if len(relative_path) > 0:
                filename_temp = self.__create_temp_name(file)
                self.temps.append(filename_temp)

                final_file = filename_temp.joinpath(*relative_path)

                self.__add_map(final_file, file)

        self.move_with_map()
        self.del_temps()
        if len(self.map.keys()) == 0:
            print("没有要优化的文件")

    def move_with_map(self):
        """
        根据映射关系移动文件。

        此方法遍历映射关系，将文件从复杂路径移动到简化后的路径。
        """
        for key, value in self.map.items():
            key.rename(value)

            print(f"{key}\t---->\t{value}")
        # TODO:提取函数
        print(f"处理了{len(self.map.keys())}个文件")

    def __goto_final(self, file: Path, relative_path) -> list[str]:
        """
        递归地找到目录中的最终文件。

        :param file: 当前检查的文件或目录。
        :param relative_path: 从初始文件到当前文件的路径列表。
        :return: 当前文件到最终文件的相对路径。
        """
        if file.is_dir():
            filenames = [i for i in file.iterdir()]

            if len(filenames) == 1 and filenames[0].is_dir():
                inner_file = filenames[0]
                relative_path.append(inner_file.name)
                self.__goto_final(inner_file, relative_path)
        return relative_path

    def del_temps(self):
        """
        删除在简化过程中创建的临时文件夹。

        此方法用于清理简化过程中生成的临时文件夹，以保持文件系统的整洁。
        """
        for temp in self.temps:
            try:
                shutil.rmtree(temp)
                print(f"delete........ {temp}")
            except Exception as e:
                print(e)

    def __create_temp_name(self, filename: Path):
        """
        为文件创建一个临时名称。

        :param filename: 需要创建临时名称的文件。
        :return: 文件的临时名称。
        """
        # 为文件创建临时名称以避免命名冲突无法移动

        filename_temp = Path(str(filename) + "_temp")  # 添加临时temp后缀
        self.__add_map(filename, filename_temp)
        return filename_temp

    def __add_map(self, rsc, dst):
        """
        添加资源文件和目标文件的映射关系。

        :param rsc: 资源文件路径。
        :param dst: 目标文件路径。
        """
        self.map[rsc] = dst
