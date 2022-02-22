import mysql.connector
from mysql.connector import Error


def con():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='PC_DATA',
                                             user='bot',
                                             password='secbot123')

        if connection.is_connected():
            print("Connected")

        else:
            print("failed")

    except Error as e:
        print(e)


con()
