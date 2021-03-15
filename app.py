from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QWidget, QHBoxLayout, QComboBox, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from mosaic import Mosaic
from PIL import Image

import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(660, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox_grid = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_grid.setGeometry(QtCore.QRect(540, 330, 86, 25))
        self.comboBox_grid.setObjectName("comboBox_grid")
        self.comboBox_grid.addItem("")
        self.comboBox_grid.addItem("")
        self.comboBox_grid.addItem("")
        self.comboBox_grid.addItem("")
        self.comboBox_grid.addItem("")
        self.comboBox_grid.addItem("")
        self.comboBox_grid.addItem("")
        self.comboBox_grid.hide()

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(540, 410, 89, 25))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.hide()

        self.label_grid = QtWidgets.QLabel(self.centralwidget)
        self.label_grid.setGeometry(QtCore.QRect(480, 330, 51, 21))
        self.label_grid.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_grid.setObjectName("label_grid")
        self.label_grid.hide()

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 410, 361, 23))

        self.progressBar.setObjectName("progressBar")
        self.progressBar.setProperty("value", 0)
        self.progressBar.hide()

        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(20, 20, 300, 300))
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setObjectName("image")

        self.mozaika = QtWidgets.QLabel(self.centralwidget)
        self.mozaika.setGeometry(QtCore.QRect(340, 20, 300, 300))
        self.mozaika.setText("")
        self.mozaika.setScaledContents(True)
        self.mozaika.setObjectName("mozaika")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 22))
        self.menubar.setObjectName("menubar")
        self.menuPlik = QtWidgets.QMenu(self.menubar)
        self.menuPlik.setObjectName("menuPlik")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.action_load_path = QtWidgets.QAction(MainWindow)
        self.action_load_path.setObjectName("action_load_path")
        self.action_load_img = QtWidgets.QAction(MainWindow)
        self.action_load_img.setObjectName("action_load_img")
        self.action_save_img = QtWidgets.QAction(MainWindow)
        self.action_save_img.setObjectName("action_save_img")
        self.action_save_img.setEnabled(False)

        self.menuPlik.addAction(self.action_load_path)
        self.menuPlik.addAction(self.action_load_img)
        self.menuPlik.addAction(self.action_save_img)
        self.menubar.addAction(self.menuPlik.menuAction())

        self.pushButton_start.clicked.connect(self.start)
        self.action_load_img.triggered.connect(self.load_image)
        self.action_load_path.triggered.connect(self.load_path)
        self.action_save_img.triggered.connect(self.save_image)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mosaicapp"))
        self.comboBox_grid.setItemText(0, _translate("MainWindow", "8x8"))
        self.comboBox_grid.setItemText(1, _translate("MainWindow", "20x20"))
        self.comboBox_grid.setItemText(2, _translate("MainWindow", "40x40"))
        self.comboBox_grid.setItemText(3, _translate("MainWindow", "80x80"))
        self.comboBox_grid.setItemText(4, _translate("MainWindow", "100x100"))
        self.comboBox_grid.setItemText(5, _translate("MainWindow", "200x200"))
        self.comboBox_grid.setItemText(6, _translate("MainWindow", "400x400"))

        self.pushButton_start.setText(_translate("MainWindow", "Start"))

        self.label_grid.setText(_translate("MainWindow", "Grid:"))

        self.menuPlik.setTitle(_translate("MainWindow", "File"))

        self.action_load_path.setText(_translate("MainWindow", "Load gallery path"))
        self.action_load_img.setText(_translate("MainWindow", "Load image"))
        self.action_save_img.setText(_translate("MainWindow", "Save image"))

    def start(self):
        self.msc = Mosaic()
        self.msc.im = self.img_file
        self.msc.path = self.path
        self.msc.grid = self.get_grid()

        self.progressBar.show()

        self.new_image = self.msc.make_mosaic(self.progressBar)
        self.mozaika.setPixmap(QtGui.QPixmap('temporary_img.jpg'))
        os.remove('temporary_img.jpg')

        self.action_save_img.setEnabled(True)

    def load_image(self):
        self.img = QFileDialog.getOpenFileName()
        self.img_file = Image.open(self.img[0])

        self.image.setPixmap(QtGui.QPixmap(self.img[0]))

        self.pushButton_start.show()
        self.label_grid.show()
        self.comboBox_grid.show()

    def load_path(self):
        self.path = QFileDialog.getExistingDirectory()

    def get_grid(self) -> int:
        self.grid = int(self.comboBox_grid.currentText().split('x')[0])
        return self.grid

    def save_image(self):
        self.w = Widget()
        self.w.get_mosaic_img(self.new_image)


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.img = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Save as')
        self.setFixedSize(400, 100)

        self.textbox = QLineEdit(self)
        self.textbox.move(90, 20)
        self.textbox.resize(130, 22)

        self.label1 = QLabel('Name:', self)
        self.label1.move(20, 22)

        self.label2 = QLabel('Size:', self)
        self.label2.move(20, 70)

        self.combo = QComboBox(self)
        self.combo.move(90, 65)
        self.combo.addItem('')
        self.combo.addItem('')
        self.combo.addItem('')
        self.combo.addItem('')
        self.combo.addItem('')
        self.combo.addItem('')
        self.combo.setItemText(0, '720 x 480 px')
        self.combo.setItemText(1, '1280 x 720 px')
        self.combo.setItemText(2, '1920 x 1080 px')
        self.combo.setItemText(3, 'A5 (2551 x 1819 px)')
        self.combo.setItemText(4, 'A4 (3579 x 2551 px)')
        self.combo.setItemText(5, 'A3 (5031 x 3579 px)')

        self.button = QPushButton('Save', self)
        self.button.move(300, 20)
        self.button.clicked.connect(self.save)

        self.show()

    def get_size(self) -> tuple:
        id = self.combo.currentIndex()
        if id == 0:
            size = (720, 480)
        elif id == 1:
            size = (1280, 720)
        elif id == 2:
            size = (1920, 1080)
        elif id == 3:
            size = (2551, 1819)
        elif id == 4:
            size = (3579, 2551)
        elif id == 5:
            size = (5031, 3579)
        return size

    def get_mosaic_img(self, mosaic):
        self.img = mosaic

    def save(self):
        name_to_save = self.textbox.text() + '.jpg'
        size_to_save = self.get_size()
        self.img = self.img.resize(size_to_save)
        self.img.save(name_to_save, 'JPEG')
        self.close()
