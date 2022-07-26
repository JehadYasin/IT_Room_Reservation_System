#This file is for the hompage screen
import time
from tkinter import *


def add_book(id, name, subject):
    App_screen.destroy()
    from Book import run2
    run2(id, name, subject)

def bookings(id, name, subject):
    App_screen.destroy()
    from Bookings import run1
    run1(id, name, subject)


def help():
    pass
    #to be implemented

#logout function: returns to login page
def logout():
    App_screen.destroy()
    import Login

#MAIN Function
def App(id, name, subject):

    global App_screen

    App_screen = Tk()
    #Setting title of screen
    App_screen.title(f"IT Room System - Homepage: {name}")
    #setting height and width of screen
    App_screen.geometry("700x420")
    App_screen["bg"]="#1C2833"
    #declaring variable

    #Creating layout of login form
    Label(App_screen,width="400", height="2", text=f"IT Room System - Homepage", bg="#1693af",fg="white",font=("Arial",20,"bold")).pack()
    Label(App_screen,width="400", height="3", text=f"*Please do not modify the size of the window", bg="#1693af",fg="white",font=("Arial",10,"bold")).pack()
    Button(App_screen, text="Logout", width=8, height=1, command=logout, bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=5,y=2)
    Button(App_screen, text=f'''
Name: {name}
Subject: {subject}
    ''', width=15, height=2, bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=5,y=70)
    img=PhotoImage(file='logo2.png')
    Label(App_screen,image=img).place(x = 600, y = 10)
    Button(App_screen, text="My Bookings/Reservations", width=30, height=1, command=lambda: 
    {bookings(id, name, subject)}, bg="#1693af",fg="white",font=("Arial",20,"bold")).place(x=100,y=170)
    Button(App_screen, text="Make a Booking", width=30, height=1, command=lambda: {add_book(id, name, subject)}, bg="#1693af",fg="white",font=("Arial",20,"bold")).place(x=100,y=250)
    Button(App_screen, text="Help (Send An Email)", width=30, height=1, command=help, bg="#1693af",fg="white",font=("Arial",20,"bold")).place(x=100,y=330)

    App_screen.mainloop()

#recieves two arguments, to customise the hompage according to the teacher
def run(id, name, subject):
    App(id, name, subject)
