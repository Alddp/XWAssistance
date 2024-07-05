import pylnk3


class Shortcut:
    """快捷方式类"""

    @staticmethod
    def get_lnk_target(lnk_path) -> str:
        """获取快捷方式指向的路径"""
        lnk = pylnk3.Lnk(lnk_path)
        return lnk.path

    @staticmethod
    def is_lnk(lnk_path) -> bool:
        """判断文件是否为快捷方式"""
        with open(lnk_path, 'rb') as f:
            return pylnk3.is_lnk(f)
