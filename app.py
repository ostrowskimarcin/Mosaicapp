from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from mosaic import Mosaic
from PIL import Image



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
        #self.action_save_img = QtWidgets.QAction(MainWindow)
        #self.action_save_img.setObjectName("action_save_img")
        self.menuPlik.addAction(self.action_load_path)
        self.menuPlik.addAction(self.action_load_img)
        #self.menuPlik.addAction(self.action_save_img)
        self.menubar.addAction(self.menuPlik.menuAction())

        self.pushButton_start.clicked.connect(self.start)
        self.action_load_img.triggered.connect(self.load_image)
        self.action_load_path.triggered.connect(self.load_path)

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
        #self.action_save_img.setText(_translate("MainWindow", "Zapisz obraz"))

    def start(self):
        self.msc = Mosaic()
        self.msc.im = self.img_file
        self.msc.path = self.path
        self.msc.grid = self.get_grid()

        self.progressBar.show()

        self.new_image = self.msc.make_mosaic(self.progressBar)
        self.mozaika.setPixmap(QtGui.QPixmap('mosaic.jpg'))


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





