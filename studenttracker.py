import sys

import cv2
import face_recognition
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import dbconnect
import shutil
import os

path = ''
# imagelist = []
# classNames = []
# encodeList = []
# pathfolder = r'C:\Users\Peetamber\Desktop\FRAS underwork\ImagesAttendance'
# myList = os.listdir(pathfolder)
# print(myList)
# for cl in myList:
#     currentImage = cv2.imread(f'{pathfolder}/{cl}')
#     imagelist.append(currentImage)
#     classNames.append(os.path.splitext(cl)[0])

# for img in imagelist:
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     encode = face_recognition.face_encodings(img)[0]
#     encodeList.append(encode)

class StudentTracker(QMainWindow):
    def __init__(self):
        super(StudentTracker, self).__init__()
        loadUi("studenttracker.ui", self)
        self.btn_imageselect.clicked.connect(self.imageselect)
        self.btn_search.clicked.connect(self.findstudent)


    def imageselect(self):
        global path
        picture = QFileDialog.getOpenFileName(self, 'Open file',
                                              r'C:\\Users\\Peetamber\\Desktop\\', "Image files (*.jpg *.gif)")
        path = (picture[0])
        # print(path)

    def findstudent(self):
        imagelist = []
        classNames = []
        encodeList = []
        pathfolder = r'C:\Users\Peetamber\Desktop\FRAS underwork\ImagesAttendance'
        myList = os.listdir(pathfolder)
        print(myList)
        for cl in myList:
            currentImage = cv2.imread(f'{pathfolder}/{cl}')
            imagelist.append(currentImage)
            classNames.append(os.path.splitext(cl)[0])
        # print(imagelist)
        # print(len(imagelist))
        for img in imagelist:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        # print(encodeList)
        # print(len(encodeList))

        img = face_recognition.load_image_file(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeimg = face_recognition.face_encodings(img)[0]
        faceDist = face_recognition.face_distance(encodeList, encodeimg)
        matchIndex = np.argmin(faceDist)
        # print(matchIndex)
        name = myList[matchIndex].rsplit('.', 1)[0]
        id, rollno, dept = (dbconnect.findstudentfromname(name))
        self.label_name.setText(name)
        self.label_id.setText(id)
        self.label_rollno.setText(rollno)
        self.label_department.setText(dept)














# app = QApplication(sys.argv)
# newface = StudentTracker()
# newface.show()
# app.exec_()