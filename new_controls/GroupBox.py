from PySide6.QtCore import Signal, QSize, Qt

from PySide6.QtWidgets import QGroupBox, QWidget, QApplication, QBoxLayout, QVBoxLayout, QLabel


class DragDropGroupBox(QGroupBox):
    file_dropped = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.path = ""
        self.setAcceptDrops(True)
        self.setObjectName(u"groupBox")
        self.setMinimumSize(QSize(150, 100))
        self.setMaximumSize(QSize(150, 100))

        self.label = QLabel("拖动文件到这")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def insert_to_Layout(self, layout: QBoxLayout):
        layout.insertWidget(1, self, 0,
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
            print(self.path)
