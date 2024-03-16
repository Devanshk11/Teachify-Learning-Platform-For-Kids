import tkinter

import speech_recognition
import threading
import json
from difflib import get_close_matches
from tkinter import messagebox
from tkinter import *
import tkinter as tk
from tkinter import Frame
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3


root= tk.Tk()
root.geometry('1000x626+250+100')
root.title('Teachify - For Kids')
bgimage =PhotoImage(file='bg2.gif')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

####################################################3-6 years button#####################################################

def three_years():
    root.withdraw()
    three_years_window = tk.Toplevel()
    three_years_window.geometry('1000x626+250+100')
    three_years_window.title('Teachify - For Kids')
    frame1 = Frame(three_years_window, height=800, width=250, bg='black')
    frame1.place(x=0, y=0)
    frame2 = Frame(three_years_window, height=80, width=1550, bg='#6666ff')
    frame2.place(x=0, y=0)

    def back(window):
        window.destroy()
        root.update()
        root.deiconify()

    back_button = Button(three_years_window, text="Back", font=('Arial', 10, 'bold'), bd=5, relief=GROOVE,
                         command=lambda: back(three_years_window))
    back_button.place(x=930, y=580)


#CREATE COURSES BUTTON-----
    def new2():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Courses')
        frame3 = Frame(root, height=800, width=250, bg='black')
        frame3.place(x=0, y=0)
        frame4 = Frame(root, height=80, width=1550, bg='#6666ff')
        frame4.place(x=0, y=0)
    courses_button = Button(frame1, text='COURSES', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0,command=new2)
    courses_button.place(x=50, y=200)

#CREATE DICTIONARY BUTTON------
    def new3():
        siu = Toplevel(root)
        siu.geometry('1000x626+250+100')
        siu.title('Teachify - Dictionary')
        frame5 = Frame(siu, height=800, width=250, bg='black')
        frame5.place(x=0, y=0)
        frame6 = Frame(siu, height=80, width=1550, bg='#6666ff')
        frame6.place(x=0, y=0)

        def nextPage():
            import dict

    dict_button = Button(frame1, text='DICTIONARY', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new3)
    dict_button.place(x=35, y=300)



#CREATE AI-BOT BUTTON-----------
    def new4():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - AI')
        frame7 = Frame(root, height=800, width=250, bg='black')
        frame7.place(x=0, y=0)
        frame8 = Frame(root, height=80, width=1550, bg='#6666ff')
        frame8.place(x=0, y=0)
    ai_button = Button(frame1, text='AI-BOT', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new4)
    ai_button.place(x=60, y=400)



btn3_6years = Button(root, text='3-6 YEARS', font=('Arial', 20, 'bold'), bd=5, relief=GROOVE, command=three_years)
btn3_6years.place(x=410, y=100)

root.mainloop()
