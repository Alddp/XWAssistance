import csv

from PySide6.QtWidgets import QWidget, QApplication

from UI.write_config_ui import Ui_Form as ConfigUI
from format_file import FormateFile


class MyWindow(QWidget, ConfigUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.load_history()
        self.bind()

    def load_history(self):
        """
        从配置文件中加载历史数据，并将其显示在界面上。
        :return:
        """
        with open(FormateFile.config_path, 'r', encoding='utf8') as f:
            reader = list(csv.reader(f))

            names = map(lambda x: x[0], reader)
            f_names = map(lambda x: x[1], reader)

        self.names_pte.setPlainText('\n'.join(names))
        self.f_names_pte.setPlainText('\n'.join(f_names))
        self.save_pb.setEnabled(False)

    def bind(self):
        """
        绑定信号和槽
        """
        # 当点击保存按钮时，调用write_config函数
        self.save_pb.clicked.connect(self.write_config)

        # 当names_pte和f_names_pte的文本内容发生改变时，启用保存按钮
        self.names_pte.textChanged.connect(lambda: self.save_pb.setEnabled(True))
        self.f_names_pte.textChanged.connect(lambda: self.save_pb.setEnabled(True))

    def write_config(self):
        """
        将窗口的数据写入./res/data.csv中

        此方法首先从names_pte和f_names_pte中读取文本内容，将其分割成列表，
        并移除列表项中的前后空白字符。然后调用FormateFile的write_formate_config方法
        将处理后的列表写入到配置文件中。最后，更新界面信息栏，显示"保存成功!"，
        并禁用保存按钮，防止重复保存操作。
        """
        # 分割数据
        names = [name.strip() for name in self.names_pte.toPlainText().split("\n") if name]
        f_names = [name.strip() for name in self.f_names_pte.toPlainText().split("\n") if name]
        # 调用格式化文件处理类的写配置方法，将处理后的数据列表写入文件
        FormateFile.write_formate_config(names, f_names)
        # 更新界面信息栏，通知用户配置已成功保存
        self.info_lb.setText("保存成功!")
        # 禁用保存按钮，以避免重复保存操作
        self.save_pb.setEnabled(False)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
