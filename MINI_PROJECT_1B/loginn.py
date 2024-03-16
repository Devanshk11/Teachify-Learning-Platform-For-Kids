import tkinter as tk
from tkinter import Label, Entry, Button, PhotoImage
from tkinter import messagebox
from tkinter import END
import pymysql
from tkinter import Checkbutton
import os
def hide():
    openeye.config(file='closeeye.png')
    password_entry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    password_entry.config(show='')
    eyeButton.config(command=hide)

import pymysql
def login_user():
    if userEntry.get()=='' or password_entry.get()=='':
        messagebox.showerror('Error','All fields are required')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Devanshk$1104')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','connection is not established try again')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query,(userEntry.get(),password_entry.get()))
        row = mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
            os.system("python TEACHIFY.py")






def signup_page():
    root.destroy()
    import signupp

# create the tkinter window
root = tk.Tk()
root.geometry('1060x595+250+100')
root.title('Teachify - For Kids')

# set the background image
bgimage = PhotoImage(file='icon_7.gif')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

# create the login page widgets
loginLabel = Label(root, text="Login", font=("Arial", 18, 'bold'), fg='white', bg='black')
loginLabel.place(x=470, y=80)

userLabel = Label(root, text="Username:", font=("Arial", 14), fg='white', bg='black')
userLabel.place(x=400, y=200)
userEntry = Entry(root, font=("Arial", 14), width=20)
userEntry.place(x=550, y=200)

passLabel = Label(root, text="Password:", font=("Arial", 14), fg='white', bg='black')
passLabel.place(x=400, y=250)

password_entry = tk.Entry(root, show='*',font=("Arial", 14), width=20)
password_entry.place(x=550, y=250)



loginButton = Button(root, text="Login", font=("Arial", 14), fg='white', bg='blue', width=10,command=login_user)
loginButton.place(x=400, y=300)


openeye=PhotoImage(file='openeye.png')
eyeButton=Button(root,image=openeye,bd=0,activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=760,y=250)

#dont have an account
noaccountButton = Button(root, text="Don't have an account?", font=("Arial", 9,'bold'),bd=0,cursor='hand2',command=signup_page)
noaccountButton.place(x=400, y=385)

# start the tkinter event loop
root.mainloop()
