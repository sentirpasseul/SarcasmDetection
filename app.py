from PyQt5 import QtCore, QtWidgets, QtGui
import sys
from PyQt5.QtGui import QIcon
from main.ui.main_ui  import Ui_MainWindow


class SarcasmDetection(QtWidgets.QMainWindow):
    def __init__(self):
        super(SarcasmDetection,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Определение сарказма в предложении')
        self.setWindowIcon(QIcon('main/src/icons/analyze.png'))

app = QtWidgets.QApplication([])
application = SarcasmDetection()
application.show()

sys.exit(app.exec_())