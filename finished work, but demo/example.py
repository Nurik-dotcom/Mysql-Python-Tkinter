from tkinter import *
import tkinter as ttk

root = Tk()
root.title("Tk dropdown example")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)
from tkinter import messagebox
import pymysql.cursors
from tkinter import *
import tkinter as tk
import os
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                              cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        actor_count = 'select count(name) from Actor'
        cursor.execute(actor_count)
        lol = cursor.fetchall()
        result = lol[0]['count(name)']
        choices = []
        for i in range(result):
            choices.append(i)
    
tkvar.set('Id ') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Выберите Id актрера").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

name = StringVar()
surname = StringVar()
age = IntVar()
country = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")
age_label = Label(text="Введите возраст:")
country_label = Label(text="Введите страну:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
age_label.grid(row=2, column=0, sticky="w")
country_label.grid(row=3, column=0, sticky="w")
 
name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
age_entry = Entry(textvariable=age)
country_entry = Entry(textvariable=country)
 
name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)
age_entry.grid(row=2,column=1, padx=5, pady=5)
country_entry.grid(row=3,column=1, padx=5, pady=5)
 
message_button = Button(text="Click Me", command=insert_into)
message_button.grid(row=5,column=1, padx=5, pady=5, sticky="e")
 
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()
