import pymysql.cursors
from tkinter import *
import tkinter as tk
import time
import os
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                              cursorclass=pymysql.cursors.DictCursor)

def create_table():
    os.system('C:/Users/Нурдаулет/OneDrive/"Рабочий стол"/mysql.session/create_table_film.py')
def show_table():
    os.system('C:/Users/Нурдаулет/OneDrive/"Рабочий стол"/mysql.session/show_table_film.py')
def update_table():
    os.system('C:/Users/Нурдаулет/OneDrive/"Рабочий стол"/mysql.session/update_table_film.py')
def insert_into():
    os.system('C:/Users/Нурдаулет/OneDrive/"Рабочий стол"/mysql.session/insert_into_film.py')
def delete_table():
    os.system('C:/Users/Нурдаулет/OneDrive/"Рабочий стол"/mysql.session/delete_table_film.py')

tk = Tk()
tk.title("FOR FILMS")
canvas = Canvas(tk, width=800, height=800, bg="#ff9666", highlightthickness=0)
canvas.pack()
b1 = Button(tk, text = "Show Table", command = show_table)
b1.place(x=300, y=200)
b2 = Button(tk, text = "Insert values", command = insert_into)
b2.place(x=300, y=300)
b3 = Button(tk, text = "Update values", command = update_table)
b3.place(x=300, y=400)
b4 = Button(tk, text = "Delete table", command = delete_table)
b4.place(x=300, y=500)
b5 = Button(tk, text = "Create table", command = create_table)
b5.place(x=300, y=600)
tk.mainloop()
