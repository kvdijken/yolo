# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pydafkJXCn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1788, 1225)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(
            "/*Copyright (c) DevSec Studio. All rights reserved.\n"
            "\n"
            "MIT License\n"
            "\n"
            "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
            'of this software and associated documentation files (the "Software"), to deal\n'
            "in the Software without restriction, including without limitation the rights\n"
            "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
            "copies of the Software, and to permit persons to whom the Software is\n"
            "furnished to do so, subject to the following conditions:\n"
            "\n"
            "The above copyright notice and this permission notice shall be included in all\n"
            "copies or substantial portions of the Software.\n"
            "\n"
            "THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
            "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
            "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
            "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
            "LIABILITY, WHETHER IN AN ACT"
            "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
            "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
            "*/\n"
            "\n"
            "/*-----QWidget-----*/\n"
            "QWidget\n"
            "{\n"
            "	background-color: #3a3a3a;\n"
            "	color: #fff;\n"
            "	selection-background-color: #b78620;\n"
            "	selection-color: #000;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QLabel-----*/\n"
            "QLabel\n"
            "{\n"
            "	background-color: transparent;\n"
            "	color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QMenuBar-----*/\n"
            "QMenuBar \n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
            "	border: 1px solid #000;\n"
            "	color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QMenuBar::item \n"
            "{\n"
            "	background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QMenuBar::item:selected \n"
            "{\n"
            "	background-color: rgba(183, 134, 32, 20%);\n"
            "	border: 1px solid #b78620;\n"
            "	color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QMenuBar::item:pressed \n"
            "{\n"
            "	background-color: rgb(183, 134, 32);\n"
            ""
            "	border: 1px solid #b78620;\n"
            "	color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QMenu-----*/\n"
            "QMenu\n"
            "{\n"
            "    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
            "    border: 1px solid #222;\n"
            "    padding: 4px;\n"
            "	color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QMenu::item\n"
            "{\n"
            "    background-color: transparent;\n"
            "    padding: 2px 20px 2px 20px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QMenu::separator\n"
            "{\n"
            "   	background-color: rgb(183, 134, 32);\n"
            "	height: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QMenu::item:disabled\n"
            "{\n"
            "    color: #555;\n"
            "    background-color: transparent;\n"
            "    padding: 2px 20px 2px 20px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QMenu::item:selected\n"
            "{\n"
            "	background-color: rgba(183, 134, 32, 20%);\n"
            "	border: 1px solid #b78620;\n"
            "	color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QToolBar-----*/\n"
            "QToolBar\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69, 69, 69, 255),stop"
            ":1 rgba(58, 58, 58, 255));\n"
            "	border-top: none;\n"
            "	border-bottom: 1px solid #4f4f4f;\n"
            "	border-left: 1px solid #4f4f4f;\n"
            "	border-right: 1px solid #4f4f4f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QToolBar::separator\n"
            "{\n"
            "	background-color: #2e2e2e;\n"
            "	width: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QToolButton-----*/\n"
            "QToolButton \n"
            "{\n"
            "	background-color: transparent;\n"
            "	color: #fff;\n"
            "	padding: 5px;\n"
            "	padding-left: 8px;\n"
            "	padding-right: 8px;\n"
            "	margin-left: 1px;\n"
            "}\n"
            "\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "	background-color: rgba(183, 134, 32, 20%);\n"
            "	border: 1px solid #b78620;\n"
            "	color: #fff;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QToolButton:pressed\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
            "	border: 1px solid #b78620;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QToolButton:checked\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, "
            "50, 255));\n"
            "	border: 1px solid #222;\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QPushButton-----*/\n"
            "QPushButton\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
            "	color: #ffffff;\n"
            "	min-width: 80px;\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-radius: 3px;\n"
            "	border-color: #051a39;\n"
            "	padding: 5px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::flat\n"
            "{\n"
            "	background-color: transparent;\n"
            "	border: none;\n"
            "	color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::disabled\n"
            "{\n"
            "	background-color: #404040;\n"
            "	color: #656565;\n"
            "	border-color: #051a39;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::hover\n"
            "{\n"
            "	background-color: rgba(183, 134, 32, 20%);\n"
            "	border: 1px solid #b78620;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton::pressed\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
            "	border: 1px solid #b78620;\n"
            "\n"
            ""
            "}\n"
            "\n"
            "\n"
            "QPushButton::checked\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
            "	border: 1px solid #222;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QLineEdit-----*/\n"
            "QLineEdit\n"
            "{\n"
            "	background-color: #131313;\n"
            "	color : #eee;\n"
            "	border: 1px solid #343434;\n"
            "	border-radius: 2px;\n"
            "	padding: 3px;\n"
            "	padding-left: 5px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QPlainTExtEdit-----*/\n"
            "QPlainTextEdit\n"
            "{\n"
            "	background-color: #131313;\n"
            "	color : #eee;\n"
            "	border: 1px solid #343434;\n"
            "	border-radius: 2px;\n"
            "	padding: 3px;\n"
            "	padding-left: 5px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QTabBar-----*/\n"
            "QTabBar::tab\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
            "	color: #ffffff;\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: #666;\n"
            "	border-bottom: none;\n"
            "	padding: 5px;\n"
            "	padding-lef"
            "t: 15px;\n"
            "	padding-right: 15px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTabWidget::pane \n"
            "{\n"
            "	background-color: red;\n"
            "	border: 1px solid #666;\n"
            "	top: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTabBar::tab:last\n"
            "{\n"
            "	margin-right: 0; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTabBar::tab:first:!selected\n"
            "{\n"
            "	background-color: #0c0c0d;\n"
            "	margin-left: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTabBar::tab:!selected\n"
            "{\n"
            "	color: #b1b1b1;\n"
            "	border-bottom-style: solid;\n"
            "	background-color: #0c0c0d;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTabBar::tab:selected\n"
            "{\n"
            "	margin-bottom: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTabBar::tab:!selected:hover\n"
            "{\n"
            "	border-top-color: #b78620;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QComboBox-----*/\n"
            "QComboBox\n"
            "{\n"
            "    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
            "    border: 1px solid #000;\n"
            "    padding-left: 6px;\n"
            "    color: #ffffff;\n"
            "    height: 20px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QComboBox::disabled\n"
            "{\n"
            "	b"
            "ackground-color: #404040;\n"
            "	color: #656565;\n"
            "	border-color: #051a39;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QComboBox:on\n"
            "{\n"
            "    background-color: #b78620;\n"
            "	color: #000;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QComboBox QAbstractItemView\n"
            "{\n"
            "    background-color: #383838;\n"
            "    color: #ffffff;\n"
            "    border: 1px solid black;\n"
            "    selection-background-color: #b78620;\n"
            "    outline: 0;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QComboBox::drop-down\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 15px;\n"
            "    border-left-width: 1px;\n"
            "    border-left-color: black;\n"
            "    border-left-style: solid; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QComboBox::down-arrow\n"
            "{\n"
            "    image: url(://arrow-down.png);\n"
            "    width: 8px;\n"
            "    height: 8px;\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QSpinBox & QDateTimeEdit-----*/\n"
            "QSpinBox,\n"
            "QDateTimeEdit \n"
            "{\n"
            "    background"
            "-color: #131313;\n"
            "	color : #eee;\n"
            "	border: 1px solid #343434;\n"
            "	padding: 3px;\n"
            "	padding-left: 5px;\n"
            "    border-radius : 2px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSpinBox::up-button, \n"
            "QDateTimeEdit::up-button\n"
            "{\n"
            "	border-top-right-radius:2px;\n"
            "	background-color: #777777;\n"
            "    width: 16px; \n"
            "    border-width: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSpinBox::up-button:hover, \n"
            "QDateTimeEdit::up-button:hover\n"
            "{\n"
            "	background-color: #585858;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSpinBox::up-button:pressed, \n"
            "QDateTimeEdit::up-button:pressed\n"
            "{\n"
            "	background-color: #252525;\n"
            "    width: 16px; \n"
            "    border-width: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSpinBox::up-arrow,\n"
            "QDateTimeEdit::up-arrow\n"
            "{\n"
            "    image: url(://arrow-up.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSpinBox::down-button, \n"
            "QDateTimeEdit::down-button\n"
            "{\n"
            "	border-bottom-right-radius:2px;\n"
            "	background-color: #777777;\n"
            "    width: 16px; \n"
            "    border-width: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            ""
            "QSpinBox::down-button:hover, \n"
            "QDateTimeEdit::down-button:hover\n"
            "{\n"
            "	background-color: #585858;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSpinBox::down-button:pressed, \n"
            "QDateTimeEdit::down-button:pressed\n"
            "{\n"
            "	background-color: #252525;\n"
            "    width: 16px; \n"
            "    border-width: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSpinBox::down-arrow,\n"
            "QDateTimeEdit::down-arrow\n"
            "{\n"
            "    image: url(://arrow-down.png);\n"
            "    width: 7px;\n"
            "    height: 7px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QGroupBox-----*/\n"
            "QGroupBox \n"
            "{\n"
            "    border: 1px solid;\n"
            "    border-color: #666666;\n"
            "	border-radius: 5px;\n"
            "    margin-top: 20px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QGroupBox::title  \n"
            "{\n"
            "    background-color: transparent;\n"
            "    color: #eee;\n"
            "    subcontrol-origin: margin;\n"
            "    padding: 5px;\n"
            "	border-top-left-radius: 3px;\n"
            "	border-top-right-radius: 3px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QHeaderView-----*/\n"
            "QHeaderView::section\n"
            "{\n"
            "    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2"
            ":1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
            "	border: 1px solid #000;\n"
            "    color: #fff;\n"
            "    text-align: left;\n"
            "	padding: 4px;\n"
            "	\n"
            "}\n"
            "\n"
            "\n"
            "QHeaderView::section:disabled\n"
            "{\n"
            "    background-color: #525251;\n"
            "    color: #656565;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QHeaderView::section:checked\n"
            "{\n"
            "    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QHeaderView::section::vertical::first,\n"
            "QHeaderView::section::vertical::only-one\n"
            "{\n"
            "    border-top: 1px solid #353635;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QHeaderView::section::vertical\n"
            "{\n"
            "    border-top: 1px solid #353635;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QHeaderView::section::horizontal::first,\n"
            "QHeaderView::section::horizontal::only-one\n"
            "{\n"
            "    border-left: 1px solid #353635;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QHeaderView::section::horizontal\n"
            "{\n"
            "    border-left: 1px solid #353635;\n"
            "\n"
            ""
            "}\n"
            "\n"
            "\n"
            "QTableCornerButton::section\n"
            "{\n"
            "    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
            "	border: 1px solid #000;\n"
            "    color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QTreeWidget-----*/\n"
            "QTreeView\n"
            "{\n"
            "	show-decoration-selected: 1;\n"
            "	alternate-background-color: #3a3a3a;\n"
            "	selection-color: #fff;\n"
            "	background-color: #2d2d2d;\n"
            "	border: 1px solid gray;\n"
            "	padding-top : 5px;\n"
            "	color: #fff;\n"
            "	font: 8pt;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTreeView::item:selected\n"
            "{\n"
            "	color:#fff;\n"
            "	background-color: #b78620;\n"
            "	border-radius: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTreeView::item:!selected:hover\n"
            "{\n"
            "    background-color: #262626;\n"
            "    border: none;\n"
            "    color: white;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTreeView::branch:has-children:!has-siblings:closed,\n"
            "QTreeView::branch:closed:has-children:has-siblings \n"
            "{\n"
            "	image: url(://tree-closed.png);\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QTreeView::branc"
            "h:open:has-children:!has-siblings,\n"
            "QTreeView::branch:open:has-children:has-siblings  \n"
            "{\n"
            "	image: url(://tree-open.png);\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QListView-----*/\n"
            "QListView \n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
            "    border : none;\n"
            "    color: white;\n"
            "    show-decoration-selected: 1; \n"
            "    outline: 0;\n"
            "	border: 1px solid gray;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QListView::disabled \n"
            "{\n"
            "	background-color: #656565;\n"
            "	color: #1b1b1b;\n"
            "    border: 1px solid #656565;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QListView::item \n"
            "{\n"
            "	background-color: #2d2d2d;\n"
            "    padding: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QListView::item:alternate \n"
            "{\n"
            "    background-color: #3a3a3a;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QListView::item:selected \n"
            "{\n"
            "	background-color: #b78620;\n"
            "	border: 1px solid #b78620;\n"
            "	color: #fff;\n"
            "\n"
            ""
            "}\n"
            "\n"
            "\n"
            "QListView::item:selected:!active \n"
            "{\n"
            "	background-color: #b78620;\n"
            "	border: 1px solid #b78620;\n"
            "	color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QListView::item:selected:active \n"
            "{\n"
            "	background-color: #b78620;\n"
            "	border: 1px solid #b78620;\n"
            "	color: #fff;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QListView::item:hover {\n"
            "    background-color: #262626;\n"
            "    border: none;\n"
            "    color: white;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QCheckBox-----*/\n"
            "QCheckBox\n"
            "{\n"
            "	background-color: transparent;\n"
            "    color: lightgray;\n"
            "	border: none;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QCheckBox::indicator\n"
            "{\n"
            "    background-color: #323232;\n"
            "    border: 1px solid darkgray;\n"
            "    width: 12px;\n"
            "    height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QCheckBox::indicator:checked\n"
            "{\n"
            '    image:url("./resources/check.png");\n'
            "	background-color: #b78620;\n"
            "    border: 1px solid #3a546e;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QCheckBox::indicator:checked:disabled\n"
            "{\n"
            '    image:url("./resources/check.png");\n'
            "	back"
            "ground-color: #805D16;\n"
            "    border: 1px solid #3a546e;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QCheckBox::indicator:unchecked:hover\n"
            "{\n"
            "	border: 1px solid #b78620; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QCheckBox::disabled\n"
            "{\n"
            "	color: #656565;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QCheckBox::indicator:disabled\n"
            "{\n"
            "	background-color: #656565;\n"
            "	color: #656565;\n"
            "    border: 1px solid #656565;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QRadioButton-----*/\n"
            "QRadioButton \n"
            "{\n"
            "	color: lightgray;\n"
            "	background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QRadioButton::indicator::unchecked:hover \n"
            "{\n"
            "	background-color: lightgray;\n"
            "	border: 2px solid #b78620;\n"
            "	border-radius: 6px;\n"
            "}\n"
            "\n"
            "\n"
            "QRadioButton::indicator::checked \n"
            "{\n"
            "	border: 2px solid #b78620;\n"
            "	border-radius: 6px;\n"
            "	background-color: rgba(183,134,32,20%);  \n"
            "	width: 9px; \n"
            "	height: 9px; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QSlider-----*/\n"
            "QSlider::groove:horizontal \n"
            "{\n"
            "	background-color: transparent;\n"
            "	height: 3px;\n"
            "\n"
            ""
            "}\n"
            "\n"
            "\n"
            "QSlider::sub-page:horizontal \n"
            "{\n"
            "	background-color: #b78620;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSlider::add-page:horizontal \n"
            "{\n"
            "	background-color: #131313;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSlider::handle:horizontal \n"
            "{\n"
            "	background-color: #b78620;\n"
            "	width: 14px;\n"
            "	margin-top: -6px;\n"
            "	margin-bottom: -6px;\n"
            "	border-radius: 6px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSlider::handle:horizontal:hover \n"
            "{\n"
            "	background-color: #d89e25;\n"
            "	border-radius: 6px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSlider::sub-page:horizontal:disabled \n"
            "{\n"
            "	background-color: #bbb;\n"
            "	border-color: #999;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSlider::add-page:horizontal:disabled \n"
            "{\n"
            "	background-color: #eee;\n"
            "	border-color: #999;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QSlider::handle:horizontal:disabled \n"
            "{\n"
            "	background-color: #eee;\n"
            "	border: 1px solid #aaa;\n"
            "	border-radius: 3px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QScrollBar-----*/\n"
            "QScrollBar:horizontal\n"
            "{\n"
            "    border: 1px solid #222222;\n"
            "    background-color: #"
            "3d3d3d;\n"
            "    height: 15px;\n"
            "    margin: 0px 16px 0 16px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
            "	border: 1px solid #2d2d2d;\n"
            "    min-height: 20px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
            "	border: 1px solid #2d2d2d;\n"
            "    width: 15px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
            "	border: 1px solid #2d2d2d;\n"
            "    width: 15px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::right-arrow:horizon"
            "tal\n"
            "{\n"
            "    image: url(://arrow-right.png);\n"
            "    width: 6px;\n"
            "    height: 6px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::left-arrow:horizontal\n"
            "{\n"
            "    image: url(://arrow-left.png);\n"
            "    width: 6px;\n"
            "    height: 6px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "    background: none;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:vertical\n"
            "{\n"
            "    background-color: #3d3d3d;\n"
            "    width: 16px;\n"
            "	border: 1px solid #2d2d2d;\n"
            "    margin: 16px 0px 16px 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical\n"
            "{\n"
            "    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
            "	border: 1px solid #2d2d2d;\n"
            "    min-height: 20px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
            "	border: 1px solid #2d2d2d;\n"
            ""
            "    height: 15px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
            "	border: 1px solid #2d2d2d;\n"
            "    height: 15px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "    image: url(://arrow-up.png);\n"
            "    width: 6px;\n"
            "    height: 6px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical\n"
            "{\n"
            "    image: url(://arrow-down.png);\n"
            "    width: 6px;\n"
            "    height: 6px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            "    background: none;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "/*-----QProgressBar-----*/\n"
            "QProgressBar\n"
            "{\n"
            "    border: 1px solid #666666;\n"
            "    text-align: center;\n"
            "	color: #000;\n"
            "	font-weight: bold;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QProgres"
            "sBar::chunk\n"
            "{\n"
            "    background-color: #b78620;\n"
            "    width: 30px;\n"
            "    margin: 0.5px;\n"
            "\n"
            "}\n"
            ""
        )
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_THD_plotfile = QAction(MainWindow)
        self.actionSave_THD_plotfile.setObjectName("actionSave_THD_plotfile")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fraFFT = QGroupBox(self.centralwidget)
        self.fraFFT.setObjectName("fraFFT")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fraFFT.sizePolicy().hasHeightForWidth())
        self.fraFFT.setSizePolicy(sizePolicy1)
        self.fraFFT.setMinimumSize(QSize(250, 250))
        font = QFont()
        font.setPointSize(16)
        self.fraFFT.setFont(font)
        self.horizontalLayout_6 = QHBoxLayout(self.fraFFT)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fraFFT2 = QFrame(self.fraFFT)
        self.fraFFT2.setObjectName("fraFFT2")
        self.fraFFT2.setFrameShape(QFrame.StyledPanel)
        self.fraFFT2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.fraFFT2)

        self.gridLayout.addWidget(self.fraFFT, 1, 0, 1, 1)

        self.fraZoom = QGroupBox(self.centralwidget)
        self.fraZoom.setObjectName("fraZoom")
        sizePolicy1.setHeightForWidth(self.fraZoom.sizePolicy().hasHeightForWidth())
        self.fraZoom.setSizePolicy(sizePolicy1)
        self.fraZoom.setMinimumSize(QSize(250, 250))
        self.fraZoom.setFont(font)
        self.fraZoom.setAutoFillBackground(False)
        self.fraZoom.setFlat(False)
        self.fraZoom.setCheckable(False)
        self.horizontalLayout_3 = QHBoxLayout(self.fraZoom)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fraZoom2 = QFrame(self.fraZoom)
        self.fraZoom2.setObjectName("fraZoom2")
        self.fraZoom2.setFrameShape(QFrame.StyledPanel)
        self.fraZoom2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.fraZoom2)

        self.gridLayout.addWidget(self.fraZoom, 0, 1, 1, 1)

        self.fraOsc = QGroupBox(self.centralwidget)
        self.fraOsc.setObjectName("fraOsc")
        sizePolicy1.setHeightForWidth(self.fraOsc.sizePolicy().hasHeightForWidth())
        self.fraOsc.setSizePolicy(sizePolicy1)
        self.fraOsc.setMinimumSize(QSize(250, 250))
        self.fraOsc.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.fraOsc)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fraOsc2 = QFrame(self.fraOsc)
        self.fraOsc2.setObjectName("fraOsc2")
        self.fraOsc2.setFrameShape(QFrame.StyledPanel)
        self.fraOsc2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.fraOsc2)

        self.gridLayout.addWidget(self.fraOsc, 0, 0, 1, 1)

        self.fraTHD = QGroupBox(self.centralwidget)
        self.fraTHD.setObjectName("fraTHD")
        sizePolicy1.setHeightForWidth(self.fraTHD.sizePolicy().hasHeightForWidth())
        self.fraTHD.setSizePolicy(sizePolicy1)
        self.fraTHD.setMinimumSize(QSize(250, 250))
        self.fraTHD.setFont(font)
        self.gridLayout_2 = QGridLayout(self.fraTHD)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackTHD = QStackedWidget(self.fraTHD)
        self.stackTHD.setObjectName("stackTHD")
        self.pageFix = QWidget()
        self.pageFix.setObjectName("pageFix")
        self.verticalLayout_4 = QVBoxLayout(self.pageFix)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.lblTHD = QLabel(self.pageFix)
        self.lblTHD.setObjectName("lblTHD")
        font1 = QFont()
        font1.setPointSize(64)
        self.lblTHD.setFont(font1)
        self.lblTHD.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblTHD)

        self.lblS0 = QLabel(self.pageFix)
        self.lblS0.setObjectName("lblS0")
        self.lblS0.setFont(font1)
        self.lblS0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblS0)

        self.lblS1 = QLabel(self.pageFix)
        self.lblS1.setObjectName("lblS1")
        self.lblS1.setFont(font1)
        self.lblS1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblS1)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.lblAverage = QLabel(self.pageFix)
        self.lblAverage.setObjectName("lblAverage")
        self.lblAverage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblAverage)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.stackTHD.addWidget(self.pageFix)
        self.pageSweep = QWidget()
        self.pageSweep.setObjectName("pageSweep")
        self.stackTHD.addWidget(self.pageSweep)

        self.gridLayout_2.addWidget(self.stackTHD, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.fraTHD, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.widgetRight = QWidget(self.centralwidget)
        self.widgetRight.setObjectName("widgetRight")
        self.widgetRight.setAutoFillBackground(False)
        self.verticalLayout_6 = QVBoxLayout(self.widgetRight)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widgetRight)
        self.frame_2.setObjectName("frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.widgetControls = QWidget(self.frame_2)
        self.widgetControls.setObjectName("widgetControls")
        self.verticalLayout_3 = QVBoxLayout(self.widgetControls)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupSignalGenerator = QGroupBox(self.widgetControls)
        self.groupSignalGenerator.setObjectName("groupSignalGenerator")
        self.groupSignalGenerator.setCheckable(False)
        self.groupSignalGenerator.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.groupSignalGenerator)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QFrame(self.groupSignalGenerator)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.formLayout_7 = QFormLayout(self.frame)
        self.formLayout_7.setObjectName("formLayout_7")
        self.formLayout_7.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label)

        self.cboSDG_ch = QComboBox(self.frame)
        self.cboSDG_ch.addItem("")
        self.cboSDG_ch.addItem("")
        self.cboSDG_ch.setObjectName("cboSDG_ch")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.cboSDG_ch)

        self.checkUseSDG = QCheckBox(self.frame)
        self.checkUseSDG.setObjectName("checkUseSDG")
        self.checkUseSDG.setChecked(True)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.checkUseSDG)

        self.verticalLayout.addWidget(self.frame)

        self.tabSDGModulation = QTabWidget(self.groupSignalGenerator)
        self.tabSDGModulation.setObjectName("tabSDGModulation")
        self.tabCW = QWidget()
        self.tabCW.setObjectName("tabCW")
        self.formLayout_2 = QFormLayout(self.tabCW)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_26 = QLabel(self.tabCW)
        self.label_26.setObjectName("label_26")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_26)

        self.edtCW_amplitude = QLineEdit(self.tabCW)
        self.edtCW_amplitude.setObjectName("edtCW_amplitude")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.edtCW_amplitude)

        self.tabSDGModulation.addTab(self.tabCW, "")
        self.tabAM = QWidget()
        self.tabAM.setObjectName("tabAM")
        self.formLayout_3 = QFormLayout(self.tabAM)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_3.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_14 = QLabel(self.tabAM)
        self.label_14.setObjectName("label_14")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.edtAM_freq = QLineEdit(self.tabAM)
        self.edtAM_freq.setObjectName("edtAM_freq")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.edtAM_freq)

        self.label_10 = QLabel(self.tabAM)
        self.label_10.setObjectName("label_10")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.edtAM_modDepth = QLineEdit(self.tabAM)
        self.edtAM_modDepth.setObjectName("edtAM_modDepth")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.edtAM_modDepth)

        self.label_21 = QLabel(self.tabAM)
        self.label_21.setObjectName("label_21")
        self.label_21.setTextFormat(Qt.AutoText)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_21)

        self.edtAM_amplitude = QLineEdit(self.tabAM)
        self.edtAM_amplitude.setObjectName("edtAM_amplitude")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.edtAM_amplitude)

        self.tabSDGModulation.addTab(self.tabAM, "")
        self.tabFM = QWidget()
        self.tabFM.setObjectName("tabFM")
        self.formLayout_4 = QFormLayout(self.tabFM)
        self.formLayout_4.setObjectName("formLayout_4")
        self.formLayout_4.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_13 = QLabel(self.tabFM)
        self.label_13.setObjectName("label_13")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.edtFM_freq = QLineEdit(self.tabFM)
        self.edtFM_freq.setObjectName("edtFM_freq")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.edtFM_freq)

        self.label_12 = QLabel(self.tabFM)
        self.label_12.setObjectName("label_12")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.edtFM_freqDev = QLineEdit(self.tabFM)
        self.edtFM_freqDev.setObjectName("edtFM_freqDev")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.edtFM_freqDev)

        self.label_22 = QLabel(self.tabFM)
        self.label_22.setObjectName("label_22")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_22)

        self.edtFM_amplitude = QLineEdit(self.tabFM)
        self.edtFM_amplitude.setObjectName("edtFM_amplitude")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.edtFM_amplitude)

        self.tabSDGModulation.addTab(self.tabFM, "")

        self.verticalLayout.addWidget(self.tabSDGModulation)

        self.verticalLayout_3.addWidget(self.groupSignalGenerator)

        self.groupBox = QGroupBox(self.widgetControls)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabSDGFixedSweep = QTabWidget(self.groupBox)
        self.tabSDGFixedSweep.setObjectName("tabSDGFixedSweep")
        self.tabFixed = QWidget()
        self.tabFixed.setObjectName("tabFixed")
        self.formLayout_6 = QFormLayout(self.tabFixed)
        self.formLayout_6.setObjectName("formLayout_6")
        self.formLayout_6.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_3 = QLabel(self.tabFixed)
        self.label_3.setObjectName("label_3")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.edtSDGFixed_f0 = QLineEdit(self.tabFixed)
        self.edtSDGFixed_f0.setObjectName("edtSDGFixed_f0")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.edtSDGFixed_f0)

        self.tabSDGFixedSweep.addTab(self.tabFixed, "")
        self.tabSweep = QWidget()
        self.tabSweep.setObjectName("tabSweep")
        self.formLayout = QFormLayout(self.tabSweep)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_15 = QLabel(self.tabSweep)
        self.label_15.setObjectName("label_15")
        self.label_15.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.edtSDGSweep_minFreq = QLineEdit(self.tabSweep)
        self.edtSDGSweep_minFreq.setObjectName("edtSDGSweep_minFreq")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edtSDGSweep_minFreq)

        self.label_20 = QLabel(self.tabSweep)
        self.label_20.setObjectName("label_20")
        self.label_20.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_20)

        self.edtSDGSweep_maxFreq = QLineEdit(self.tabSweep)
        self.edtSDGSweep_maxFreq.setObjectName("edtSDGSweep_maxFreq")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edtSDGSweep_maxFreq)

        self.label_23 = QLabel(self.tabSweep)
        self.label_23.setObjectName("label_23")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_23)

        self.edtSDGSweep_step = QLineEdit(self.tabSweep)
        self.edtSDGSweep_step.setObjectName("edtSDGSweep_step")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edtSDGSweep_step)

        self.tabSDGFixedSweep.addTab(self.tabSweep, "")

        self.verticalLayout_5.addWidget(self.tabSDGFixedSweep)

        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupOSC = QGroupBox(self.widgetControls)
        self.groupOSC.setObjectName("groupOSC")
        self.formLayout_8 = QFormLayout(self.groupOSC)
        self.formLayout_8.setObjectName("formLayout_8")
        self.formLayout_8.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_2 = QLabel(self.groupOSC)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cboSDS_ch = QComboBox(self.groupOSC)
        self.cboSDS_ch.addItem("")
        self.cboSDS_ch.addItem("")
        self.cboSDS_ch.setObjectName("cboSDS_ch")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.cboSDS_ch)

        self.label_24 = QLabel(self.groupOSC)
        self.label_24.setObjectName("label_24")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_24)

        self.checkSDS_autoVertical = QCheckBox(self.groupOSC)
        self.checkSDS_autoVertical.setObjectName("checkSDS_autoVertical")

        self.formLayout_8.setWidget(
            1, QFormLayout.FieldRole, self.checkSDS_autoVertical
        )

        self.label_25 = QLabel(self.groupOSC)
        self.label_25.setObjectName("label_25")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_25)

        self.checkSDS_autoHorizontal = QCheckBox(self.groupOSC)
        self.checkSDS_autoHorizontal.setObjectName("checkSDS_autoHorizontal")
        self.checkSDS_autoHorizontal.setChecked(True)

        self.formLayout_8.setWidget(
            2, QFormLayout.FieldRole, self.checkSDS_autoHorizontal
        )

        self.label_4 = QLabel(self.groupOSC)
        self.label_4.setObjectName("label_4")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.edtSDSPeriods = QLineEdit(self.groupOSC)
        self.edtSDSPeriods.setObjectName("edtSDSPeriods")

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.edtSDSPeriods)

        self.verticalLayout_3.addWidget(self.groupOSC)

        self.groupTHD = QGroupBox(self.widgetControls)
        self.groupTHD.setObjectName("groupTHD")
        self.groupTHD.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.formLayout_5 = QFormLayout(self.groupTHD)
        self.formLayout_5.setObjectName("formLayout_5")
        self.formLayout_5.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_5 = QLabel(self.groupTHD)
        self.label_5.setObjectName("label_5")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.edtTHDHarmonics = QLineEdit(self.groupTHD)
        self.edtTHDHarmonics.setObjectName("edtTHDHarmonics")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.edtTHDHarmonics)

        self.label_16 = QLabel(self.groupTHD)
        self.label_16.setObjectName("label_16")
        self.label_16.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.edtTHDFloor = QLineEdit(self.groupTHD)
        self.edtTHDFloor.setObjectName("edtTHDFloor")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.edtTHDFloor)

        self.label_9 = QLabel(self.groupTHD)
        self.label_9.setObjectName("label_9")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.edtTHDAverage = QLineEdit(self.groupTHD)
        self.edtTHDAverage.setObjectName("edtTHDAverage")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.edtTHDAverage)

        self.verticalLayout_3.addWidget(self.groupTHD)

        self.groupFFTPlot = QGroupBox(self.widgetControls)
        self.groupFFTPlot.setObjectName("groupFFTPlot")
        self.formLayout_9 = QFormLayout(self.groupFFTPlot)
        self.formLayout_9.setObjectName("formLayout_9")
        self.formLayout_9.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_17 = QLabel(self.groupFFTPlot)
        self.label_17.setObjectName("label_17")
        self.label_17.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_17)

        self.edtFFTPlotMinY = QLineEdit(self.groupFFTPlot)
        self.edtFFTPlotMinY.setObjectName("edtFFTPlotMinY")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.edtFFTPlotMinY)

        self.label_18 = QLabel(self.groupFFTPlot)
        self.label_18.setObjectName("label_18")
        self.label_18.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.edtFFTPlotMaxY = QLineEdit(self.groupFFTPlot)
        self.edtFFTPlotMaxY.setObjectName("edtFFTPlotMaxY")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.edtFFTPlotMaxY)

        self.verticalLayout_3.addWidget(self.groupFFTPlot)

        self.groupTHDPlot = QGroupBox(self.widgetControls)
        self.groupTHDPlot.setObjectName("groupTHDPlot")
        self.formLayout_10 = QFormLayout(self.groupTHDPlot)
        self.formLayout_10.setObjectName("formLayout_10")
        self.formLayout_10.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_6 = QLabel(self.groupTHDPlot)
        self.label_6.setObjectName("label_6")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.edtTHDAmplitude = QCheckBox(self.groupTHDPlot)
        self.edtTHDAmplitude.setObjectName("edtTHDAmplitude")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.edtTHDAmplitude)

        self.verticalLayout_3.addWidget(self.groupTHDPlot)

        self.verticalLayout_2.addWidget(self.widgetControls)

        self.groupComm = QGroupBox(self.frame_2)
        self.groupComm.setObjectName("groupComm")
        self.horizontalLayout_2 = QHBoxLayout(self.groupComm)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textComm = QTextEdit(self.groupComm)
        self.textComm.setObjectName("textComm")
        font2 = QFont()
        font2.setFamily("Monospace")
        self.textComm.setFont(font2)
        self.textComm.setLineWrapMode(QTextEdit.NoWrap)
        self.textComm.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textComm)

        self.verticalLayout_2.addWidget(self.groupComm)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btnStop = QPushButton(self.frame_5)
        self.btnStop.setObjectName("btnStop")
        self.btnStop.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.btnStop)

        self.btnStart = QPushButton(self.frame_5)
        self.btnStart.setObjectName("btnStart")

        self.horizontalLayout_4.addWidget(self.btnStart)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.verticalLayout_6.addWidget(self.frame_2)

        self.horizontalLayout.addWidget(self.widgetRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1788, 25))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.checkUseSDG, self.cboSDG_ch)
        QWidget.setTabOrder(self.cboSDG_ch, self.tabSDGModulation)
        QWidget.setTabOrder(self.tabSDGModulation, self.edtCW_amplitude)
        QWidget.setTabOrder(self.edtCW_amplitude, self.edtAM_freq)
        QWidget.setTabOrder(self.edtAM_freq, self.edtAM_amplitude)
        QWidget.setTabOrder(self.edtAM_amplitude, self.edtAM_modDepth)
        QWidget.setTabOrder(self.edtAM_modDepth, self.edtFM_freq)
        QWidget.setTabOrder(self.edtFM_freq, self.edtFM_amplitude)
        QWidget.setTabOrder(self.edtFM_amplitude, self.edtFM_freqDev)
        QWidget.setTabOrder(self.edtFM_freqDev, self.tabSDGFixedSweep)
        QWidget.setTabOrder(self.tabSDGFixedSweep, self.edtSDGFixed_f0)
        QWidget.setTabOrder(self.edtSDGFixed_f0, self.edtSDGSweep_minFreq)
        QWidget.setTabOrder(self.edtSDGSweep_minFreq, self.edtSDGSweep_maxFreq)
        QWidget.setTabOrder(self.edtSDGSweep_maxFreq, self.edtSDGSweep_step)
        QWidget.setTabOrder(self.edtSDGSweep_step, self.cboSDS_ch)
        QWidget.setTabOrder(self.cboSDS_ch, self.checkSDS_autoVertical)
        QWidget.setTabOrder(self.checkSDS_autoVertical, self.checkSDS_autoHorizontal)
        QWidget.setTabOrder(self.checkSDS_autoHorizontal, self.edtSDSPeriods)
        QWidget.setTabOrder(self.edtSDSPeriods, self.edtTHDHarmonics)
        QWidget.setTabOrder(self.edtTHDHarmonics, self.edtTHDFloor)
        QWidget.setTabOrder(self.edtTHDFloor, self.edtTHDAverage)
        QWidget.setTabOrder(self.edtTHDAverage, self.edtFFTPlotMinY)
        QWidget.setTabOrder(self.edtFFTPlotMinY, self.edtFFTPlotMaxY)
        QWidget.setTabOrder(self.edtFFTPlotMaxY, self.edtTHDAmplitude)
        QWidget.setTabOrder(self.edtTHDAmplitude, self.textComm)
        QWidget.setTabOrder(self.textComm, self.btnStop)
        QWidget.setTabOrder(self.btnStop, self.btnStart)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_THD_plotfile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSettings.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)

        self.stackTHD.setCurrentIndex(0)
        self.tabSDGModulation.setCurrentIndex(0)
        self.tabSDGFixedSweep.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Yolo", None)
        )
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "About...", None)
        )
        self.actionSave_THD_plotfile.setText(
            QCoreApplication.translate("MainWindow", "Save THD plotfile", None)
        )
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", "Quit", None))
        self.actionSettings.setText(
            QCoreApplication.translate("MainWindow", "Settings ...", None)
        )
        self.fraFFT.setTitle(QCoreApplication.translate("MainWindow", "FFT", None))
        self.fraZoom.setTitle(QCoreApplication.translate("MainWindow", "Zoom", None))
        self.fraOsc.setTitle(
            QCoreApplication.translate("MainWindow", "Oscilloscope", None)
        )
        self.fraTHD.setTitle(QCoreApplication.translate("MainWindow", "THD", None))
        self.lblTHD.setText(QCoreApplication.translate("MainWindow", "THD", None))
        self.lblS0.setText(QCoreApplication.translate("MainWindow", "s0", None))
        self.lblS1.setText(QCoreApplication.translate("MainWindow", "s1", None))
        self.lblAverage.setText(
            QCoreApplication.translate("MainWindow", "Average over", None)
        )
        self.groupSignalGenerator.setTitle(
            QCoreApplication.translate("MainWindow", "Stimulus", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "Channel", None))
        self.cboSDG_ch.setItemText(
            0, QCoreApplication.translate("MainWindow", "1", None)
        )
        self.cboSDG_ch.setItemText(
            1, QCoreApplication.translate("MainWindow", "2", None)
        )

        self.checkUseSDG.setText(
            QCoreApplication.translate("MainWindow", "Use signal generator", None)
        )
        self.label_26.setText(
            QCoreApplication.translate("MainWindow", "Amplitude (V<sub>pp</sub>)", None)
        )
        self.tabSDGModulation.setTabText(
            self.tabSDGModulation.indexOf(self.tabCW),
            QCoreApplication.translate("MainWindow", "CW", None),
        )
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", "Carrier frequency", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "Modulation depth (%)", None)
        )
        self.label_21.setText(
            QCoreApplication.translate(
                "MainWindow", "Carrier amplitude (V<sub>pp</sub>)", None
            )
        )
        self.tabSDGModulation.setTabText(
            self.tabSDGModulation.indexOf(self.tabAM),
            QCoreApplication.translate("MainWindow", "AM", None),
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", "Carrier frequency", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", "Frequency deviation", None)
        )
        self.label_22.setText(
            QCoreApplication.translate(
                "MainWindow", "Carrier amplitude (V<sub>pp</sub>)", None
            )
        )
        self.tabSDGModulation.setTabText(
            self.tabSDGModulation.indexOf(self.tabFM),
            QCoreApplication.translate("MainWindow", "FM", None),
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Fundamental frequency", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Fundamental (Hz)", None)
        )
        self.tabSDGFixedSweep.setTabText(
            self.tabSDGFixedSweep.indexOf(self.tabFixed),
            QCoreApplication.translate("MainWindow", "Fixed", None),
        )
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", "Minimum frequency (Hz)", None)
        )
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", "Maximum frequency (Hz)", None)
        )
        self.label_23.setText(
            QCoreApplication.translate("MainWindow", "Frequency step (Hz)", None)
        )
        self.tabSDGFixedSweep.setTabText(
            self.tabSDGFixedSweep.indexOf(self.tabSweep),
            QCoreApplication.translate("MainWindow", "Sweep", None),
        )
        self.groupOSC.setTitle(
            QCoreApplication.translate("MainWindow", "Oscilloscope", None)
        )
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Channel", None))
        self.cboSDS_ch.setItemText(
            0, QCoreApplication.translate("MainWindow", "1", None)
        )
        self.cboSDS_ch.setItemText(
            1, QCoreApplication.translate("MainWindow", "2", None)
        )

        self.label_24.setText(
            QCoreApplication.translate("MainWindow", "Auto adjust V/div", None)
        )
        self.checkSDS_autoVertical.setText("")
        self.label_25.setText(
            QCoreApplication.translate("MainWindow", "Auto adjust timescale", None)
        )
        self.checkSDS_autoHorizontal.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Periods", None))
        self.groupTHD.setTitle(QCoreApplication.translate("MainWindow", "THD", None))
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "Harmonics", None)
        )
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow", "Floor (dB<sub>V<sub>rms</sub></sub>)", None
            )
        )
        self.label_9.setText(QCoreApplication.translate("MainWindow", "Average", None))
        self.groupFFTPlot.setTitle(
            QCoreApplication.translate("MainWindow", "FFT plot", None)
        )
        self.label_17.setText(
            QCoreApplication.translate(
                "MainWindow", "FFT min. Y (dB<sub>V<sub>rms</sub></sub>)", None
            )
        )
        self.label_18.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>FFT max. Y (dB<span style=" vertical-align:sub;">Vrms</span>)</p></body></html>',
                None,
            )
        )
        self.groupTHDPlot.setTitle(
            QCoreApplication.translate("MainWindow", "THD plot", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Plot amplitude", None)
        )
        self.edtTHDAmplitude.setText("")
        self.groupComm.setTitle(
            QCoreApplication.translate("MainWindow", "Communication", None)
        )
        self.btnStop.setText(QCoreApplication.translate("MainWindow", "Stop", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", "Start", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))
        self.menuSettings.setTitle(
            QCoreApplication.translate("MainWindow", "Edit", None)
        )

    # retranslateUi
