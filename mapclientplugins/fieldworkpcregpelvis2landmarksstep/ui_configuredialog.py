# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuredialog.ui'
#
# Created: Thu Jun 19 13:12:10 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(418, 391)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.configGroupBox = QtGui.QGroupBox(Dialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label0)
        self.lineEdit0 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName("lineEdit0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit0)
        self.label_2 = QtGui.QLabel(self.configGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditLASIS = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditLASIS.setObjectName("lineEditLASIS")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditLASIS)
        self.label_3 = QtGui.QLabel(self.configGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditRASIS = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditRASIS.setObjectName("lineEditRASIS")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditRASIS)
        self.label_4 = QtGui.QLabel(self.configGroupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditLPSIS = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditLPSIS.setObjectName("lineEditLPSIS")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditLPSIS)
        self.label_5 = QtGui.QLabel(self.configGroupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditRPSIS = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditRPSIS.setObjectName("lineEditRPSIS")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditRPSIS)
        self.label_7 = QtGui.QLabel(self.configGroupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.checkBoxGUI = QtGui.QCheckBox(self.configGroupBox)
        self.checkBoxGUI.setText("")
        self.checkBoxGUI.setObjectName("checkBoxGUI")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.checkBoxGUI)
        self.lineEditSacral = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditSacral.setObjectName("lineEditSacral")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEditSacral)
        self.label = QtGui.QLabel(self.configGroupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "ConfigureDialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("Dialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "LASIS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "RASIS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "LPSIS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "RPSIS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "GUI:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Sacral:", None, QtGui.QApplication.UnicodeUTF8))

