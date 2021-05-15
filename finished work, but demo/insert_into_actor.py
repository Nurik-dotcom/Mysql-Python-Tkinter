from tkinter import *
 
import pymysql.cursors
from tkinter import *
import tkinter as tk
import os
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                               cursorclass=pymysql.cursors.DictCursor)

from tkinter import messagebox
def insert_into(): 
    with connection:  
        with connection.cursor() as cursor:
            name1 = name.get()
            surname1 = surname.get()
            age1 = age.get()
            country1 = country.get()
            sql = """insert into Actor(Name, Surname, Age, Country) value (%s, %s, %s, %s);"""
            var = (name1, surname1, age1, country1)
            cursor.execute(sql, var)
            connection.commit()
            messagebox.showinfo("GUI Python", 'ADDED')
 
root = Tk()
root.title("GUI на Python")
 
name = StringVar()
surname = StringVar()
age = IntVar()
country = StringVar()

name_label = Label(text="Enter name:")
surname_label = Label(text="Enter surname:")
age_label = Label(text="Enter age:")
country_label = Label(text="Enter country:")

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
 
root.mainloop()
