import pymysql.cursors

from tkinter import *
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                               cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        root = Tk()
        cursor.execute('DROP TABLE Film')
        connection.commit()
        text1=Text(root,height=85,width=85,font='Arial 14',wrap=WORD)
        text1.insert(1.0, 'Table deleted')
        text1.place(x=10, y=10)
        root.mainloop()
