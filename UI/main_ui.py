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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(652, 508)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
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
        self.auto_width_pb = QPushButton(Form)
        self.auto_width_pb.setObjectName(u"auto_width_pb")

        self.horizontalLayout_3.addWidget(self.auto_width_pb)

        self.back_pb = QPushButton(Form)
        self.back_pb.setObjectName(u"back_pb")

        self.horizontalLayout_3.addWidget(self.back_pb)

        self.start_pb = QPushButton(Form)
        self.start_pb.setObjectName(u"start_pb")

        self.horizontalLayout_3.addWidget(self.start_pb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_names_pb = QPushButton(Form)
        self.add_names_pb.setObjectName(u"add_names_pb")

        self.verticalLayout.addWidget(self.add_names_pb)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(150, 100))
        self.groupBox.setMaximumSize(QSize(150, 100))
        self.groupBox.setAcceptDrops(True)

        self.verticalLayout.addWidget(self.groupBox, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fp_led = QLineEdit(Form)
        self.fp_led.setObjectName(u"fp_led")

        self.horizontalLayout.addWidget(self.fp_led)

        self.select_fp_tb = QToolButton(Form)
        self.select_fp_tb.setObjectName(u"select_fp_tb")

        self.horizontalLayout.addWidget(self.select_fp_tb)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.preview_pb = QPushButton(Form)
        self.preview_pb.setObjectName(u"preview_pb")

        self.verticalLayout.addWidget(self.preview_pb)


        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_led.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5173\u952e\u8bcd", None))
        self.search_pb.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.auto_width_pb.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5217\u5bbd", None))
        self.back_pb.setText(QCoreApplication.translate("Form", u"\u64a4\u9500", None))
        self.start_pb.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.add_names_pb.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u540d\u5355", None))
        self.groupBox.setTitle("")
        self.select_fp_tb.setText(QCoreApplication.translate("Form", u"...", None))
        self.preview_pb.setText(QCoreApplication.translate("Form", u"\u9884\u89c8", None))
    # retranslateUi

