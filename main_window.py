from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_main_window import Ui_main_window_widget

class MainWindow(QWidget, Ui_main_window_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Library Management System")

    