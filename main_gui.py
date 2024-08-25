import os
import sys

from PySide6.QtWidgets import (QApplication, QWidget,
                               QLabel, QVBoxLayout, QLineEdit, QPushButton,
                               QComboBox, QFileDialog)

from xw import main as xw


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.resize(200, 250)

    def init_ui(self):
        self.setAcceptDrops(True)
        self.setWindowTitle("XW")

        self.layout = QVBoxLayout()
        self.label = QLabel("拖动文件夹到此处")

        self.file_path_le = QLineEdit()

        self.command_cmb = QComboBox()
        self.add_cmd()

        self.choose_file_btn = QPushButton("选择文件")
        self.choose_file_btn.clicked.connect(self.open_file_dialog)

        self.start_btn = QPushButton("Start")
        self.start_btn.clicked.connect(self.start_exe)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.file_path_le)
        self.layout.addWidget(self.command_cmb)
        self.layout.addWidget(self.choose_file_btn)
        self.layout.addWidget(self.start_btn)
        self.setLayout(self.layout)

    def add_cmd(self):
        cmbs = ["help", "show", "simplify", "format"]
        self.command_cmb.addItems(cmbs)

    def open_file_dialog(self):
        # file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        file_path = QFileDialog.getExistingDirectory(self, "Select Directory")

        if file_path:
            self.file_path_le.setText(file_path)
            # self.label.setText(f"File path: {file_path}")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            self.path = urls[0].toLocalFile()
            if os.path.isfile(self.path):
                self.file_path_le.setText(self.path)
                # self.label.setText(f"File self.path: {self.path}")
            elif os.path.isdir(self.path):
                # self.label.setText(f"Folder self.pat: {self.path}")
                self.file_path_le.setText(self.path)
            else:
                self.label.setText("Dropped item is not a file or folder")

    def start_exe(self):
        cmd_type = self.command_cmb.currentText()
        file_path = self.file_path_le.text()
        exe_path_absolute = os.path.abspath(sys.argv[0])

        print(f"{exe_path_absolute=}")

        xw([exe_path_absolute, cmd_type, file_path])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()

    widget.show()
    sys.exit(app.exec())
