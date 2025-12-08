from PySide6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My App")
window.resize(400, 300)
window.show()

sys.exit(app.exec())