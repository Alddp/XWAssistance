# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'write_config_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPlainTextEdit,
                               QPushButton, QVBoxLayout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(368, 401)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.names_pte = QPlainTextEdit(Form)
        self.names_pte.setObjectName(u"names_pte")

        self.verticalLayout.addWidget(self.names_pte)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.f_names_pte = QPlainTextEdit(Form)
        self.f_names_pte.setObjectName(u"f_names_pte")

        self.verticalLayout_2.addWidget(self.f_names_pte)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.info_lb = QLabel(Form)
        self.info_lb.setObjectName(u"info_lb")
        self.info_lb.setMinimumSize(QSize(150, 10))
        self.info_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.info_lb, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.save_pb = QPushButton(Form)
        self.save_pb.setObjectName(u"save_pb")

        self.verticalLayout_3.addWidget(self.save_pb)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None))
        self.label_2.setText(
            QCoreApplication.translate("Form", u"\u8981\u683c\u5f0f\u5316\u7684\u6587\u4ef6\u540d", None))
        self.info_lb.setText("")
        self.save_pb.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi
