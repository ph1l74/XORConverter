# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(520, 153)
        self.txtEnter = QtGui.QPlainTextEdit(Dialog)
        self.txtEnter.setGeometry(QtCore.QRect(10, 10, 301, 131))
        self.txtEnter.setObjectName(_fromUtf8("txtEnter"))
        self.lvlResult = QtGui.QLabel(Dialog)
        self.lvlResult.setGeometry(QtCore.QRect(320, 10, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.lvlResult.setFont(font)
        self.lvlResult.setObjectName(_fromUtf8("lvlResult"))
        self.btnConvert = QtGui.QPushButton(Dialog)
        self.btnConvert.setGeometry(QtCore.QRect(330, 110, 181, 31))
        self.btnConvert.setObjectName(_fromUtf8("btnConvert"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "XOR Multibyte Converter", None))
        self.lvlResult.setText(_translate("Dialog", "", None))
        self.btnConvert.setText(_translate("Dialog", "Convert", None))

