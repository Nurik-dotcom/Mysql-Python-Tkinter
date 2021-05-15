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
                id = int(input('Запишите id, в котором хотите исправть Название: '))
                time.sleep(1)
                print('Обработка id')
                time.sleep(2)
                imya = input('На какое название хотите заменить? :')
                sql = "UPDATE Film SET title = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "Изменения приняты")

                    
            elif choice == 2:
                print('lol')
                id = int(input('Запишите id, в котором хотите исправть место съемок: '))
                time.sleep(1)
                print('Обработка id')
                time.sleep(2)
                imya = input('На какое место хотите заменить? :')
                sql = "UPDATE Film SET country = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "Изменения приняты")
   
            elif choice == 3:
                print('lol')
                id = int(input('Запишите id, в котором хотите исправть год выпуска: '))
                time.sleep(1)
                print('Обработка id')
                time.sleep(2)
                imya = int(input('На какое год хотите заменить? :'))
                sql = "UPDATE Actor SET year = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "Изменения приняты")
            elif choice == 4:
                print('lol')
                id = int(input('Запишите id, в котором хотите исправть жанр: '))
                time.sleep(1)
                print('Обработка id')
                time.sleep(2)
                imya = input('На какое жанр хотите заменить? :')
                sql = "UPDATE Actor SET genre = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "Изменения приняты")
                
            elif choice == 5:
                print('lol')
                id = int(input('Запишите id, в котором хотите исправть длительность: '))
                time.sleep(1)
                print('Обработка id')
                time.sleep(2)
                imya = input('На какое длительность хотите заменить? :')
                sql = "UPDATE Actor SET duration_in_minute = %s WHERE id = %s"
                val = (imya, id)
                cursor.execute(sql, val)
                connection.commit()
                print(cursor.rowcount, "Изменения приняты")

            else:
                output = "Invalid selection"
        var = IntVar()
        Radiobutton(window, text="Название", variable=var, value=1, command=viewSelected).pack()
        Radiobutton(window, text="Место сьемок", variable=var, value=2, command=viewSelected).pack()
        Radiobutton(window, text="Год выпуска", variable=var, value=3, command=viewSelected).pack()
        Radiobutton(window, text="Жанр", variable=var, value=4, command=viewSelected).pack()
        Radiobutton(window, text="Длительность в минутах", variable=var, value=5, command=viewSelected).pack()
        window.mainloop()
