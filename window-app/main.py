import sys, re

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import form

app = QApplication(sys.argv)
UI = form.Ui_Dialog()
MainWindow = QWidget()
UI.setupUi(MainWindow)
MainWindow.show()
QCoreApplication.processEvents()


def convert_xor():
    entered_text = str(UI.txtEnter.toPlainText())
    result = int('00', 16)
    for i, element in enumerate(entered_text.split()):
        result = int(element, 16) ^ result
    result = "%X" % result
    result = str(result)
    UI.lvlResult.setText(result)
    UI.txtEnter.setPlainText(entered_text + " " + result)

UI.btnConvert.clicked.connect(lambda: convert_xor())

sys.exit(app.exec_())