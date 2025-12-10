import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_main_window import Ui_main_window_widget
from media_item import Category

class MainWindow(QWidget, Ui_main_window_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Library Management System")
        self.refresh_available_btn.clicked.connect(self.refresh_available_books)
        self.add_media_btn.clicked.connect(self.add_media)
        self.search_btn.clicked.connect(self.search_books)
        self.filter_by_category_cmbx.currentIndexChanged.connect(self.on_category_filter_changed)
        
        # Populate category comboboxes with enum values
        categories = [cat.value for cat in Category]
        self.category_cmbx.addItems(categories)
        self.filter_by_category_cmbx.addItems([""] + categories)

    def refresh_available_books(self):
        print("refresh_available_books called")
        response = requests.get('http://localhost:5000/available_media')
        media_list = response.json()['media']
        self.display_media_list(media_list)

    def add_media(self):
        print(f"add_media called - Name: {self.name_line_edit.text()}, Author: {self.author_line_edit.text()}, Date: {self.publication_date_date_edit.date().toString()}, Category: {self.category_cmbx.currentText()}, Available: {self.available_for_borrowing_chkbx.isChecked()}")
        data = {
            'name': self.name_line_edit.text(),
            'author': self.author_line_edit.text(),
            'publication_date': self.publication_date_date_edit.date().toString(),
            'category': self.category_cmbx.currentText(),
            'available_for_borrowing': self.available_for_borrowing_chkbx.isChecked()
        }
        response = requests.post('http://localhost:5000/add_media', json=data)
        print(f"Media added: {response.json()}")
        self.name_line_edit.clear()
        self.author_line_edit.clear()
        self.available_for_borrowing_chkbx.setChecked(False)
        self.refresh_available_books()

    def search_books(self):
        search_term = self.search_by_name_line_edit.text()
        print(f"search_books called - Search term: {search_term}")
        response = requests.get(f'http://localhost:5000/search?name={search_term}')
        results = response.json()['results']
        self.display_media_list(results)

    def on_category_filter_changed(self):
        category = self.filter_by_category_cmbx.currentText()
        print(f"on_category_filter_changed called - Category: {category}")
        if category:
            response = requests.get(f'http://localhost:5000/available_media?category={category}')
            media_list = response.json()['media']
            self.display_media_list(media_list)
        else:
            self.refresh_available_books()

    def display_media_list(self, media_list):
        model = QStandardItemModel()
        for media in media_list:
            item_text = f"{media['name']} - {media['author']} ({media['category']})"
            item = QStandardItem(item_text)
            item.setData(media['id'], Qt.UserRole)
            model.appendRow(item)
        self.available_lst.setModel(model)