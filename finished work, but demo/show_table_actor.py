import pymysql.cursors
from tkinter import *
import tkinter as tk
import os
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                              cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:

        sql = "SELECT Id as 'ID', Name as 'Имя', Surname as 'Фамилия', Age as 'Возраст', Country as 'Страна' from Actor"
        #sql = "SELECT * from Actor"
        cursor.execute(sql)
        result = cursor.fetchall()
        root=Tk()
        canvas = Canvas(root, width=750, height=300, bg="blue", highlightthickness=0)
        canvas.pack()
        text1=Text(root,height=200,width=50,font='Arial 14',wrap=WORD)
        text1.insert(1.0, result)
        text1.place(x=10, y=10)
        root.mainloop()



