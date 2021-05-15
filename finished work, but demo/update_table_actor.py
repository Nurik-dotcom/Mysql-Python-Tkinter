import pymysql.cursors
from tkinter import *
import tkinter as tk
import time
import os
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                              cursorclass=pymysql.cursors.DictCursor)




with connection:
        
    with connection.cursor() as cursor:
        window = Tk()
        window.title('Изменения данных')
        window.geometry('500x300')
        def viewSelected():
            choice  = var.get()
            if choice == 1:
                print('lol')
                id = int(input('Write an actor"s ID, where you want to change : '))
                time.sleep(1)
                print('processing')
                time.sleep(2)
                imya = input('Enter your own name? :')
                sql = "UPDATE Actor SET Name = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print("Changed")
                    
            elif choice == 2:
                print('lol')
                id = int(input('Write an actor"s ID, where you want to change : '))
                time.sleep(1)
                print('processing')
                time.sleep(2)
                imya = input('Enter your own surname? :')
                sql = "UPDATE Actor SET Surname = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print("Changed")
   
            elif choice == 3:
                print('lol')
                id = int(input('Write an actor"s ID, where you want to change : '))
                time.sleep(1)
                print('processing')
                time.sleep(2)
                imya = input('Enter your own age? :')
                sql = "UPDATE Actor SET Age = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print("Changed")
            elif choice == 4:
                print('lol')
                id = int(input('Write an actor"s ID, where you want to change : '))
                time.sleep(1)
                print('processing')
                time.sleep(2)
                imya = input('Enter your own country? :')
                sql = "UPDATE Actor SET Country = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print("Changed")

            else:
                output = "Invalid selection"
        var = IntVar()
        Radiobutton(window, text="Name", variable=var, value=1, command=viewSelected).pack()
        Radiobutton(window, text="Surname", variable=var, value=2, command=viewSelected).pack()
        Radiobutton(window, text="Age", variable=var, value=3, command=viewSelected).pack()
        Radiobutton(window, text="Country", variable=var, value=4, command=viewSelected).pack()
        window.mainloop()
