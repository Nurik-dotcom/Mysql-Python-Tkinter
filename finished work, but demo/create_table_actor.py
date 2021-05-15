from tkinter import *
import pymysql.cursors
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                               cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        root = Tk()
        cursor.execute('create table Actor(Id INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(30) NOT NULL,Surname VARCHAR(20) NOT NULL,Age INT DEFAULT 0,Country varchar(40));')
        connection.commit()
        text1=Text(root,height=100,width=100,font='Arial 14',wrap=WORD)
        text1.insert(1.0, 'Table created')
        text1.place(x=10, y=10)
        root.mainloop()
