import mysql.connector


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def insertBLOB(id, name, rollno, dept, photo):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='frasdb',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO student(id, name, rollno, dept, photo) VALUES (%s,%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (id, name, rollno, dept, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def deleteface(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='frasdb',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        sql_fetch_blob_query = """DELETE from student where id = %s"""
        cursor.execute(sql_fetch_blob_query, (id,))
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to delete data from MySQL table {} ".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def givenamefromid(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='frasdb',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from student where id = %s"""
        cursor.execute(sql_fetch_blob_query, (id,))
        record = cursor.fetchall()
        for row in record:
            return row[1]


    except mysql.connector.Error as error:
        print("Failed to delete data from MySQL table {} ".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")


def findstudentfromname(name):
    global dept, rollno, id
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='frasdb',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from student where name = %s"""

        cursor.execute(sql_fetch_blob_query, (name,))
        record = cursor.fetchall()
        for row in record:
            id = str(row[0])
            rollno = str(row[2])
            dept = str(row[3])
            # name is already detected using the file name
        # list = (id, rollno, dept)
        return id, rollno, dept

    except mysql.connector.Error as error:
        print("Failed ".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def readBLOB(id, photo):
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='frasdb',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from student where id = %s"""

        cursor.execute(sql_fetch_blob_query, (id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image = row[2]
            print("Storing employee image on disk \n")
            write_file(image, photo)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# readBLOB(1, r"C:\Users\Peetamber\Desktop\QuickBits\FRAS\FRAS-master\Cache")  # whenever changing the file location make
# changes here also. Cache folder
# name = 'Peets'
# studentid = 100
# path = 'C:/Users/Peetamber/Desktop/test.jpg'
# insertBLOB(studentid, name, path)

# insertBLOB(2, "Elon Musk", r"C:\Users\Peetamber\PycharmProjects\FaceRecognitionProject\AttendanceImages\Elon Musk.jpg")
