from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QHeaderView, QMessageBox

from UI.main_ui import Ui_Form as MainUi
from Window.config import MyWindow as ConfigWindow
from format_file import FormateFile


class MyWindow(QWidget, MainUi):
    """
    自定义窗口类，继承自QWidget和Ui_Form
    """

    def __init__(self):
        """
        窗口初始化函数
        """
        super().__init__()

        self.config_window = ConfigWindow()
        self.ff = FormateFile()

        self.setupUi(self)
        self.bind()

    def bind(self):
        self.add_names_pb.clicked.connect(self.show_config)
        self.preview_pb.clicked.connect(lambda: self.update_tableView())

    def show_config(self):
        self.config_window.load_history()
        self.config_window.show()

    def update_tableView(self):
        self.ff.init(r"C:\Users\Alddp\Desktop\test")
        """ 更新tableview数据 """
        self.tableWidget.clear()
        try:
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(['folder', '', 'target'])
            self.tableWidget.setRowCount(len(self.ff.target_data.keys()))
            for i, (key, value) in enumerate(self.ff.target_data.items()):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(key))
                self.tableWidget.setItem(i, 1, QTableWidgetItem("->"))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(value))

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Error", f"Failed to load files: {e}")


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
