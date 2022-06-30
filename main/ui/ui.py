import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MainApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text_header = QtWidgets.QLabel('Здравствуйте! Данное программное приложение разработано для анализа '
                           'текстов на предмет сарказма в них', alignment=QtCore.Qt.AlignLeft)
        self.text_body = QtWidgets.QLabel('Введите текст для анализа:', alignment=QtCore.Qt.AlignLeft)
        self.input_box = QtWidgets.QLineEdit(self)
        self.input_box.move(30,30)
        self.input_box.resize(300, 300)



        self.list_table_body = [self.text_body, self.input_box]
        ##self.table_body = QtWidgets.QTableWidget(self.list_table_body)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text_header)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MainApplication()
    widget.resize(1200, 600)
    widget.show()

    sys.exit(app.exec())