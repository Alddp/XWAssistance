from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QMessageBox

from UI.main_ui import Ui_Form as MainUi
from Window.config import MyWindow as ConfigWindow
from format_file import FormateFile


class MyWindow(QWidget, MainUi):

    def __init__(self):
        """
        窗口初始化函数
        """
        super().__init__()
        self.setupUi(self)

        self.ff = FormateFile()

        self.back_pb.setEnabled(False)

        self.bind()

    def bind(self):
        self.add_names_pb.clicked.connect(self.show_config)
        self.preview_pb.clicked.connect(lambda: self.update_tableView())
        self.auto_width_pb.clicked.connect(lambda: self.tableWidget.resizeColumnsToContents())

    @staticmethod
    def show_config():
        edit_ui = ConfigWindow()
        edit_ui.load_history()
        edit_ui.show()

    def update_tableView(self):
        self.ff.init(self.fp_led.text())
        """ 更新tableview数据 """
        self.tableWidget.clear()
        try:
            count = len(self.ff.target_data.keys())
            # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(['folder', f'匹配:{count}', 'target'])
            self.tableWidget.setRowCount(count)
            for i, (key, value) in enumerate(self.ff.target_data.items()):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(key))
                self.tableWidget.setItem(i, 1, QTableWidgetItem("→"))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(value))

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Error", f"Failed to load files: {e}")


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
