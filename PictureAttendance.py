import os
import sys

import face_recognition
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import cv2

path = 'AttendanceImages'
imagelist = []
classNames = []
encodeList = []
myList = os.listdir(path)
target=''


class PictueAttendance(QDialog):
    def __init__(self):
        super(PictueAttendance, self).__init__()
        loadUi("PictureAttendance.ui", self)
        self.selectpic.clicked.connect(self.pictureopen)
        self.facedetect.clicked.connect(self.imageprocessing)

    def imageprocessing(self):
        # print(myList)
        for cl in myList:
            currentImage = cv2.imread(f'{path}/{cl}')
            imagelist.append(currentImage)
            classNames.append(os.path.splitext(cl)[0])

        for img in imagelist:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        print(encodeList)

    def pictureopen(self):
        global target
        picture = QFileDialog.getOpenFileName(self, 'Open file',
                                              r'C:\\Users\\Peetamber\\Desktop\\', "Image files (*.jpg *.gif)")
        target = picture[0]
        print(target)




app = QApplication(sys.argv)
mainwindow = PictueAttendance()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(650)
widget.setFixedHeight(600)
widget.show()
app.exec_()
