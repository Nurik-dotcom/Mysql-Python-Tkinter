from tkinter import *
import pymysql.cursors
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                               cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        root = Tk()
        cursor.execute('create table Film(Id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(30) NOT NULL,genre VARCHAR(20) NOT NULL,year INT DEFAULT 0,Country varchar(40), duration_in_min int, director_id int, FOREIGN KEY (Director_id) REFERENCES Director(Id) ON DELETE CASCADE);')
        connection.commit()
        canvas = Canvas(root, width=100, height=100, bg="blue", highlightthickness=0)
        canvas.pack()
        text1=Text(root,height=85,width=85,font='Arial 14',wrap=WORD)
        text1.insert(1.0, 'Table created')
        text1.place(x=10, y=10)
        root.mainloop()
