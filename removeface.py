import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import dbconnect
import shutil
import os


class RemoveFace(QMainWindow):
    def __init__(self):
        super(RemoveFace, self).__init__()
        loadUi("removeface.ui", self)
        self.remove_button.clicked.connect(self.removeface)

    def removeface(self):
        studentid = self.studentid.text()
        name = dbconnect.givenamefromid(studentid)
        # print(type(name))
        # print(f'name = {name}')
        # name = 'peets'
        path = 'C:/Users/Peetamber/Desktop/FRAS underwork/ImagesAttendance/'
        target = path + name + '.jpg'
        print(target)
        if os.path.exists(target):
            os.remove(target)
            print('Face removed')
        else:
            print("The file does not exist")
        dbconnect.deleteface(studentid)
        self.hide()




# app = QApplication(sys.argv)
# newface = RemoveFace()
# newface.show()
# app.exec_()
