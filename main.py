import sys

from PySide6 import QtWidgets
from main_window import MainWindow

app = QtWidgets.QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()