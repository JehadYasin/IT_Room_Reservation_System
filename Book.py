#Booking File
from tkinter import *
import sqlite3
import random
import string

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import tkinter as tk

from tkcalendar import Calendar, DateEntry

num_list = []
alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)
for i in range(10):
    num_list.append(str(i))


def submit(id, room, date, period):
    room = room.get()
    period = int(period.get())
  
    conn = sqlite3.connect('maindata.db')
    #select query
    cursor = conn.execute('SELECT * FROM Rooms WHERE Date="%s" AND Reservation_Period="%i" AND Room="%s"'%(date, period, room))
    if len(cursor.fetchall()) > 0:
        Label(Book, text=f"Error: {room} is already reserved at the time chosen",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=150,y=300)
    else:
        Label(Book, text=f"",bg="#1C2833",fg="white",font=("Arial",12,"bold"), width=300).place(x=150,y=300)
        Label(Book, text=f"{room} has been successfuly reserved, Period {period}, {date}",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=100,y=300)
        letter_part = random.choices(alphabet_list, k=3)
        num_part = random.choice(num_list)
        code = f"{letter_part[0]}{letter_part[1]}{letter_part[2]}{num_part}"
        cur = conn.cursor()
        command = 'INSERT INTO Rooms(Reservation_ID, Date, Reservation_Period, Teacher_ID, Room) VALUES(?,?,?,?,?);'
        data_tuple = (code, date, int(period), int(id), str(room))
        cur.execute(command, data_tuple)
        conn.commit()
        cur.close()

def example1():
    def print_sel():
        global chosen_date
        chosen_date = str(cal.selection_get())
        date_str = f"Date: {str(cal.selection_get())}"
        top.destroy()
        Label(Book, text=date_str,bg="#1C2833",fg="white",font=("Arial",8)).place(x=300,y=230)

    top = tk.Toplevel(Book)
    top.title("IT Room System - Calendar")

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()




def back(id, name, subject):
    Book.destroy()
    from App import run
    run(id, name, subject)

def Book_page(id, name, subject):
    global Book

    Book = Tk()
    #Setting title of screen
    Book.title(f"IT Room System - Book a Room")
    #setting height and width of screen
    Book.geometry("700x420")
    Book["bg"]="#1C2833"
    
    
    Room = StringVar()
    Period = StringVar()

    Room_opts = [
        "MacSuite1",
        "MacSuite2"
    ]

    Period_Opts = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
    ]

    Label(Book,width="400", height="2", text=f"IT Room System - Add a Booking", bg="#1693af",fg="white",font=("Arial",20,"bold")).pack()
    Label(Book,width="400", height="3", text=f"*Please do not modify the size of the window", bg="#1693af",fg="white",font=("Arial",10,"bold")).pack()
    Button(Book, text="Back", width=8, height=1, command=lambda: {back(id, name, subject)}, bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=5,y=2)
    Button(Book, text=f'''
Name: {name}
Subject: {subject}
    ''', width=15, height=2, bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=5,y=70)

    Label(Book, text="Room:",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=5,y=150)
    Room.set("<Choose a Room>")
    drop = OptionMenu( Book , Room , *Room_opts ).place(x=5,y=200)
    
    Label(Book, text="Date:",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=300,y=150)
    ttk.Button(Book, text='<Choose Date>', command=example1).place(x=300, y=200)
    
    Label(Book, text="Period:",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=560,y=150)
    Period.set("<Choose Period>")
    drop = OptionMenu( Book , Period , *Period_Opts).place(x=560,y=200)
    Button(Book, text="Submit", command=lambda:{submit(id, Room, chosen_date, Period)}, width=30, height=1, bg="#1693af",fg="white",font=("Arial",20,"bold")).place(x=100,y=350)
    
def run2(id, name, subject):
    Book_page(id, name, subject)

