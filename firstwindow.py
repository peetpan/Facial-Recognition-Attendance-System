import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

from mainwindow import Ui_Dialog
from newface import NewFace
from removeface import RemoveFace
from studenttracker import StudentTracker


class FirstWindow(QDialog):
    def __init__(self):
        super(FirstWindow, self).__init__()
        loadUi("firstwindow.ui", self)
        self.btn_newface.clicked.connect(self.opennewface)
        self.btn_removeface.clicked.connect(self.removeface)
        self.btn_cico.clicked.connect(self.checkinout)
        self.btn_stutrack.clicked.connect(self.studentracker)



    def opennewface(self):
        # firstwindow.hide()
        self._new_window = NewFace()
        self._new_window.show()

    def removeface(self):
        # firstwindow.hide()
        self._new_window = RemoveFace()
        self._new_window.show()

    def checkinout(self):
        # firstwindow.hide()
        self._new_window = Ui_Dialog()
        self._new_window.show()

    def studentracker(self):
        # firstwindow.hide()
        self._new_window = StudentTracker()
        self._new_window.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    firstwindow = FirstWindow()
    firstwindow.show()
    app.exec_()
