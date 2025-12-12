from main_window import MainWindow
from PySide6.QtWidgets import QApplication

def test_category_combobox_populated():
    app = QApplication([])
    window = MainWindow()
    categories = [window.category_cmbx.itemText(i) for i in range(window.category_cmbx.count())]
    assert "book" in categories
    assert "film" in categories
    assert "magazine" in categories
    app.quit()