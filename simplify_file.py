import shutil
from pathlib import Path
from typing import Dict, List


class FileSimplifier:
    """
    该类旨在简化文件路径，通过将复杂的目录结构映射到简单的文件名，
    以减少文件路径的复杂性，方便文件管理和访问。
    """

    def __init__(self, work_space: str):
        """
        初始化文件简化器，设定初始路径。

        :param work_space: 需要简化的文件或目录的路径。
        """
        self.map: Dict[Path, Path] = {}
        self.work_space = Path(work_space)
        self.log: Dict[Path, List[Path]] = {}

    def simplify(self):
        """
        简化文件路径的主方法，包括加载映射、日志和解析日志。
        """
        self.load_map()
        self.load_log()
        self.parse_log()

    def parse_log(self):
        """
        解析日志并处理文件移动过程中可能出现的冲突。
        """
        for main_folder, inner_files in self.log.items():
            crack_name = None
            renamed_file = None
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

    def load_log(self) -> Dict[Path, List[Path]]:
        """
        加载日志，记录每个文件夹及其对应的文件。

        :return: 包含文件夹及其文件的字典。
        """
        for final_folder_p, folder_p in self.map.items():
            self.log[folder_p] = [file for file in final_folder_p.iterdir()]
        return self.log

    def load_map(self) -> Dict[Path, Path]:
        """
        存储一层路径和深层路径的映射。
        键是深层路径，值是一层路径。

        :return: 包含路径映射的字典。
        """
        for folder_p in self.work_space.iterdir():
            if not folder_p.is_dir():
                continue
            if (final_folder_p := self.got_to_final(folder_p)) != folder_p:
                self.map[final_folder_p] = folder_p
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


if __name__ == '__main__':
    fs = FileSimplifier(r"C:\Users\Alddp\Desktop\main")
    fs.simplify()
