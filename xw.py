# 导入所需的PySide6模块和自定义模块
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QMessageBox

from UI.main_ui import Ui_Form as MainUi
from Window.config import MyWindow as ConfigWindow
from file_manage import FileFormater, FileSimplifier
from new_controls.GroupBox import DragDropGroupBox


class MyWindow(QWidget, MainUi):

    def __init__(self):
        """
        窗口初始化函数
        """
        super().__init__()
        self.setupUi(self)

        # 初始化FormateFile对象
        self.f_formater = FileFormater()
        self.f_simplifier = FileSimplifier()

        # 禁用返回按钮
        self.back_pb.setEnabled(False)

        # 移除并替换默认的groupBox为DragDropGroupBox
        self.verticalLayout.removeWidget(self.groupBox)
        self.groupBox.deleteLater()

        self.group_box = DragDropGroupBox(self.groupBox).insert_to_Layout(self.verticalLayout)

        # 当前模式
        self.chosen_model = self.comboBox.currentText()

        # 绑定信号与槽函数
        self.bind()

        # 设置默认模式
        self.set_format_model()

    def bind(self):
        # 显示配置窗口
        self.add_names_pb.clicked.connect(self.show_config)
        # 当文件拖拽到组框内时，更新工作空间
        self.group_box.file_dropped.connect(self.fp_led.setText)
        # 当输入框内容改变时，更新工作空间
        self.fp_led.textChanged.connect(self.update_work_space)

        self.comboBox.currentIndexChanged.connect(self.choose_function)

    # ============================================================================================
    def set_format_model(self):
        """ 切换模式为format """
        self.start_pb.clicked.connect(self.format_files)
        self.preview_pb.clicked.connect(self.show_format_table)

    def set_simplify_model(self):
        """ 切换模式为simplify """

        self.start_pb.clicked.connect(self.simplify_files)
        self.preview_pb.clicked.connect(self.show_simplify_table)
        ...

    def set_convert_model(self):
        """切换convert模式"""
        ...

    def choose_function(self, chosen_model: str):
        """根据combobox当前索引选择模式"""
        self.start_pb.clicked.disconnect()
        self.preview_pb.clicked.disconnect()
        match chosen_model:
            case 0:
                self.set_format_model()
            case 1:
                self.set_simplify_model()
            case 2:
                self.set_convert_model()
            case _:
                ...

    # ============================================================================================

    def format_files(self):
        # self.f_formater.work_space = self.fp_led.text()
        self.f_formater.start()
        QMessageBox.information(self, 'info', '完成')

    def simplify_files(self):
        # self.f_simplifier.work_space = self.fp_led.text()
        self.f_simplifier.start()
        QMessageBox.information(self, 'info', '完成')

    # ============================================================================================

    def update_work_space(self, string: str):
        """ 更新self.ff中记录工作目录的work_space属性, 并更新self.fp_led的内容 """
        self.f_formater.work_space = string
        self.f_simplifier.work_space = string

    @staticmethod
    def show_config():
        """
        显示配置窗口。

        该方法创建一个配置窗口实例，加载历史数据，并显示窗口。
        """
        edit_ui = ConfigWindow()
        edit_ui.load_history()
        edit_ui.show()

    # ============================================================================================
    def show_format_table(self):
        """
        更新表格视图。

        此方法首先初始化文件操作对象，然后清除现有的表格数据。接着，它尝试根据文件操作对象中的数据更新表格，
        包括设置列数、行数，并填充表格数据。如果在数据加载过程中发生异常，将显示错误消息对话框。
        """
        # 初始化文件操作对象
        self.f_formater.init(self.fp_led.text())
        # 清除现有的表格数据
        self.tableWidget.clear()

        try:
            # 获取目标数据的键的数量
            count = len(self.f_formater.target_data.keys())
            self.tableWidget.setColumnCount(3)
            # 设置表格的列标签
            self.tableWidget.setHorizontalHeaderLabels(['folder', f'匹配:{count}', 'target'])
            # 设置表格行数为键的数量
            self.tableWidget.setRowCount(count)
            # 遍历目标数据，填充表格
            for i, (key, value) in enumerate(self.f_formater.target_data.items()):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(key))
                self.tableWidget.setItem(i, 1, QTableWidgetItem("-->"))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(value))

            # 调整表格列宽以适应内容
            self.tableWidget.resizeColumnsToContents()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load files: {e}")

    def show_simplify_table(self):
        # 初始化文件操作对象
        self.f_simplifier.init(self.fp_led.text())
        # 清除现有的表格数据
        self.tableWidget.clear()

        # 设置表格的列标签
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['folder', '匹配:', 'target'])

        try:
            # 获取所有文件和对应的目标
            items = [(file, key) for key, files in self.f_simplifier.log.items() for file in files]

            # 设置行数
            self.tableWidget.setRowCount(len(items))

            # 填充表格
            for i, (file, key) in enumerate(items):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(file)))
                self.tableWidget.setItem(i, 1, QTableWidgetItem("-->"))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(key)))

            # 调整表格列宽以适应内容
            self.tableWidget.resizeColumnsToContents()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load files: {e}")

    def show_convert_table(self):
        ...
    # ============================================================================================


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
