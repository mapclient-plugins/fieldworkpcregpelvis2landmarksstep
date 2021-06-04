# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 391)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.label_2 = QLabel(self.configGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.lineEditLASIS = QLineEdit(self.configGroupBox)
        self.lineEditLASIS.setObjectName(u"lineEditLASIS")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditLASIS)

        self.label_3 = QLabel(self.configGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lineEditRASIS = QLineEdit(self.configGroupBox)
        self.lineEditRASIS.setObjectName(u"lineEditRASIS")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEditRASIS)

        self.label_4 = QLabel(self.configGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.lineEditLPSIS = QLineEdit(self.configGroupBox)
        self.lineEditLPSIS.setObjectName(u"lineEditLPSIS")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEditLPSIS)

        self.label_5 = QLabel(self.configGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.lineEditRPSIS = QLineEdit(self.configGroupBox)
        self.lineEditRPSIS.setObjectName(u"lineEditRPSIS")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEditRPSIS)

        self.label_7 = QLabel(self.configGroupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_7)

        self.checkBoxGUI = QCheckBox(self.configGroupBox)
        self.checkBoxGUI.setObjectName(u"checkBoxGUI")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.checkBoxGUI)

        self.lineEditSacral = QLineEdit(self.configGroupBox)
        self.lineEditSacral.setObjectName(u"lineEditSacral")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEditSacral)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label)

        self.lineEditLHJC = QLineEdit(self.configGroupBox)
        self.lineEditLHJC.setObjectName(u"lineEditLHJC")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEditLHJC)

        self.lineEditRHJC = QLineEdit(self.configGroupBox)
        self.lineEditRHJC.setObjectName(u"lineEditRHJC")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEditRHJC)

        self.label_6 = QLabel(self.configGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_6)

        self.label_8 = QLabel(self.configGroupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.configGroupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.spinBoxNPCs = QSpinBox(self.configGroupBox)
        self.spinBoxNPCs.setObjectName(u"spinBoxNPCs")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBoxNPCs)

        self.comboBoxRegMode = QComboBox(self.configGroupBox)
        self.comboBoxRegMode.setObjectName(u"comboBoxRegMode")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBoxRegMode)

        self.label_10 = QLabel(self.configGroupBox)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_10)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("Dialog", u"identifier:  ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"LASIS:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"RASIS:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"LPSIS:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"RPSIS:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"GUI:", None))
        self.checkBoxGUI.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Sacral:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"LHJC:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"RHJC:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"PCs to Fit:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Registration Mode:", None))
    # retranslateUi

