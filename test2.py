import os
import shutil


def simplify_file(path):
    # path/filename
    if path is None:
        return

    # 首先获取path的父目录
    parent_dir = os.path.dirname(path)

    # 使用os.listdir获取path目录下的所有文件及子目录名
    filenames = os.listdir(path)

    # 遍历items，这里假设你只想移动文件，不移动子目录
    filenames_len = len(filenames)

    for filename in filenames:
        filename_path = os.path.join(path, filename)
        simplify_file(filename_path if filenames_len == 1 else None)

        if len(os.listdir(filename_path)) > 0:
            # 执行移动操作
            shutil.copyfile(filename_path, parent_dir)


        else:
            print(f"{filename_path}是空文件夹")


if __name__ == '__main__':
    for item in os.listdir(r"C:\Users\Alddp\Desktop\test"):
        simplify_file(os.path.join(r"C:\Users\Alddp\Desktop\test", item))
