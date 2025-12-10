import sys
import threading

from PySide6 import QtWidgets
from main_window import MainWindow
from app import app as flask_app

# Start Flask backend in a separate thread
flask_thread = threading.Thread(target=lambda: flask_app.run(debug=False, port=5000), daemon=False)
flask_thread.start()

# Start PySide6 GUI
app = QtWidgets.QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

res = app.exec()
print(res)