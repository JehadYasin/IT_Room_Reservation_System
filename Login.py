from tkinter import *

import sqlite3


def next_page(id, name, subject):
    login_screen.destroy()
    from App import run
    run(id, name, subject)

#defining login function
def login():
    #getting form data
    tid=Teacher_ID.get()
    pwd=password.get()
    #applying empty validation
    if tid=='' or pwd=='':
        message.set("Error: Fill the empty field(s)")
    else:
      #open database
      conn = sqlite3.connect('maindata.db')
      #select query
      cursor = conn.execute('SELECT * from Login where Teacher_ID="%s" and Password="%s"'%(tid,pwd))
      #fetch data 
    if cursor.fetchone():
        name = conn.execute('SELECT Name from Login WHERE Teacher_ID = "%s"'%(tid)).fetchone()
        subject = conn.execute('SELECT Subject from Login WHERE Teacher_ID = "%s"'%(tid)).fetchone()
        for i in name:
            name = i
        for i in subject:
            subject = i
        login_screen.after(3000, next_page(tid, name, subject))
    else:
        message.set("Error: Wrong ID or Password!")

#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("IT Room System - LOGIN")
    #setting height and width of screen
    login_screen.geometry("830x250")
    login_screen["bg"]="#1C2833"
    #declaring variable
    global  message
    global Teacher_ID
    global password
    
    Teacher_ID = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login formx
    Label(login_screen,width="400", text="Login Form - IT Room System", bg="#17afc3",fg="white",font=("Arial",16,"bold")).pack()
    #Username Label
    Label(login_screen, text="Teacher ID* ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=Teacher_ID,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=42)
    #Password Label
    Label(login_screen, text="Password* ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=70,y=120)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, command=login, bg="#17afc3",fg="white",font=("Arial",12,"bold")).place(x=125,y=170)
    img=PhotoImage(file='logo.png')
    Label(login_screen,image=img).place(x = 350, y = 40 )
    
    login_screen.mainloop()

#calling function Loginform
Loginform()






