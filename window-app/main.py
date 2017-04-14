import re
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import form

app = QApplication(sys.argv)
UI = form.Ui_Dialog()
MainWindow = QWidget()
UI.setupUi(MainWindow)
MainWindow.show()
QCoreApplication.processEvents()

def convertXOR():
    text = str(UI.txtEnter.toPlainText())
    list = re.split(' ', text)
    i = 0
    result = int('00', 16)
    while i < len(list):
        result = int(list[i], 16) ^ result
        i += 1
    result = "%X" % result
    result = str(result)
    UI.lvlResult.setText(result)
    UI.txtEnter.appendPlainText(" = " + result)

UI.btnConvert.clicked.connect(lambda: convertXOR())

sys.exit(app.exec_())