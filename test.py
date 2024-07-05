import os
import shutil


class FileSimplifier:
    """
    path/filenames/file/inner_item
    """

    @staticmethod
    def simplify_file_path(path: str):
        """
        简化给定路径下的文件路径。
        
        该方法会遍历指定路径下的所有文件和文件夹。如果遇到文件夹，则递归调用自身以简化该文件夹内的路径；
        如果遇到文件，则直接输出提示信息，说明该路径不是文件夹。
        
        参数:
        path (str): 需要简化路径的文件夹路径。
        """
        # 遍历指定路径下的所有文件和文件夹
        for filenames in os.listdir(path):
            # 构建完整的文件或文件夹路径
            filenames_path = os.path.join(path, filenames)
            # 判断当前路径是否为文件夹
            if os.path.isdir(filenames_path):
                # 如果是文件夹，则递归调用自身以简化该文件夹内的路径
                FileSimplifier.simplify_file(filenames_path)
            else:
                pass

    @staticmethod
    def simplify_file(path, file):
        """
        如果文件夹下只有一个文件夹,则这个文件夹上移一层
        path/file/item
        """

        # 自身路径:filename_path
        # 内部文件:names
        # 内部文件数量: names_len
        # 内部文件路径:name_path = os.path.join(filename_path,names)
        item_len = len(os.listdir(file))
        items = os.listdir(file)
        if item_len == 1:
            item = items[0]
            FileSimplifier.simplify_file(os.path.join(path))

            # 移动文件


    @staticmethod
    def move_files_to_directory(src_dir, dst_dir):
        """
        将源目录下的文件移动到目标目录
        """
        for item in os.listdir(src_dir):
            src_file_path = os.path.join(src_dir, item)
            dst_file_path = os.path.join(dst_dir, item)
            try:
                shutil.move(src_file_path, dst_file_path)
            except shutil.Error as e:
                print(f"移动文件出错：{e}")
                # 处理文件重命名和移动的逻辑
                if os.path.exists(dst_file_path):
                    new_name = f"{item}_del"
                    dst_file_path = os.path.join(dst_dir, new_name)
                    os.rename(src_file_path, dst_file_path)
                    shutil.move(dst_file_path, src_file_path)
                    shutil.move(src_file_path, dst_file_path)
            except Exception as e:
                print(f"处理文件 {item} 时出错：{e}")
            else:
                print(f"文件 {item} 移动成功")


    @staticmethod
    def remove_empty_directory(directory):
        """
        安全删除空目录
        """
        if os.path.isdir(directory) and os.listdir(directory) == []:
            shutil.rmtree(directory)


if __name__ == '__main__':
    f = FileSimplifier()
    f.simplify_file_path(r"C:\Users\Alddp\Desktop\movetest")
