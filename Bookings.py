from re import I
from tkinter import *
import sqlite3
import time

def mark_cancel(id, name, subject, input):
    output = tuple(input.get())
    res_id = f'{output[2]}{output[3]}{output[4]}{output[5]}'
    conn = sqlite3.connect('maindata.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Rooms WHERE Reservation_ID="%s"'%(res_id))
    conn.commit()

    Book_screen.after(500, Book_screen.destroy())
    run1(id, name, subject)

def back(id, name, subject):
    Book_screen.destroy()
    from App import run
    run(id, name, subject)


#Bookings Page File
def Bookings(id, name, subject):
    global Book_screen
    Book_screen = Tk()
    #Setting title of screen
    Book_screen.title(f"IT Room System - Bookings: {name}")
    #setting height and width of screen
    Book_screen.geometry("800x420")
    Book_screen["bg"]="#1C2833"

    conn = sqlite3.connect('maindata.db')
    cursor = conn.execute('SELECT Reservation_ID,Date,Reservation_Period,Room FROM Rooms WHERE Teacher_ID="%s"'%(id))
    options = cursor.fetchall()
    conn.close()

    #Creating layout of login form
    Label(Book_screen,width="400", height="2", text=f"IT Room System - {name}'s Bookings", bg="#1693af",fg="white",font=("Arial",20,"bold")).pack()
    Label(Book_screen,width="400", height="3", text=f"*Please do not modify the size of the window", bg="#1693af",fg="white",font=("Arial",10,"bold")).pack()
    Button(Book_screen, text="Back", width=8, height=1, command=lambda: {back(id, name, subject)}, bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=5,y=2)
    Button(Book_screen, text=f'''
Name: {name}
Subject: {subject}
    ''', width=15, height=2, bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=5,y=70)
    img=PhotoImage(file='logo2.png')
    Label(Book_screen,image=img).place(x = 700, y = 10)
    Label(Book_screen, text=f"Choose a Booking:", bg="#1693af",fg="white",font=("Arial",15,"bold")).place(x = 40, y = 170)
    clicked = StringVar()
    clicked.set('<Choose Booking>')
    drop = OptionMenu( Book_screen , clicked , *options )
    drop.place(x = 40, y = 220)

    Button(Book_screen, text="Mark Booking as Complete", width=30, height=2, command=lambda: {mark_cancel(id, name, subject, clicked)}, bg="#1693af",fg="white",font=("Arial",20,"bold")).place(x=250,y=170)
    Button(Book_screen, text="Cancel a Booking", width=30, height=2, command=lambda: {mark_cancel(id, name, subject, clicked)}, bg="#1693af",fg="white",font=("Arial",20,"bold")).place(x=250,y=300)
    Book_screen.mainloop()

#recieves two arguments, to customise the hompage according to the teacher
def run1(id, name, subject):
    Bookings(id, name, subject)
