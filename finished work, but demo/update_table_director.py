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
                id = int(input('Запишите id, в котором хотите исправть имя: '))
                time.sleep(1)
                print('Обработка id')
                time.sleep(2)
                imya = input('На какое имя хотите заменить? :')
                sql = "UPDATE Director SET Name = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "Изменения приняты")

                    
            elif choice == 2:
                print('lol')
                id = int(input('Запишите id, в котором хотите исправть фамилию: '))
                time.sleep(1)
                print('Обработка id')
                time.sleep(2)
                imya = input('На какое фамилию хотите заменить? :')
                sql = "UPDATE Director SET Surname = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "Изменения приняты")
   
            elif choice == 3:
                print('lol')
                id = int(input('Запишите id, в котором хотите исправть возраст: '))
                time.sleep(1)
                print('Обработка id')
                time.sleep(2)
                imya = int(input('На какое возраст хотите заменить? :'))
                sql = "UPDATE Director SET Age = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "Изменения приняты")
            elif choice == 4:
                print('lol')
                id = int(input('Запишите id, в котором хотите исправть страну: '))
                time.sleep(1)
                print('Обработка id')
                time.sleep(2)
                imya = input('На какое страну хотите заменить? :')
                sql = "UPDATE Director SET Country = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "Изменения приняты")

            else:
                output = "Invalid selection"
        var = IntVar()
        Radiobutton(window, text="Name", variable=var, value=1, command=viewSelected).pack()
        Radiobutton(window, text="Surname", variable=var, value=2, command=viewSelected).pack()
        Radiobutton(window, text="Age", variable=var, value=3, command=viewSelected).pack()
        Radiobutton(window, text="Country", variable=var, value=4, command=viewSelected).pack()
        window.mainloop()
