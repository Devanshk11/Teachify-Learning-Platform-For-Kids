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
from PIL import Image, ImageTk

import pyttsx3


root= tk.Tk()
root.geometry('1000x626+250+100')
root.title('Teachify - For Kids')
bgimage =PhotoImage(file='bg2.gif')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)


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



    # ----------------------------------------------COURSES BUTTON-----------------------------------------------------------
    def new2():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')
        frame2 = Frame(root, height=800, width=250, bg='black')
        frame2.place(x=0, y=0)
        frame3 = Frame(root, height=80, width=1550, bg='#6666ff')
        frame3.place(x=0, y=0)

    btn2 = Button(root, text='COURSES', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new2)
    btn2.place(x=50, y=200)

    # ----------------------------------------------DICTIONARY BUTTON----------------------------------------------------

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def new3():
        siu = Toplevel(root)
        siu.geometry('1000x626+250+100')
        siu.title('Teachify - Dictionary')
        # -------------------------------------ENTER WORD-----------------------------------------------
        lbl = Label(siu, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        lbl.place(x=450, y=70)
        lbl.pack()
        # -----------------------------------ENTER WORD TEXT-FIELD----------------------------------------
        enterwordentry = Entry(siu, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
        enterwordentry.place(x=320, y=80)

        # -------------------------------------SEARCH BUTTON------------------------------------------------
        def search():
            data = json.load(open('data.json'))
            word = enterwordentry.get()
            word = word.lower()
            if word in data:
                meaning = data[word]
                textarea.delete(1.0, END)
                for item in meaning:
                    textarea.insert(END, u'\u2022' + item + '\n\n')

            elif len(get_close_matches(word, data.keys())) > 0:
                close_match = get_close_matches(word, data.keys())[0]
                res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')

                if res == True:
                    enterwordentry.delete(0, END)
                    enterwordentry.insert(END, close_match)
                    meaning = data[close_match]
                    textarea.delete(1.0, END)
                    textarea.config(state=NORMAL)
                    textarea.delete(1.0, END)
                    for item in meaning:
                        textarea.insert(END, u'\u2022' + item + '\n\n')
                    root.lift()  # bring the root window to front
                    root.focus_force()  # focus the root window
                else:
                    textarea.delete(1.0, END)
                    messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
                    enterwordentry.delete(0, END)
                    root.lift()  # bring the root window to front
                    root.focus_force()  # focus the root window

            # Release the focus of the message box
            searchButton.focus_set()
            searchButton.grab_release()

        searchButton = Button(siu, text='SEARCH', bd=0, bg='white', activebackground='white', cursor='hand2',
                              command=search)
        searchButton.place(x=400, y=140)
        # ---------------------------------------MIC BUTTON--------------------------------------------------------

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        def wordaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(enterwordentry.get())
            engine.runAndWait()

        micButton = Button(siu, text='MIC BUTTON', bd=0, bg='white', activebackground='white',
                           cursor='hand2', command=wordaudio)
        micButton.place(x=500, y=140)
        # ----------------------------------------MEANING---------------------------------------------------------------
        meaninglabel = Label(siu, text='MEANING', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        meaninglabel.place(x=400, y=225)

        # -----------------------------------ENTER MEANING TEXT FIELD-----------------------------------
        textarea = Text(siu, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
        textarea.place(x=270, y=300)

        # ----------------------------------------MEANING WALA MIC BUTTON-----------------------------------------------------

        def meaningaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(textarea.get(1.0, END))
            engine.runAndWait()

        audioButton = Button(siu, text='AUDIO', bd=0, bg='white', activebackground='white',
                             cursor='hand2', command=meaningaudio)
        audioButton.place(x=400, y=555)

        # -----------------------------------------CLEAR SCREEN BUTTON--------------------------------------------
        # Define a function to clear the input
        def clear():
            textarea.config(state=NORMAL)
            enterwordentry.delete(0, END)
            textarea.delete(1.0, END)
            textarea.config(state=DISABLED)

        clearButton = Button(siu, text='CLEAR_TXT', bd=0, bg='white', activebackground='white', cursor='hand2'
                             , command=clear)
        clearButton.place(x=500, y=555)

        # --------------------------------------------EXIT BUTTON-----------------------------------

        # Define a function to close the window
        def close_window():
            siu.destroy()

        # Create a close button
        close_btn = tk.Button(siu, text="X", command=close_window, bg='red', fg='white', width=5, height=1)
        close_btn.place(x=950, y=10)

    btn3 = Button(root, text='DICTIONARY', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new3)
    btn3.place(x=35,y = 300)

    # ---------------------------------------------AI-BOT BUTTON----------------------------------------------------------
    def new4():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')

    btn = Button(root, text='AI-BOT', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new4)
    btn.place(x=60, y=400)


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
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def new3():
        siu = Toplevel(root)
        siu.geometry('1000x626+250+100')
        siu.title('Teachify - Dictionary')
        frame5 = Frame(siu, height=800, width=250, bg='black')
        frame5.place(x=0, y=0)
        frame4 = Frame(siu, height=80, width=1550, bg='#6666ff')
        frame4.place(x=0, y=0)

        # -------------------------------------ENTER WORD-----------------------------------------------
        lbl = Label(siu, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        lbl.place(x=474, y=80)

        # -----------------------------------ENTER WORD TEXT-FIELD----------------------------------------
        enterwordentry = Entry(siu, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
        enterwordentry.place(x=446, y=140)

        # -------------------------------------SEARCH BUTTON------------------------------------------------
        def search():
            data = json.load(open('data.json'))
            word = enterwordentry.get()
            word = word.lower()
            if word in data:
                meaning = data[word]
                textarea.delete(1.0, END)
                for item in meaning:
                    textarea.insert(END, u'\u2022' + item + '\n\n')

            elif len(get_close_matches(word, data.keys())) > 0:

                close_match = get_close_matches(word, data.keys())[0]

                res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')
                if res == True:
                    enterwordentry.delete(0, END)
                    enterwordentry.insert(END, close_match)
                    meaning = data[close_match]
                    textarea.delete(1.0, END)
                    textarea.config(state=NORMAL)
                    textarea.delete(1.0, END)
                    for item in meaning:
                        textarea.insert(END, u'\u2022' + item + '\n\n')

                else:

                    textarea.delete(1.0, END)

                    messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
                    enterwordentry.delete(0, END)



        searchButton = Button(siu, text='SEARCH', bd=0, bg='white', activebackground='white', cursor='hand2',
                              command=search)
        searchButton.place(x=540, y=215)

        # ------------------------------------MIC BUTTON--------------------------------------------------------

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        def wordaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(enterwordentry.get())
            engine.runAndWait()

        micButton = Button(siu, text='MIC BUTTON', bd=0, bg='white', activebackground='white',
                           cursor='hand2', command=wordaudio)
        micButton.place(x=600, y=215)
        # ----------------------------------------MEANING---------------------------------------------------------------
        meaninglabel = Label(siu, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        meaninglabel.place(x=510, y=260)

        # -----------------------------------ENTER MEANING TEXT FIELD-----------------------------------
        textarea = Text(siu, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
        textarea.place(x=390, y=320)

        # ----------------------------------------MEANING WALA MIC BUTTON-----------------------------------------------------

        def meaningaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(textarea.get(1.0, END))
            engine.runAndWait()

        audioButton = Button(siu, text='audioimage', bd=0, bg='white', activebackground='white',
                             cursor='hand2', command=meaningaudio)
        audioButton.place(x=510, y=585)

        # -----------------------------------------CLEAR SCREEN BUTTON--------------------------------------------

        def clear():
            textarea.config(state=NORMAL)
            enterwordentry.delete(0, END)
            textarea.delete(1.0, END)
            textarea.config(state=DISABLED)

        clearButton = Button(siu, text='clearimage', bd=0, bg='white', activebackground='white', cursor='hand2'
                             , command=clear)
        clearButton.place(x=600, y=585)

        # --------------------------------------------EXIT BUTTON-----------------------------------

        def iexit():
            res = messagebox.askyesno('Confirm', 'Do you want to exit?')
            if res == True:
                siu.destroy()
            else:
                pass

        exitButton = Button(siu, text='exitimage', bd=0, bg='white', activebackground='white', cursor='hand2',
                            command=iexit)
        exitButton.place(x=680, y=585)

        def enter_function(event):
            searchButton.invoke()

        siu.bind('<Return>', enter_function)
        siu.mainloop()

    btn2 = Button(root, text='DICTIONARY', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new3)
    btn2.place(x=35, y=400)

    # ---------------------------------------------AI-BOT BUTTON----------------------------------------------------------
    def new4():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')

    btn = Button(root, text='AI-BOT', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new4)
    btn.place(x=60, y=500)


root.geometry('1000x626+250+100')
root.title('Teachify - For Kids')

btn1 = Button(root, text='3-6 YEARS', font=('Arial', 20, 'bold'), bd=5, relief=GROOVE, command=dsk)
btn1.place(x=410, y=100)

btn2 = Button(root, text='7-11 YEARS', font=('Arial', 20, 'bold'), bd=5, relief=GROOVE, command=dsk1)
btn2.place(x=400, y=300)

root.mainloop()
#-------------------------------------------------DICTIONARY BUTTON----------------------------------------------------
siu = tkinter.Toplevel()
bgimage = PhotoImage(file='bg_icon.gif')

bgLabel = Label(siu, image=bgimage)
bgLabel.place(x=0, y=0)
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def new3():
        siu = Toplevel(root)
        siu.geometry('1000x626+250+100')
        siu.title('Teachify - Dictionary')
        frame5 = Frame(siu, height=800, width=250, bg='black')
        frame5.place(x=0, y=0)
        frame4 = Frame(siu, height=80, width=1550, bg='#6666ff')
        frame4.place(x=0, y=0)

        # -------------------------------------ENTER WORD-----------------------------------------------
        lbl = Label(siu, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        lbl.place(x=474, y=80)

        # -----------------------------------ENTER WORD TEXT-FIELD----------------------------------------
        enterwordentry = Entry(siu, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
        enterwordentry.place(x=446, y=140)

        # -------------------------------------SEARCH BUTTON------------------------------------------------
        def search():
            data = json.load(open('data.json'))
            word = enterwordentry.get()
            word = word.lower()
            if word in data:
                meaning = data[word]
                textarea.delete(1.0, END)
                for item in meaning:
                    textarea.insert(END, u'\u2022' + item + '\n\n')

            elif len(get_close_matches(word, data.keys())) > 0:

                close_match = get_close_matches(word, data.keys())[0]

                res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')
                if res == True:
                    enterwordentry.delete(0, END)
                    enterwordentry.insert(END, close_match)
                    meaning = data[close_match]
                    textarea.delete(1.0, END)
                    textarea.config(state=NORMAL)
                    textarea.delete(1.0, END)
                    for item in meaning:
                        textarea.insert(END, u'\u2022' + item + '\n\n')

                else:

                    textarea.delete(1.0, END)

                    messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
                    enterwordentry.delete(0, END)

        searchButton = Button(siu, text='SEARCH', bd=0, bg='white', activebackground='white', cursor='hand2',
                              command=search)
        searchButton.place(x=540, y=215)

        # ------------------------------------MIC BUTTON--------------------------------------------------------

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        def wordaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(enterwordentry.get())
            engine.runAndWait()

        micButton = Button(siu, text='MIC BUTTON', bd=0, bg='white', activebackground='white',
                           cursor='hand2', command=wordaudio)
        micButton.place(x=600, y=215)
        # ----------------------------------------MEANING---------------------------------------------------------------
        meaninglabel = Label(siu, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        meaninglabel.place(x=510, y=260)

        # -----------------------------------ENTER MEANING TEXT FIELD-----------------------------------
        textarea = Text(siu, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
        textarea.place(x=390, y=320)

        # ----------------------------------------MEANING WALA MIC BUTTON-----------------------------------------------------

        def meaningaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(textarea.get(1.0, END))
            engine.runAndWait()

        audioButton = Button(siu, text='audioimage', bd=0, bg='white', activebackground='white',
                             cursor='hand2', command=meaningaudio)
        audioButton.place(x=510, y=585)

        # -----------------------------------------CLEAR SCREEN BUTTON--------------------------------------------

        def clear():
            textarea.config(state=NORMAL)
            enterwordentry.delete(0, END)
            textarea.delete(1.0, END)
            textarea.config(state=DISABLED)

        clearButton = Button(siu, text='clearimage', bd=0, bg='white', activebackground='white', cursor='hand2'
                             , command=clear)
        clearButton.place(x=600, y=585)

        # --------------------------------------------EXIT BUTTON-----------------------------------

        def iexit():
            res = messagebox.askyesno('Confirm', 'Do you want to exit?')
            if res == True:
                siu.destroy()
            else:
                pass

        exitButton = Button(siu, text='exitimage', bd=0, bg='white', activebackground='white', cursor='hand2',
                            command=iexit)
        exitButton.place(x=680, y=585)

        def enter_function(event):
            searchButton.invoke()

        siu.bind('<Return>', enter_function)
        siu.mainloop()

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
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def new3():
        siu = Toplevel(root)
        siu.geometry('1000x626+250+100')
        siu.title('Teachify - Dictionary')
        frame5 = Frame(siu, height=800, width=250, bg='black')
        frame5.place(x=0, y=0)
        frame4 = Frame(siu, height=80, width=1550, bg='#6666ff')
        frame4.place(x=0, y=0)

        # -------------------------------------ENTER WORD-----------------------------------------------
        lbl = Label(siu, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        lbl.place(x=474, y=80)

        # -----------------------------------ENTER WORD TEXT-FIELD----------------------------------------
        enterwordentry = Entry(siu, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
        enterwordentry.place(x=446, y=140)

        # -------------------------------------SEARCH BUTTON------------------------------------------------
        def search():
            data = json.load(open('data.json'))
            word = enterwordentry.get()
            word = word.lower()
            if word in data:
                meaning = data[word]
                textarea.delete(1.0, END)
                for item in meaning:
                    textarea.insert(END, u'\u2022' + item + '\n\n')

            elif len(get_close_matches(word, data.keys())) > 0:

                close_match = get_close_matches(word, data.keys())[0]

                res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')
                if res == True:
                    enterwordentry.delete(0, END)
                    enterwordentry.insert(END, close_match)
                    meaning = data[close_match]
                    textarea.delete(1.0, END)
                    textarea.config(state=NORMAL)
                    textarea.delete(1.0, END)
                    for item in meaning:
                        textarea.insert(END, u'\u2022' + item + '\n\n')

                else:

                    textarea.delete(1.0, END)

                    messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
                    enterwordentry.delete(0, END)

        searchButton = Button(siu, text='SEARCH', bd=0, bg='white', activebackground='white', cursor='hand2',
                              command=search)
        searchButton.place(x=540, y=215)

        # ------------------------------------MIC BUTTON--------------------------------------------------------

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        def wordaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(enterwordentry.get())
            engine.runAndWait()

        micButton = Button(siu, text='MIC BUTTON', bd=0, bg='white', activebackground='white',
                           cursor='hand2', command=wordaudio)
        micButton.place(x=600, y=215)
        # ----------------------------------------MEANING---------------------------------------------------------------
        meaninglabel = Label(siu, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        meaninglabel.place(x=510, y=260)

        # -----------------------------------ENTER MEANING TEXT FIELD-----------------------------------
        textarea = Text(siu, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
        textarea.place(x=390, y=320)

        # ----------------------------------------MEANING WALA MIC BUTTON-----------------------------------------------------

        def meaningaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(textarea.get(1.0, END))
            engine.runAndWait()

        audioButton = Button(siu, text='audioimage', bd=0, bg='white', activebackground='white',
                             cursor='hand2', command=meaningaudio)
        audioButton.place(x=510, y=585)

        # -----------------------------------------CLEAR SCREEN BUTTON--------------------------------------------

        def clear():
            textarea.config(state=NORMAL)
            enterwordentry.delete(0, END)
            textarea.delete(1.0, END)
            textarea.config(state=DISABLED)

        clearButton = Button(siu, text='clearimage', bd=0, bg='white', activebackground='white', cursor='hand2'
                             , command=clear)
        clearButton.place(x=600, y=585)

        # --------------------------------------------EXIT BUTTON-----------------------------------

        def iexit():
            res = messagebox.askyesno('Confirm', 'Do you want to exit?')
            if res == True:
                siu.destroy()
            else:
                pass

        exitButton = Button(siu, text='exitimage', bd=0, bg='white', activebackground='white', cursor='hand2',
                            command=iexit)
        exitButton.place(x=680, y=585)

        def enter_function(event):
            searchButton.invoke()

        siu.bind('<Return>', enter_function)
        siu.mainloop()

    btn2 = Button(root, text='DICTIONARY', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new3)
    btn2.place(x=35, y=400)

    # ---------------------------------------------AI-BOT BUTTON----------------------------------------------------------
    def new4():
        root = tk.Tk()
        root.geometry('1000x626+250+100')
        root.title('Teachify - Home')

    btn = Button(root, text='AI-BOT', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new4)
    btn.place(x=60, y=500)


root.geometry('1000x626+250+100')
root.title('Teachify - For Kids')
bgimage = PhotoImage(file='bg2.gif')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)
btn1 = Button(root, text='3-6 YEARS', font=('Arial', 20, 'bold'), bd=5, relief=GROOVE, command=dsk)
btn1.place(x=410, y=100)

btn2 = Button(root, text='7-11 YEARS', font=('Arial', 20, 'bold'), bd=5, relief=GROOVE, command=dsk1)
btn2.place(x=400, y=300)

root.mainloop()

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
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def new3():
        siu=Toplevel(root)
        siu.geometry('1000x626+250+100')
        siu.title('Teachify - Dictionary')
        frame5 = Frame(siu, height=800, width=250, bg='black')
        frame5.place(x=0, y=0)
        frame4 = Frame(siu, height=80, width=1550, bg='#6666ff')
        frame4.place(x=0, y=0)

        # -------------------------------------ENTER WORD-----------------------------------------------
        lbl = Label(siu, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        lbl.place(x=474, y=80)

        # -----------------------------------ENTER WORD TEXT-FIELD----------------------------------------
        enterwordentry = Entry(siu, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
        enterwordentry.place(x=446, y=140)

        # -------------------------------------SEARCH BUTTON------------------------------------------------
        def search():
            data = json.load(open('data.json'))
            word = enterwordentry.get()
            word = word.lower()
            if word in data:
                meaning = data[word]
                textarea.delete(1.0, END)
                for item in meaning:
                    textarea.insert(END, u'\u2022' + item + '\n\n')

            elif len(get_close_matches(word, data.keys())) > 0:

                close_match = get_close_matches(word, data.keys())[0]

                res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')
                if res == True:
                    enterwordentry.delete(0, END)
                    enterwordentry.insert(END, close_match)
                    meaning = data[close_match]
                    textarea.delete(1.0, END)
                    textarea.config(state=NORMAL)
                    textarea.delete(1.0, END)
                    for item in meaning:
                        textarea.insert(END, u'\u2022' + item + '\n\n')

                else:

                    textarea.delete(1.0, END)

                    messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
                    enterwordentry.delete(0, END)

        searchButton = Button(siu, text='SEARCH', bd=0, bg='white', activebackground='white', cursor='hand2',
                              command=search)
        searchButton.place(x=540, y=215)

        # ------------------------------------MIC BUTTON--------------------------------------------------------

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        def wordaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(enterwordentry.get())
            engine.runAndWait()

        micButton = Button(siu, text='MIC BUTTON', bd=0, bg='white', activebackground='white',
                           cursor='hand2', command=wordaudio)
        micButton.place(x=600, y=215)
        # ----------------------------------------MEANING---------------------------------------------------------------
        meaninglabel = Label(siu, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='#ccccff')
        meaninglabel.place(x=510, y=260)

        # -----------------------------------ENTER MEANING TEXT FIELD-----------------------------------
        textarea = Text(siu, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
        textarea.place(x=390, y=320)

        # ----------------------------------------MEANING WALA MIC BUTTON-----------------------------------------------------

        def meaningaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(textarea.get(1.0, END))
            engine.runAndWait()

        audioButton = Button(siu, text='audioimage', bd=0, bg='white', activebackground='white',
                             cursor='hand2', command=meaningaudio)
        audioButton.place(x=510, y=585)

        # -----------------------------------------CLEAR SCREEN BUTTON--------------------------------------------

        def clear():
            textarea.config(state=NORMAL)
            enterwordentry.delete(0, END)
            textarea.delete(1.0, END)
            textarea.config(state=DISABLED)

        clearButton = Button(siu, text='clearimage', bd=0, bg='white', activebackground='white', cursor='hand2'
                             , command=clear)
        clearButton.place(x=600, y=585)

        # --------------------------------------------EXIT BUTTON-----------------------------------

        def iexit():
            res = messagebox.askyesno('Confirm', 'Do you want to exit?')
            if res == True:
                siu.destroy()
            else:
                pass

        exitButton = Button(siu, text='exitimage', bd=0, bg='white', activebackground='white', cursor='hand2',
                            command=iexit)
        exitButton.place(x=680, y=585)

        def enter_function(event):
            searchButton.invoke()

        siu.bind('<Return>', enter_function)
        siu.mainloop()



    btn2 = Button(root, text='DICTIONARY', font=('Arial', 20, 'bold'), bg='black', fg='white', bd=0, command=new3)
    btn2.place(x=35, y=400)







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