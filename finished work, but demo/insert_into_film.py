from tkinter import *
import pymysql.cursors
from tkinter import messagebox
connection = pymysql.connect(host='localhost', user='root', password='Atleticomadrid2002',
                              database='session',
                              cursorclass=pymysql.cursors.DictCursor)
# Эта часть не работает *********************************************************************************
# def insert_into():
#     with connection:
#         with connection.cursor() as cursor:
#             title1 = title.get()
#             country1 = country.get()
#             year1 = year.get()
#             duration1 = duration.get()
#             clicked2 = clicked.get()
#             clicked3 = clicked1.get()
#             sql = """insert into Film(title, genre, year, country, duration_in_min, director_id) value (%s, %s, %s, %s, %s,(select * from Director where Id = %s));"""
#             var = (title1, clicked2, year1, country1, duration1, clicked3)
#             cursor.execute(sql, var)
#             cursor.close()

            
            
# root = Tk()
# title = StringVar()
# country = StringVar()
# year = IntVar()
# duration = IntVar()

# title_label = Label(text="Введите имя:")
# country_label = Label(text="Введите фамилию:")
# year_label = Label(text="Введите год выпуска:")
# duration_label = Label(text="Длитеьность фильма в минутах:")
 
# title_label.grid(row=0, column=0, sticky="w")
# country_label.grid(row=1, column=0, sticky="w")
# year_label.grid(row=2, column=0, sticky="w")
# duration_label.grid(row=3, column=0, sticky="w")

# title_entry = Entry(textvariable=title)
# country_entry = Entry(textvariable=country)
# year_entry = Entry(textvariable=year)
# duration_entry = Entry(textvariable=duration)
 
# title_entry.grid(row=0,column=1, padx=5, pady=5)
# country_entry.grid(row=1,column=1, padx=5, pady=5)
# year_entry.grid(row=2,column=1, padx=5, pady=5)
# duration_entry.grid(row=3,column=1, padx=5, pady=5)
# options = [
#     "Ужасы",
#     "Экшн",
#     "Драма",
#     "Комедия",
#     "Фантастика",
#     "Мистика",
#     "Меха"
# ]
  
# clicked = StringVar()
  
# clicked.set( "Жанр" )

# drop = OptionMenu( root , clicked , *options )
# drop.grid(row=4, column=0, padx=5, pady=5)
# with connection:
#     with connection.cursor() as cursor:
#         actor_count = 'select count(name) from Director'
#         cursor.execute(actor_count)
#         lol = cursor.fetchall()
#         result = lol[0]['count(name)']
#         genre = []
#         for i in range(result):
#             genre.append(i)
# clicked1 = StringVar()
# clicked1.set( "ID режжисера" )
# drop1 = OptionMenu( root , clicked1 , *genre )
# drop1.grid(row=4, column=2, padx=5, pady=5)
# Adlet = Button(text="Добавить значение", command=insert_into)
# Adlet.grid(row=5, column=0, padx=5, pady=5, sticky="e")
# root.mainloop()
# *********************************************************************************
with connection:  
    with connection.cursor() as cursor:
        window = Tk()
        window.title('Data change')
        window.geometry('500x300')
        title1 = input('Name of film: ')
        country1 = input('Country: ')
        year1 = int(input('Year: '))
        duration1 = int(input('Duration: '))
        clicked2 = input('Genre: ')
        clicked3 = int(input('Director ID: '))

        sql = """insert into Film(director_id, title, genre, year, country, duration_in_min) values((select Name from Director where Id = %s),%s, %s, %s, %s, %s);"""
        var = (clicked3, title1, clicked2, year1, country1, duration1)
        cursor.execute(sql, var)
        connection.commit()
