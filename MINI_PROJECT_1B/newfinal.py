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

root.mainloop()
