import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import dbconnect
import shutil
import os

path = ''
oldfilename = ''


class NewFace(QMainWindow):
    def __init__(self):
        super(NewFace, self).__init__()
        loadUi("newface.ui", self)
        self.add_button.clicked.connect(self.pressed)
        self.picbutton.clicked.connect(self.pictureopen)

    def pictureopen(self):
        global path, oldfilename
        picture = QFileDialog.getOpenFileName(self, 'Open file',
                                              r'C:\\Users\\Peetamber\\Desktop\\', "Image files (*.jpg *.gif)")
        path = (picture[0])
        print(path)
        oldfilename = path.rsplit('/', 1)[-1]  # This gives the filename with the extension from the path

    def pressed(self):
        print('Adding new face')
        name = (self.name.text())
        studentid = (self.studentid.text())
        department = self.dept.text()
        rollno = int(self.rollno.text())
        dbconnect.insertBLOB(studentid, name, rollno, department, path)
        path2 = path.rsplit('/', 1)[0] + '/FRAS underwork/ImagesAttendance' + '/' + oldfilename
        target = path.rsplit('/', 1)[0] + '/FRAS underwork/ImagesAttendance' + '/' + name + '.jpg'
        print(target)
        print(path2)
        shutil.copy(path, r'C:\Users\Peetamber\Desktop\FRAS underwork\ImagesAttendance')
        os.rename(path2, target)
        self.hide()


# app = QApplication(sys.argv)
# newface = NewFace()
# newface.show()
# app.exec_()
