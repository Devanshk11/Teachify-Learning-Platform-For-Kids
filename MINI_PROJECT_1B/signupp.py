import tkinter as tk
from tkinter import Label, Entry, Button, PhotoImage
from tkinter import messagebox
from tkinter import END
import pymysql
from tkinter import Checkbutton
from tkinter import IntVar

def clear():
    emailEntry.delete(0,END)
    userEntry.delete(0,END)
    password_entry.delete(0,END)
    confirmpassword_entry.delete(0,END)
    check.set(0)



def connect_database():
    if emailEntry.get()=='' or userEntry.get()=='' or password_entry.get()=='' or confirmpassword_entry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    elif password_entry.get() !=confirmpassword_entry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms and Conditions')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Devanshk$1104')
            mycursor=con.cursor()
        except:
            messagebox.showerror('ERROR','Database Connectivity Issue, Please Try Again')
            return
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(100))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        # in the connect_database function, use the password_color variable to update the password field's background color before inserting it into the database
        query = 'insert into data(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query, (emailEntry.get(),userEntry.get(), password_entry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Registration Is Successful')
        clear()
        root.destroy()
        import loginn




def login_page():
   root.destroy()
   import loginn

# create the tkinter window
root = tk.Tk()
root.geometry('1060x595+250+100')
root.title('Teachify - For Kids')

# set the background image
bgimage = PhotoImage(file='icon_7.gif')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

# create the signup page widgets
signupLabel = Label(root, text="Create an account", font=("Arial", 18, 'bold'), fg='white', bg='black')

signupLabel.place(x=470, y=80)

emailLabel = Label(root, text="Email ID:", font=("Arial", 14), fg='white', bg='black')
emailLabel.place(x=400, y=150)
emailEntry = Entry(root, font=("Arial", 14), width=20)
emailEntry.place(x=550, y=150)

userLabel = Label(root, text="Username:", font=("Arial", 14), fg='white', bg='black')
userLabel.place(x=400, y=200)
userEntry = Entry(root, font=("Arial", 14), width=20)
userEntry.place(x=550, y=200)

passLabel = Label(root, text="Password:", font=("Arial", 14), fg='white', bg='black')
passLabel.place(x=400, y=250)
password_entry = tk.Entry(root, show='*',font=("Arial", 14), width=20)
password_entry.place(x=550, y=250)

confirmpassLabel = Label(root, text="Confirm Password:", font=("Arial", 14), fg='white', bg='black')
confirmpassLabel.place(x=400, y=300)
confirmpassword_entry = tk.Entry(root, show='*',font=("Arial", 14), width=20)
confirmpassword_entry.place(x=600, y=300)

check=IntVar()
termsandconditions = Checkbutton(root, text='I agree to the terms and conditions.', font=("Arial", 14), fg='black', bg='green',activebackground='green',activeforeground='white',cursor='hand2',variable=check)
termsandconditions.place(x=400, y=350)

signupButton = Button(root, text="Signup", font=("Arial", 14), fg='white', bg='blue', width=10,command=connect_database)
signupButton.place(x=400, y=400)

# link to the login page
loginLabel = Label(root, text="Already have an account?", font=("Arial", 10), fg='black', bg='white')
loginLabel.place(x=400, y=450)
loginButton = Button(root, text="Login", font=("Arial", 10), fg='white', bg='red', bd=0, cursor='hand2', width=10, activeforeground='blue', command=login_page, highlightthickness='0', highlightbackground=root.cget("bg"))
loginButton.place(x=570, y=450)

# start the tkinter event loop
root.mainloop()
