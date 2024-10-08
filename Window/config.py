from PySide6.QtWidgets import QWidget, QApplication, QMessageBox

from UI.write_config_ui import Ui_Form as ConfigUI
from file_manage import FileFormater


class MyWindow(QWidget, ConfigUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ff = FileFormater()

        self.bind()

    def bind(self):
        """
        绑定信号和槽
        """
        # 当点击保存按钮时，调用write_config函数
        self.save_pb.clicked.connect(self.write_config)
        self.close_pb.clicked.connect(lambda: self.close())

        # 当names_pte和f_names_pte的文本内容发生改变时，启用保存按钮
        self.names_pte.textChanged.connect(self.update_files_count)
        self.f_names_pte.textChanged.connect(self.update_files_count)

    def update_files_count(self):
        self.save_pb.setEnabled(True)
        names_len = len(self.names_pte.toPlainText().split('\n'))
        f_names_len = len(self.f_names_pte.toPlainText().split('\n'))

        self.name_lb.setText(f"姓名:{names_len}")
        self.f_name_lb.setText(f"要格式化的姓名:{f_names_len}")

    def load_history(self):
        """ 从配置文件中加载历史数据，并将其显示在界面上"""

        try:
            names, f_names = self.ff.read_data(FileFormater.config_path)

            self.names_pte.setPlainText('\n'.join(names))
            self.f_names_pte.setPlainText('\n'.join(f_names))
            self.save_pb.setEnabled(False)
        except Exception as e:
            print(e)

    def write_config(self):
        """
        将窗口的数据写入./config/data.csv中

        此方法首先从names_pte和f_names_pte中读取文本内容，将其分割成列表，
        并移除列表项中的前后空白字符。然后调用FormateFile的write_formate_config方法
        将处理后的列表写入到配置文件中。最后，更新界面信息栏，显示"保存成功!"，
        并禁用保存按钮，防止重复保存操作。
        """
        # 分割数据
        names = [name.strip() for name in self.names_pte.toPlainText().split("\n") if name]
        f_names = [name.strip() for name in self.f_names_pte.toPlainText().split("\n") if name]
        # 调用格式化文件处理类的写配置方法，将处理后的数据列表写入文件
        try:
            FileFormater.write_formate_config(names, f_names)
            # 更新界面信息栏，通知用户配置已成功保存
            self.info_lb.setText("保存成功!")
            self.save_pb.setEnabled(False)
        except ValueError as e:
            QMessageBox.critical(self, "Error", f"{e}")


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
