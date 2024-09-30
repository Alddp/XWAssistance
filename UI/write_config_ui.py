# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'write_config_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(368, 430)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_lb = QLabel(Form)
        self.name_lb.setObjectName(u"name_lb")
        self.name_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.name_lb, 0, Qt.AlignmentFlag.AlignHCenter)

        self.names_pte = QPlainTextEdit(Form)
        self.names_pte.setObjectName(u"names_pte")
        self.names_pte.setMinimumSize(QSize(168, 0))

        self.verticalLayout.addWidget(self.names_pte)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.f_name_lb = QLabel(Form)
        self.f_name_lb.setObjectName(u"f_name_lb")
        self.f_name_lb.setMinimumSize(QSize(168, 0))
        self.f_name_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.f_name_lb, 0, Qt.AlignmentFlag.AlignHCenter)

        self.f_names_pte = QPlainTextEdit(Form)
        self.f_names_pte.setObjectName(u"f_names_pte")
        self.f_names_pte.setMinimumSize(QSize(168, 336))

        self.verticalLayout_2.addWidget(self.f_names_pte)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.info_lb = QLabel(Form)
        self.info_lb.setObjectName(u"info_lb")
        self.info_lb.setMinimumSize(QSize(150, 10))
        self.info_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.info_lb)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.save_pb = QPushButton(Form)
        self.save_pb.setObjectName(u"save_pb")

        self.horizontalLayout_2.addWidget(self.save_pb)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.close_pb = QPushButton(Form)
        self.close_pb.setObjectName(u"close_pb")

        self.horizontalLayout_2.addWidget(self.close_pb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name_lb.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None))
        self.f_name_lb.setText(QCoreApplication.translate("Form", u"\u8981\u683c\u5f0f\u5316\u7684\u6587\u4ef6\u540d", None))
        self.info_lb.setText("")
        self.save_pb.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.close_pb.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
    # retranslateUi

