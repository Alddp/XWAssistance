# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(590, 578)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_led = QLineEdit(Form)
        self.search_led.setObjectName(u"search_led")

        self.horizontalLayout_2.addWidget(self.search_led)

        self.search_pb = QPushButton(Form)
        self.search_pb.setObjectName(u"search_pb")

        self.horizontalLayout_2.addWidget(self.search_pb)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 400))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setDragEnabled(True)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.show_skip_pb = QPushButton(Form)
        self.show_skip_pb.setObjectName(u"show_skip_pb")

        self.horizontalLayout_3.addWidget(self.show_skip_pb)

        self.back_pb = QPushButton(Form)
        self.back_pb.setObjectName(u"back_pb")

        self.horizontalLayout_3.addWidget(self.back_pb)

        self.start_pb = QPushButton(Form)
        self.start_pb.setObjectName(u"start_pb")

        self.horizontalLayout_3.addWidget(self.start_pb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_names_pb = QPushButton(Form)
        self.add_names_pb.setObjectName(u"add_names_pb")
        self.add_names_pb.setMaximumSize(QSize(275, 16777215))

        self.verticalLayout.addWidget(self.add_names_pb)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(200, 150))
        self.groupBox.setMaximumSize(QSize(300, 150))
        self.groupBox.setAcceptDrops(True)

        self.verticalLayout.addWidget(self.groupBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fp_led = QLineEdit(Form)
        self.fp_led.setObjectName(u"fp_led")
        self.fp_led.setMaximumSize(QSize(243, 16777215))

        self.horizontalLayout.addWidget(self.fp_led)

        self.select_fp_tb = QToolButton(Form)
        self.select_fp_tb.setObjectName(u"select_fp_tb")

        self.horizontalLayout.addWidget(self.select_fp_tb)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(152, 30))
        self.comboBox.setMaximumSize(QSize(300, 16777215))
        self.comboBox.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.comboBox.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";\n"
"font: 700 12pt \"Consolas\";")

        self.verticalLayout.addWidget(self.comboBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.preview_pb = QPushButton(Form)
        self.preview_pb.setObjectName(u"preview_pb")
        self.preview_pb.setMaximumSize(QSize(275, 16777215))

        self.verticalLayout.addWidget(self.preview_pb)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_led.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5173\u952e\u8bcd", None))
        self.search_pb.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.show_skip_pb.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u672a\u4ea4", None))
        self.back_pb.setText(QCoreApplication.translate("Form", u"\u64a4\u9500", None))
        self.start_pb.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.add_names_pb.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u540d\u5355", None))
        self.groupBox.setTitle("")
        self.select_fp_tb.setText(QCoreApplication.translate("Form", u"...", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Format", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Simplify", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Convert", None))

        self.preview_pb.setText(QCoreApplication.translate("Form", u"\u9884\u89c8", None))
    # retranslateUi

