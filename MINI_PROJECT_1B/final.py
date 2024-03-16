from tkinter import *
import tkinter as tk
from tkinter import Frame
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
import os
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


root = tk.Tk()

####################################################3-6 years button#####################################################
def dsk():
    root = tk.Tk()
    root.geometry('1000x626+250+100')
    root.title('Teachify - For Kids')

    # ----------------------------------------------CREATE LEFT BLACK FRAME-------------------------------------------------

    black_frame = tk.Frame(root, bg='black')

    black_frame.pack(side=tk.LEFT)
    black_frame.pack_propagate(False)
    black_frame.configure(width=250, height=800)

    root.tk_setPalette('#ccccff')
    main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)

    # -------------------------------------------------CREATE TOP BLUE LABEL-------------------------------------------------

    blue_frame = Frame(root, height=80, width=1550, bg='#6666ff')
    blue_frame.place(x=0, y=0)

    # -----------------------------------------------HOME BUTTON-----------------------------------------------------------


    def new1():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')

    btn1 = Button(root, text='HOME', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new1)
    btn1.place(x=70, y=200)

    blue_frame = Frame(root, height=80, width=1550, bg='#6666ff')
    blue_frame.place(x=0, y=0)

    # ----------------------------------------------COURSES BUTTON-----------------------------------------------------------
    def new2():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')
        frame2 = Frame(root, height=80, width=1550, bg='#6666ff')
        frame2.place(x=0, y=0)

    btn2 = Button(root, text='COURSES', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new2)
    btn2.place(x=45, y=300)

    # ----------------------------------------------DICTIONARY BUTTON----------------------------------------------------
    def new3():
        root = tk.Toplevel()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Dictionary')



    btn3 = Button(root, text='DICTIONARY', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new3)
    btn3.place(x=35, y=400)


    # ---------------------------------------------AI-BOT BUTTON----------------------------------------------------------
    def new4():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')

    btn = Button(root, text='AI-BOT', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new4)
    btn.place(x=60, y=500)



 ########################################################7-11 years old##################################################
def dsk1():
    root = tk.Tk()
    root.geometry('1000x626+250+100')
    root.title('Teachify - For Kids')
    # ----------------------------------------------CREATE LEFT BLACK FRAME-------------------------------------------------

    black_frame = tk.Frame(root, bg='black')

    black_frame.pack(side=tk.LEFT)
    black_frame.pack_propagate(False)
    black_frame.configure(width=250, height=800)

    root.tk_setPalette('#ccccff')
    main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)

    # -------------------------------------------------CREATE TOP BLUE LABEL-------------------------------------------------

    blue_frame = Frame(root, height=80, width=1550, bg='#6666ff')
    blue_frame.place(x=0, y=0)

    # -----------------------------------------------HOME BUTTON-----------------------------------------------------------

    def new1():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')
    btn1 = Button(root, text='HOME', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new1)
    btn1.place(x=70, y=200)

    blue_frame = Frame(root, height=80, width=1550, bg='#6666ff')
    blue_frame.place(x=0, y=0)

    # ----------------------------------------------COURSES BUTTON-----------------------------------------------------------
    def new2():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')
        frame2 = Frame(root, height=80, width=1550, bg='#6666ff')
        frame2.place(x=0, y=0)

    btn2 = Button(root, text='COURSES', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new2)
    btn2.place(x=45, y=300)

    # ----------------------------------------------DICTIONARY BUTTON----------------------------------------------------
    def new3():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Dictionary')
        frame3 = Frame(root, height=80, width=1550, bg='#6666ff')
        frame3.place(x=0, y=0)

    btn3 = Button(root, text='DICTIONARY', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new3)
    btn3.place(x=35, y=400)



    # ---------------------------------------------AI-BOT BUTTON----------------------------------------------------------
    def new4():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')

    btn = Button(root, text='AI-BOT', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new4)
    btn.place(x=60, y=500)
root.geometry('1000x626+250+100')
root.title('Teachify - For Kids')
bgimage =PhotoImage(file='bg2.gif')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)
btn1 = Button(root, text='3-6 YEARS', font=('Arial', 20, 'bold'),bd=5,relief=GROOVE,command=dsk)
btn1.place(x=410, y=100)

btn2 = Button(root, text='7-11 YEARS', font=('Arial', 20, 'bold'),bd=5,relief=GROOVE,command=dsk1)
btn2.place(x=400, y=300)




root.mainloop()