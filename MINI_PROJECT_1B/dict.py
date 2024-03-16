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


#====================================================================================================================#
                                              #DICTIONARY CODE#
#====================================================================================================================#

dict = Tk()
dict.geometry('1280x914+100+30')
dict.title('Teachify - Dictionary')

bgimage =PhotoImage(file='bg_icon.gif')
bgLabel = Label(dict, image=bgimage)
bgLabel.place(x=0, y=0)

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def wordaudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(enterwordentry.get())
    engine.runAndWait()

def  meaningaudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()

def clear():
    textarea.config(state=NORMAL)
    enterwordentry.delete(0, END)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)

def iexit():
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if res == True:
        dict.destroy()
    else:
        pass


def search():
    data = json.load(open('data.json'))
    word = enterwordentry.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END, u'\u2022' + item + '\n\n')

    elif len(get_close_matches(word, data.keys())) > 0:

        close_match = get_close_matches(word, data.keys())[0]

        res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')
        if res == True:
            enterwordentry.delete(0,END)
            enterwordentry.insert(END,close_match)
            meaning = data[close_match]
            textarea.delete(1.0, END)
            textarea.config(state=NORMAL)
            textarea.delete(1.0,END)
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')

        else:

            textarea.delete(1.0, END)


            messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
            enterwordentry.delete(0, END)









#-------------------------------------ENTER WORD-----------------------------------------------
enterwordLabel = Label(dict, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='white')
enterwordLabel.place(x=530, y=20)

#-----------------------------------ENTER WORD TEXT-FIELD----------------------------------------
enterwordentry = Entry(dict, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
enterwordentry.place(x=510, y=80)

#-------------------------------------SEARCH BUTTON------------------------------------------------
searchimage = PhotoImage(file='search.gif')
searchButton = Button(dict,image=searchimage, bd=0, bg='white', activebackground='white', cursor='hand2',command=search)
searchButton.place(x=620, y=150)

#------------------------------------MIC BUTTON--------------------------------------------------------
micimage = PhotoImage(file='mic.gif')
micButton = Button(dict, image=micimage, bd=0, bg='white', activebackground='white',
                   cursor='hand2',command=wordaudio)
micButton.place(x=710, y=153)


#----------------------------------------MEANING---------------------------------------------------------------
meaninglabel = Label(dict, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='white')
meaninglabel.place(x=580, y=240)

#-----------------------------------ENTER MEANING TEXT FIELD-----------------------------------
textarea = Text(dict, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
textarea.place(x=460, y=300)

#----------------------------------------MEANING WALA MIC BUTTON-----------------------------------------------------
audioimage = PhotoImage(file='microphone.gif')
audioButton = Button(dict, image=audioimage, bd=0, bg='white', activebackground='white',
                     cursor='hand2',command=meaningaudio)
audioButton.place(x=530, y=555)

#-----------------------------------------CLEAR SCREEN BUTTON--------------------------------------------
clearimage = PhotoImage(file='clear.gif')
clearButton = Button(dict, image=clearimage, bd=0, bg='white', activebackground='white', cursor='hand2'
                    ,command=clear)
clearButton.place(x=660, y=555)

#--------------------------------------------EXIT BUTTON-----------------------------------
exitimage = PhotoImage(file='exit.gif')
exitButton = Button(dict, image=exitimage, bd=0, bg='white', activebackground='white', cursor='hand2',command=iexit)
exitButton.place(x=790, y=555)



def enter_function(event):
    searchButton.invoke()

dict.bind('<Return>',enter_function)
dict.mainloop()