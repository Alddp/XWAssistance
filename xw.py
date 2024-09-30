# 导入所需的PySide6模块和自定义模块
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QMessageBox

from UI.main_ui import Ui_Form as MainUi
from Window.config import MyWindow as ConfigWindow
from format_file import FormateFile
from new_controls.GroupBox import DragDropGroupBox


# 主窗口类，继承自QWidget和MainUi
class MyWindow(QWidget, MainUi):

    def __init__(self):
        """
        窗口初始化函数
        """
        super().__init__()
        self.setupUi(self)

        # 初始化FormateFile对象
        self.ff = FormateFile()

        # 禁用返回按钮
        self.back_pb.setEnabled(False)

        # 移除并替换默认的groupBox为DragDropGroupBox
        self.verticalLayout.removeWidget(self.groupBox)
        self.groupBox.deleteLater()

        self.group_box = DragDropGroupBox(self.groupBox).insert_to_Layout(self.verticalLayout)

        # 绑定信号与槽函数
        self.bind()

    def bind(self):

        # 显示配置窗口
        self.add_names_pb.clicked.connect(self.show_config)

        # 更新表格视图
        self.preview_pb.clicked.connect(lambda: self.update_tableView())

        # 当自动调整列宽按钮被点击时，调整表格视图的列宽
        self.auto_width_pb.clicked.connect(lambda: self.tableWidget.resizeColumnsToContents())

        # 当文件拖拽到组框内时，更新工作空间
        self.group_box.file_dropped.connect(self.update_work_space)

        # 执行重命名操作
        self.start_pb.clicked.connect(self.ff.rename_to_target)

    def update_work_space(self, string: str):
        """ 更新self.ff中记录工作目录的work_space属性, 并更新self.fp_led的内容 """
        self.fp_led.setText(string)
        self.ff.work_space = string

    @staticmethod
    def show_config():
        """
        显示配置窗口。

        该方法创建一个配置窗口实例，加载历史数据，并显示窗口。
        """
        edit_ui = ConfigWindow()
        edit_ui.load_history()
        edit_ui.show()

    def update_tableView(self):
        """
        更新表格视图。

        此方法首先初始化文件操作对象，然后清除现有的表格数据。接着，它尝试根据文件操作对象中的数据更新表格，
        包括设置列数、行数，并填充表格数据。如果在数据加载过程中发生异常，将显示错误消息对话框。
        """
        # 初始化文件操作对象
        self.ff.init(self.fp_led.text())
        # 清除现有的表格数据
        self.tableWidget.clear()

        try:
            # 获取目标数据的键的数量
            count = len(self.ff.target_data.keys())
            self.tableWidget.setColumnCount(3)
            # 设置表格的列标签
            self.tableWidget.setHorizontalHeaderLabels(['folder', f'匹配:{count}', 'target'])
            # 设置表格行数为键的数量
            self.tableWidget.setRowCount(count)
            # 遍历目标数据，填充表格
            for i, (key, value) in enumerate(self.ff.target_data.items()):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(key))
                self.tableWidget.setItem(i, 1, QTableWidgetItem("==>"))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(value))

            # 调整表格列宽以适应内容
            self.tableWidget.resizeColumnsToContents()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Error", f"Failed to load files: {e}")


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
