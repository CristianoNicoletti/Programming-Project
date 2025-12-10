import sys
import threading
import os
import signal

from PySide6 import QtWidgets
from main_window import MainWindow
from app import app as flask_app

# Start Flask backend in a separate thread
flask_thread = threading.Thread(target=lambda: flask_app.run(debug=False, port=5000), daemon=False)
flask_thread.start()

class MainWindowWithExit(MainWindow):
    def closeEvent(self, event):
        # Kill backend (Flask) and exit frontend
        os.kill(os.getpid(), signal.SIGTERM)

app = QtWidgets.QApplication(sys.argv)

main_window = MainWindowWithExit()
main_window.show()

res = app.exec()
print(res)