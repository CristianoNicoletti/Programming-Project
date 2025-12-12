# Main PySide6 GUI window for the Library Management System
import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_main_window import Ui_main_window_widget
from media_item import Category


class MainWindow(QWidget, Ui_main_window_widget):
    """
    Main application window for the Library Management System GUI.
    Handles user interactions, communicates with the backend API, and updates the UI.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Library Management System")

        # Connect UI buttons to their respective handler methods
        self.refresh_available_btn.clicked.connect(self.refresh_available_books)
        self.add_media_btn.clicked.connect(self.add_media)
        self.search_btn.clicked.connect(self.search_books)

        # Populate category comboboxes with enum values
        categories = [cat.value for cat in Category]
        self.category_cmbx.addItems(categories)
        self.filter_by_category_cmbx.addItems(["All Categories"] + categories)
        self.available_for_borrowing_chkbx.setChecked(True)
        self.delete_btn.clicked.connect(self.delete_selected_search_result)
        self.search_result_list.itemSelectionChanged.connect(self.display_selected_search_result)
        self.available_lst.itemSelectionChanged.connect(self.display_selected_available_media)

        # Store last search results for lookup
        self._last_search_results = []

    def refresh_available_books(self):
        """
        Refresh the list of available media, optionally filtered by category.
        """
        print("refresh_available_books called")
        category = self.filter_by_category_cmbx.currentText()
        if category and category != "All Categories":
            response = requests.get(f'http://localhost:5000/available_media?category={category}')
        else:
            response = requests.get('http://localhost:5000/available_media')
        media_list = response.json()['media']
        self._last_available_list = media_list  # Store for available list lookup
        self.display_media_list(media_list)

    def add_media(self):
        """
        Collect data from the form and send a request to add a new media item.
        """
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
        self.available_for_borrowing_chkbx.setChecked(True)
        self.refresh_available_books()

    def search_books(self):
        """
        Search for media items by name and display the results.
        """
        search_term = self.search_by_name_line_edit.text()
        print(f"search_books called - Search term: {search_term}")
        response = requests.get(f'http://localhost:5000/search?name={search_term}')
        results = response.json()['results']
        self._last_search_results = results
        self.display_search_results(results)

    def display_media_list(self, media_list):
        """
        Display a list of available media in the UI list widget.
        """
        self.available_lst.clear()
        from PySide6.QtWidgets import QListWidgetItem
        for media in media_list:
            item_text = f"{media['name']} - {media['author']} ({media['category']})"
            list_item = QListWidgetItem(item_text)
            list_item.setData(Qt.UserRole, media['id'])
            self.available_lst.addItem(list_item)

    def display_search_results(self, results):
        """
        Display search results in the UI list widget.
        """
        self.search_result_list.clear()
        for media in results:
            item_text = f"{media['name']} - {media['author']} ({media['category']})"
            item = QStandardItem(item_text)
            from PySide6.QtWidgets import QListWidgetItem
            list_item = QListWidgetItem(item_text)
            list_item.setData(Qt.UserRole, media['id'])
            self.search_result_list.addItem(list_item)

    def display_selected_search_result(self):
        """
        Show details of the selected search result in a message box.
        """
        selected_items = self.search_result_list.selectedItems()
        if not selected_items:
            return
        selected_item = selected_items[0]
        media_id = selected_item.data(Qt.UserRole)
        media = next((m for m in self._last_search_results if m['id'] == media_id), None)
        if media:
            details = (
                f"Name: {media['name']}\n"
                f"Author: {media['author']}\n"
                f"Publication Date: {media['publication_date']}\n"
                f"Category: {media['category']}\n"
                f"Available for Borrowing: {media['available_for_borrowing']}\n"
                f"ID: {media['id']}"
            )
            QMessageBox.information(self, "Media Details", details)

    def display_selected_available_media(self):
        """
        Show details of the selected available media item.
        """
        selected_items = self.available_lst.selectedItems()
        if not selected_items:
            return
        selected_item = selected_items[0]
        media_id = selected_item.data(Qt.UserRole)
        media = next((m for m in getattr(self, '_last_available_list', []) if m['id'] == media_id), None)
        if media:
            details = (
                f"Name: {media['name']}\n"
                f"Author: {media['author']}\n"
                f"Publication Date: {media['publication_date']}\n"
                f"Category: {media['category']}\n"
                f"Available for Borrowing: {media['available_for_borrowing']}\n"
                f"ID: {media['id']}"
            )
            QMessageBox.information(self, "Media Details", details)

    def delete_selected_search_result(self):
        """
        Delete the selected media item from the search results via the backend API.
        """
        selected_items = self.search_result_list.selectedItems()
        if not selected_items:
            return
        selected_item = selected_items[0]
        media_id = selected_item.data(Qt.UserRole)
        response = requests.delete('http://localhost:5000/delete_media', json={'id': media_id})
        print(f"Delete response: {response.json()}")
        self.search_by_name_line_edit.clear()
        self.search_books()
        self._last_search_results = []