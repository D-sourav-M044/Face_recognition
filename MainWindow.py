from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QStatusBar
from PyQt5.uic import loadUi
#from myproj import myfun
from liveness_demo import runlive
from encode_faces import runencode

class MainWindow(QMainWindow):
    def __init__(self):
        WINDOW_TITLE = "Face_rocognition_security_system"
        GUI_UI_LOCATION = "Fpro.ui"

        super(MainWindow, self).__init__()
        loadUi(GUI_UI_LOCATION, self)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("click any of them")

        self.setWindowTitle(WINDOW_TITLE)
        # ^ Same ^
        
        self.putton1.clicked.connect(self.asd1)
        self.putton2.clicked.connect(self.asd2)

    def asd1(self):
        #self.mylabel.setText('hejdkslfj')
        #myfun('hello', 'test', 'bye')
        runlive("liveness.model","le.pickle","face_detector")
    def asd2(self):
        runencode("face_dataset","hog","encodings.pickle")    
        
