import pymysql.cursors
from tkinter import *
import tkinter as tk
import time
import os
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                              cursorclass=pymysql.cursors.DictCursor)

def for_actor():
    os.system('C:/Users/Нурдаулет/OneDrive/"Рабочий стол"/mysql.session/director.py')#location
def for_director():
    os.system('C:/Users/Нурдаулет/OneDrive/"Рабочий стол"/mysql.session/actor.py')
def for_films():
    os.system('C:/Users/Нурдаулет/OneDrive/"Рабочий стол"/mysql.session/films.py')


tk = Tk()
tk.title("MYSQL")
canvas = Canvas(tk, width=600, height=600, bg="#ebb14d", highlightthickness=0)
canvas.pack()
b1 = Button(tk, text = "Working with ACTOR list", command = for_director)
b1.place(x=200, y=200)
b2 = Button(tk, text = "Working with DIRECTOR list", command = for_actor)
b2.place(x=200, y=300)
b3 = Button(tk, text = "Working with FILM list", command = for_films)
b3.place(x=200, y=400)
