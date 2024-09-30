from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QBoxLayout


class DragDropGroupBox(QGroupBox):
    file_dropped = Signal(str)

    def __init__(self, group_box: QGroupBox, parent=None):
        super().__init__(parent)

        # 复制 group_box 的属性
        # self.setTitle(group_box.title())
        # self.setStyleSheet(group_box.styleSheet())  # 复制样式表
        self.setCheckable(group_box.isCheckable())
        self.setMinimumSize(group_box.minimumSize())
        self.setMaximumSize(group_box.maximumSize())
        self.setAcceptDrops(True)

        # 开启拖放功能
        self.setAcceptDrops(True)
        self.path = ""

        # 创建标签
        self.label = QLabel("拖动文件到这")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def insert_to_Layout(self, layout: QBoxLayout):
        layout.insertWidget(2, self, 0,
                            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        return self

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.path = url.toLocalFile()
            self.file_dropped.emit(self.path)
            print(f"File dropped: {self.path}")
