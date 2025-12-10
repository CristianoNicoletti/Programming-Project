# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDateTimeEdit, QHBoxLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_main_window_widget(object):
    def setupUi(self, main_window_widget):
        if not main_window_widget.objectName():
            main_window_widget.setObjectName(u"main_window_widget")
        main_window_widget.resize(805, 560)
        self.tab_widget = QTabWidget(main_window_widget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setGeometry(QRect(0, 0, 801, 561))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.filter_by_catergory_lbl = QLabel(self.tab)
        self.filter_by_catergory_lbl.setObjectName(u"filter_by_catergory_lbl")

        self.horizontalLayout_2.addWidget(self.filter_by_catergory_lbl)

        self.refresh_available_btn = QPushButton(self.tab)
        self.refresh_available_btn.setObjectName(u"refresh_available_btn")

        self.horizontalLayout_2.addWidget(self.refresh_available_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.browse_tab_verticallayout = QVBoxLayout()
        self.browse_tab_verticallayout.setObjectName(u"browse_tab_verticallayout")
        self.filter_by_category_cmbx = QComboBox(self.tab)
        self.filter_by_category_cmbx.setObjectName(u"filter_by_category_cmbx")

        self.browse_tab_verticallayout.addWidget(self.filter_by_category_cmbx)

        self.available_lst = QListView(self.tab)
        self.available_lst.setObjectName(u"available_lst")
        self.available_lst.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.browse_tab_verticallayout.addWidget(self.available_lst)


        self.verticalLayout_2.addLayout(self.browse_tab_verticallayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.tab_widget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget_2 = QWidget(self.tab_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 10, 741, 501))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.name_lbl = QLabel(self.layoutWidget_2)
        self.name_lbl.setObjectName(u"name_lbl")

        self.verticalLayout.addWidget(self.name_lbl)

        self.name_line_edit = QLineEdit(self.layoutWidget_2)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.verticalLayout.addWidget(self.name_line_edit)

        self.Author_lbl = QLabel(self.layoutWidget_2)
        self.Author_lbl.setObjectName(u"Author_lbl")

        self.verticalLayout.addWidget(self.Author_lbl)

        self.author_line_edit = QLineEdit(self.layoutWidget_2)
        self.author_line_edit.setObjectName(u"author_line_edit")

        self.verticalLayout.addWidget(self.author_line_edit)

        self.publication_date_lbl = QLabel(self.layoutWidget_2)
        self.publication_date_lbl.setObjectName(u"publication_date_lbl")

        self.verticalLayout.addWidget(self.publication_date_lbl)

        self.publication_date_date_edit = QDateEdit(self.layoutWidget_2)
        self.publication_date_date_edit.setObjectName(u"publication_date_date_edit")
        self.publication_date_date_edit.setMaximumDateTime(QDateTime(QDate(2100, 12, 31), QTime(19, 59, 59)))
        self.publication_date_date_edit.setMinimumDateTime(QDateTime(QDate(1752, 9, 14), QTime(22, 0, 0)))
        self.publication_date_date_edit.setMinimumDate(QDate(1752, 9, 14))
        self.publication_date_date_edit.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.publication_date_date_edit.setCalendarPopup(True)
        self.publication_date_date_edit.setDate(QDate(2000, 1, 1))

        self.verticalLayout.addWidget(self.publication_date_date_edit)

        self.category_lbl = QLabel(self.layoutWidget_2)
        self.category_lbl.setObjectName(u"category_lbl")

        self.verticalLayout.addWidget(self.category_lbl)

        self.category_cmbx = QComboBox(self.layoutWidget_2)
        self.category_cmbx.setObjectName(u"category_cmbx")

        self.verticalLayout.addWidget(self.category_cmbx)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.available_for_borrowing_lbl = QLabel(self.layoutWidget_2)
        self.available_for_borrowing_lbl.setObjectName(u"available_for_borrowing_lbl")

        self.horizontalLayout.addWidget(self.available_for_borrowing_lbl)

        self.available_for_borrowing_chkbx = QCheckBox(self.layoutWidget_2)
        self.available_for_borrowing_chkbx.setObjectName(u"available_for_borrowing_chkbx")

        self.horizontalLayout.addWidget(self.available_for_borrowing_chkbx)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.add_media_btn = QPushButton(self.layoutWidget_2)
        self.add_media_btn.setObjectName(u"add_media_btn")

        self.verticalLayout.addWidget(self.add_media_btn)

        self.tab_widget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.layoutWidget_3 = QWidget(self.tab_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 20, 741, 61))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.search_by_name_lbl = QLabel(self.layoutWidget_3)
        self.search_by_name_lbl.setObjectName(u"search_by_name_lbl")

        self.horizontalLayout_3.addWidget(self.search_by_name_lbl)

        self.search_btn = QPushButton(self.layoutWidget_3)
        self.search_btn.setObjectName(u"search_btn")

        self.horizontalLayout_3.addWidget(self.search_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.search_by_name_line_edit = QLineEdit(self.layoutWidget_3)
        self.search_by_name_line_edit.setObjectName(u"search_by_name_line_edit")

        self.verticalLayout_3.addWidget(self.search_by_name_line_edit)

        self.search_result_list = QListWidget(self.tab_3)
        self.search_result_list.setObjectName(u"search_result_list")
        self.search_result_list.setGeometry(QRect(20, 90, 741, 51))
        self.delete_btn = QPushButton(self.tab_3)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(680, 160, 75, 24))
        self.tab_widget.addTab(self.tab_3, "")

        self.retranslateUi(main_window_widget)

        self.tab_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(main_window_widget)
    # setupUi

    def retranslateUi(self, main_window_widget):
        main_window_widget.setWindowTitle(QCoreApplication.translate("main_window_widget", u"Form", None))
        self.filter_by_catergory_lbl.setText(QCoreApplication.translate("main_window_widget", u"Filter by Category", None))
        self.refresh_available_btn.setText(QCoreApplication.translate("main_window_widget", u"Refresh Available", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), QCoreApplication.translate("main_window_widget", u"Browse", None))
        self.name_lbl.setText(QCoreApplication.translate("main_window_widget", u"Name:", None))
        self.name_line_edit.setInputMask("")
        self.name_line_edit.setText("")
        self.name_line_edit.setPlaceholderText(QCoreApplication.translate("main_window_widget", u"e.g., The Great Gatsby", None))
        self.Author_lbl.setText(QCoreApplication.translate("main_window_widget", u"Author:", None))
        self.author_line_edit.setPlaceholderText(QCoreApplication.translate("main_window_widget", u"e.g., F. Scott Fitzgerald", None))
        self.publication_date_lbl.setText(QCoreApplication.translate("main_window_widget", u"Publication Date:", None))
        self.category_lbl.setText(QCoreApplication.translate("main_window_widget", u"Category:", None))
        self.available_for_borrowing_lbl.setText(QCoreApplication.translate("main_window_widget", u"Availabile for Borrowing:", None))
        self.available_for_borrowing_chkbx.setText("")
        self.add_media_btn.setText(QCoreApplication.translate("main_window_widget", u"Add media", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("main_window_widget", u"Add Media", None))
        self.search_by_name_lbl.setText(QCoreApplication.translate("main_window_widget", u"Search by Name:", None))
        self.search_btn.setText(QCoreApplication.translate("main_window_widget", u"Search", None))
        self.delete_btn.setText(QCoreApplication.translate("main_window_widget", u"Delete", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), QCoreApplication.translate("main_window_widget", u"Search", None))
    # retranslateUi

