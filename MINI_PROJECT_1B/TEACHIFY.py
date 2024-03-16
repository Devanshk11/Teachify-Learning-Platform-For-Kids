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
from tkinter import ttk
import googletrans
import wikipedia
import random
import pyperclip
import pygame

engine = pyttsx3.init()

root = tk.Tk()
root.geometry('1060x595+250+100')
root.title('Teachify - For Kids')
bgimage = PhotoImage(file='icon_7.gif')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)


def three_six_page():
    three_six = tk.Toplevel()
    three_six.geometry('1060x595+250+100')
    three_six.title('Teachify - For Kids')
    # Create a frame to hold the image
    image_frame = Frame(three_six, bg='white', width=500, height=500)
    image_frame.pack(side=LEFT, padx=0, pady=0)

    # Load the image
    bg_image = Image.open("bg3.png")
    bg_image = bg_image.resize((1050, 595))
    photo = ImageTk.PhotoImage(bg_image)

    # Create a label to display the image
    image_label = Label(image_frame, image=photo, bg='white')
    image_label.image = photo
    image_label.pack()

    def back():
        three_six.destroy()

    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
    back_button = Button(three_six, image=back_button_image, bd=0, bg='#efd2aa', command=back,
                         height=50, width=50)
    back_button.image = back_button_image
    back_button.place(x=275, y=400)

    ##------------------------------------------------------CREATE COURSE BUTTON-----------------------------------------------------------##

    def maths():
        maths = tk.Toplevel()
        maths.geometry('1060x595+250+100')
        maths.title('Teachify - For Kids')

        # Create a frame to hold the image
        image_frame = Frame(maths, bg='white', width=500, height=500)
        image_frame.pack(side=LEFT, padx=0, pady=0)

        # Load the  image
        bg_image = Image.open("new_bg.png")
        bg_image = bg_image.resize((1050, 595))
        photo = ImageTk.PhotoImage(bg_image)

        # Create a label to display the image
        image_label = Label(image_frame, image=photo, bg='white')
        image_label.image = photo
        image_label.pack()

        mathslabel = Label(maths, text='MATHS', font=('castellar', 29, 'bold'), fg='red3', bg='#ffffff')
        mathslabel.place(x=320, y=110)

        def back():
            maths.destroy()

        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
        back_button = Button(maths, image=back_button_image, bd=0, command=back, bg='#ffffff',
                             height=74, width=76)
        back_button.image = back_button_image
        back_button.place(x=90, y=380)

        def tables_pg():
            tables = tk.Toplevel()
            tables.geometry('1060x595+250+100')
            tables.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(tables, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            tb_label = Label(tables, text='MATHS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            tb_label.place(x=420, y=35)

            def table_one_pg():
                tab_lab1 = Label(tables, text="1   x   1   =   1      ", font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                tab_lab1.place(x=120, y=170)

                tab_lab2 = Label(tables, text="1   x   2   =   2      ", font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                tab_lab2.place(x=120, y=240)

                tab_lab3 = Label(tables, text="1   x   3   =   3      ", font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                tab_lab3.place(x=120, y=310)

                tab_lab4 = Label(tables, text="1   x   4   =   4      ", font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                tab_lab4.place(x=120, y=380)

                tab_lab5 = Label(tables, text="1   x   5   =   5      ", font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                tab_lab5.place(x=120, y=450)

                tab_lab6 = Label(tables, text="1   x   6   =   6    ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab6.place(x=620, y=170)

                tab_lab7 = Label(tables, text="1   x   7   =   7    ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab7.place(x=620, y=240)

                tab_lab8 = Label(tables, text="1   x   8   =   8    ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab8.place(x=620, y=310)

                tab_lab9 = Label(tables, text="1   x   9   =   9    ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab9.place(x=620, y=380)

                tab_lab10 = Label(tables, text="1   x   10   = 10  ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab10.place(x=620, y=450)

            table_one_btn = Button(tables, text='1', font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                   command=table_one_pg)
            table_one_btn.place(x=500, y=510)

            def table_two_pg():
                tab_lab11 = Label(tables, text="2   x   1   =   2      ", font=('castellar', 29, 'bold'),
                                  bg='#fff7ea')
                tab_lab11.place(x=120, y=170)

                tab_lab12 = Label(tables, text="2   x   2   =   4      ", font=('castellar', 29, 'bold'),
                                  bg='#fff7ea')
                tab_lab12.place(x=120, y=240)

                tab_lab13 = Label(tables, text="2   x   3   =   6      ", font=('castellar', 29, 'bold'),
                                  bg='#fff7ea')
                tab_lab13.place(x=120, y=310)

                tab_lab14 = Label(tables, text="2   x   4   =   8      ", font=('castellar', 29, 'bold'),
                                  bg='#fff7ea')
                tab_lab14.place(x=120, y=380)

                tab_lab15 = Label(tables, text="2   x   5   =   10      ", font=('castellar', 29, 'bold'),
                                  bg='#fff7ea')
                tab_lab15.place(x=120, y=450)

                tab_lab16 = Label(tables, text="2   x   6   =   12  ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab16.place(x=620, y=170)

                tab_lab17 = Label(tables, text="2   x   7   =   14  ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab17.place(x=620, y=240)

                tab_lab18 = Label(tables, text="2   x   8   =   16  ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab18.place(x=620, y=310)

                tab_lab19 = Label(tables, text="2   x   9   =   18  ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab19.place(x=620, y=380)

                tab_lab20 = Label(tables, text="2   x   10   =  20 ", font=('castellar', 29, 'bold'), bg='#fff7ea')
                tab_lab20.place(x=620, y=450)

            table_two_btn = Button(tables, text='2', font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                   command=table_two_pg)
            table_two_btn.place(x=530, y=510)

        table_btn = Button(maths, text="TABLES", command=tables_pg, font=('Arial', 20, 'bold'), bd=1, bg='#ffffff')
        table_btn.place(x=345, y=180)

        # ---------------------------------------ADDITION---------------------------------------------------------------------
        def additn():
            opr = tk.Toplevel()
            opr.geometry('1060x595+250+100')
            opr.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(opr, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()
            op_label = Label(opr, text='MATHS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            op_label.place(x=420, y=35)
            op_label = Label(opr, text='MATHS-Addition', font=('castellar', 29, 'bold'), fg='red3',
                             bg='#fffdf0')
            op_label.place(x=320, y=35)

            def opr_ad_pg():
                op_label = Label(opr, text='1   +   1   =   2     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)

                op_label = Label(opr, text='1   +   2   =   3     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr, text='1   +   3   =   4     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr, text='1   +   4   =   5     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr, text='1   +   5   =   6   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr, text='1   +   6   =   7   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr, text='1   +   7   =   8   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr, text='1   +   8   =   9   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr, text='1   +   9   =   10  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr, text='1   +   10   =  11  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr, text="1", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_ad_pg)
            opr_btn.place(x=400, y=510)

            def opr_ad_pg():
                op_label = Label(opr, text='2   +   1   =   2    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)

                op_label = Label(opr, text='2   +   2   =   4    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr, text='2   +   3   =   5    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr, text='2   +   4   =   6   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr, text='2   +   5   =   7   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr, text='2   +   6   =   8   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr, text='2   +   7   =   9   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr, text='2   +   8   =   10   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr, text='2   +   9   =   11  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr, text='2   +   10   =  12  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr, text="2", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_ad_pg)
            opr_btn.place(x=430, y=510)

            def opr_ad_pg():
                op_label = Label(opr, text='3   +   1   =   4     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)

                op_label = Label(opr, text='3   +   2   =   5     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr, text='3   +   3   =   6     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr, text='3   +   4   =   7     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr, text='3   +   5   =   8     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr, text='3   +   6   =   9   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr, text='3   +   7   =   10   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr, text='3   +   8   =   11   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr, text='3   +   9   =   12   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr, text='3   +   10   =  13  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr, text="3", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_ad_pg)
            opr_btn.place(x=460, y=510)

            def opr_ad_pg():
                op_label = Label(opr, text='4   +   1   =   5     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)

                op_label = Label(opr, text='4   +   2   =   6     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr, text='4   +   3   =   7     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr, text='4   +   4   =   8     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr, text='4   +   5   =   9     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr, text='4   +   6   =   10   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr, text='4   +   7   =   11   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr, text='4   +   8   =   12   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr, text='4   +   9   =   13  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr, text='4   +   10   =  14  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr, text="4", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_ad_pg)
            opr_btn.place(x=490, y=510)

            def opr_ad_pg():
                op_label = Label(opr, text='5   +   1   =   6     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)

                op_label = Label(opr, text='5   +   2   =   7     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr, text='5   +   3   =   8     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr, text='5   +   4   =   9     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr, text='5   +   5   =   10     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr, text='5   +   6   =   11   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr, text='5   +   7   =   12   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr, text='5   +   8   =   13   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr, text='5   +   9   =   14  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr, text='5   +   10   =  15  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr, text="5", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_ad_pg)
            opr_btn.place(x=520, y=510)

        additn_btn = Button(maths, text="ADDITION", font=('Arial', 20, 'bold'), bg='#ffffff', command=additn)
        additn_btn.place(x=330, y=250)

        # ----------------------------------------SUBTRACTION---------------------------------------------------------------
        def subtract_pg():
            opr1 = tk.Toplevel()
            opr1.geometry('1060x595+250+100')
            opr1.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(opr1, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()
            op_label = Label(opr1, text='MATHS-Subtraction', font=('castellar', 29, 'bold'), fg='red3',
                             bg='#fffdf0')
            op_label.place(x=280, y=35)

            def opr_sub_pg():
                op_label = Label(opr1, text='MATHS-Subtraction', font=('castellar', 29, 'bold'), fg='red3',
                                 bg='#fffdf0')
                op_label.place(x=280, y=35)

                op_label = Label(opr1, text='1   -   1   =   0   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)
                op_label.place(x=120, y=170)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr1, text="1", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_sub_pg)
            opr_btn.place(x=400, y=510)

            def opr_sub_pg():
                op_label = Label(opr1, text='2   -   1   =   1   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)

                op_label = Label(opr1, text='2   -   2   =   0   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr1, text='                     ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr1, text="2", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_sub_pg)
            opr_btn.place(x=430, y=510)

            def opr_sub_pg():
                op_label = Label(opr1, text='3   -   1   =   2   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)

                op_label = Label(opr1, text='3   -   2   =   1   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr1, text='3   -   3   =   0  ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr1, text="3", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_sub_pg)
            opr_btn.place(x=460, y=510)

            def opr_sub_pg():
                op_label = Label(opr1, text='4   -   1   =   3   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)

                op_label = Label(opr1, text='4   -   2   =   2   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr1, text='4   -   3   =   1   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr1, text='4   -   4   =   0   ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr1, text="4", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_sub_pg)
            opr_btn.place(x=490, y=510)

            def opr_sub_pg():
                op_label = Label(opr1, text='5   -   1   =   4      ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=170)

                op_label = Label(opr1, text='5   -   2   =   3      ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=240)

                op_label = Label(opr1, text='5   -   3   =   2       ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=310)

                op_label = Label(opr1, text='5   -   4   =   1       ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=380)

                op_label = Label(opr1, text='5   -   5   =   0       ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=120, y=450)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=170)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=240)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=310)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=380)

                op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                 bg='#fff7ea')
                op_label.place(x=620, y=450)

            opr_btn = Button(opr1, text="5", font=('castellar', 12, 'bold'), bg='#fff7ea',
                             command=opr_sub_pg)
            opr_btn.place(x=520, y=510)

        subtract_btn = Button(maths, text="SUBTRACTION", font=('Arial', 20, 'bold'), bg='#ffffff', command=subtract_pg)
        subtract_btn.place(x=290, y=320)

        # ---------------------------------------NUMBERS---------------------------------------------------------------------------------------------
        # Initialize Pygame mixer
        pygame.mixer.init()

        def numbers():
            numbers = tk.Toplevel()
            numbers.geometry('1060x595+250+100')
            numbers.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(numbers, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            numberslabel = Label(numbers, text='NUMBERS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            numberslabel.place(x=395, y=35)

            def back():
                numbers.destroy()

            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
            back_button = Button(numbers, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                 height=74, width=76)
            back_button.image = back_button_image
            back_button.place(x=60, y=460)

            ##---------------------------------------

            zero_image = Image.open("0.png")
            zero_image = zero_image.resize((120, 120))
            zero_photo = ImageTk.PhotoImage(zero_image)

            # Create a label to display the zero image
            zero_label = Label(numbers, image=zero_photo)
            zero_label.image = zero_photo
            zero_label.place(x=100, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("0.mp3")
                    pygame.mixer.music.play()

            # Create a button with the zero image
            zero_button = Button(numbers, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_audio)
            zero_button.place(x=100, y=200)

            ##---------------------------------------

            # Load the one image
            one_image = Image.open("1.png")
            one_image = one_image.resize((120, 120))
            one_photo = ImageTk.PhotoImage(one_image)

            # Create a label to display the one image
            one_label = Label(numbers, image=one_photo)
            one_label.image = one_photo
            one_label.place(x=245, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("1.mp3")
                    pygame.mixer.music.play()

            # Create a button with the one image
            one_button = Button(numbers, image=one_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                command=play_audio)
            one_button.place(x=245, y=200)

            ##---------------------------------------

            # Load the two image
            two_image = Image.open("2.png")
            two_image = two_image.resize((120, 120))
            two_photo = ImageTk.PhotoImage(two_image)

            # Create a label to display the two image
            two_label = Label(numbers, image=two_photo)
            two_label.image = two_photo
            two_label.place(x=390, y=200)

            # Define function to play audio on button click
            def play_two_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("2.mp3")
                    pygame.mixer.music.play()

            # Create a button with the two image
            two_button = Button(numbers, image=two_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                command=play_two_audio)
            two_button.place(x=390, y=200)

            ##---------------------------------------

            # Load the three image
            three_image = Image.open("3.png")
            three_image = three_image.resize((120, 120))
            three_photo = ImageTk.PhotoImage(three_image)

            # Create a label to display the three image
            three_label = Label(numbers, image=three_photo)
            three_label.image = three_photo
            three_label.place(x=540, y=200)

            # Define function to play audio on button click
            def play_three_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("3.mp3")
                    pygame.mixer.music.play()

            # Create a button with the three image
            three_button = Button(numbers, image=three_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_three_audio)
            three_button.place(x=540, y=200)

            ##---------------------------------------

            four_image = Image.open("4.png")
            four_image = four_image.resize((120, 120))
            four_photo = ImageTk.PhotoImage(four_image)

            # Create a label to display the four image
            four_label = Label(numbers, image=four_photo)
            four_label.image = four_photo
            four_label.place(x=690, y=200)

            # Define function to play audio on button click
            def play_four_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("4.mp3")
                    pygame.mixer.music.play()

            # Create a button with the four image
            four_button = Button(numbers, image=four_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_four_audio)
            four_button.place(x=690, y=200)

            ##---------------------------------------

            # Load the five image
            five_image = Image.open("5.png")
            five_image = five_image.resize((120, 120))
            five_photo = ImageTk.PhotoImage(five_image)

            # Create a label to display the five image
            five_label = Label(numbers, image=five_photo)
            five_label.image = five_photo
            five_label.place(x=840, y=200)

            # Define function to play audio on button click
            def play_five_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("5.mp3")
                    pygame.mixer.music.play()

            # Create a button with the five image
            five_button = Button(numbers, image=five_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_five_audio)
            five_button.place(x=840, y=200)

            ##---------------------------------------

            six_image = Image.open("6.png")
            six_image = six_image.resize((120, 120))
            six_photo = ImageTk.PhotoImage(six_image)

            # Create a label to display the six image
            six_label = Label(numbers, image=six_photo)
            six_label.image = six_photo
            six_label.place(x=180, y=350)

            # Define function to play audio on button click
            def play_six_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("6.mp3")
                    pygame.mixer.music.play()

            # Create a button with the six image
            six_button = Button(numbers, image=six_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                command=play_six_audio)
            six_button.place(x=180, y=350)

            ##---------------------------------------

            # Load and resize the image for seven
            seven_image = Image.open("7.png")
            seven_image = seven_image.resize((120, 120))
            seven_photo = ImageTk.PhotoImage(seven_image)

            # Create a label to display the seven image
            seven_label = Label(numbers, image=seven_photo)
            seven_label.image = seven_photo
            seven_label.place(x=320, y=350)

            # Define function to play audio on button click
            def play_seven_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("7.mp3")
                    pygame.mixer.music.play()

            # Create a button with the seven image
            seven_button = Button(numbers, image=seven_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_seven_audio)
            seven_button.place(x=320, y=350)

            ##---------------------------------------

            eight_image = Image.open("8.png")
            eight_image = eight_image.resize((120, 120))
            eight_photo = ImageTk.PhotoImage(eight_image)

            # Create a label to display the eight image
            eight_label = Label(numbers, image=eight_photo)
            eight_label.image = eight_photo
            eight_label.place(x=460, y=350)

            # Define function to play audio on button click
            def play_eight_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("8.mp3")
                    pygame.mixer.music.play()

            # Create a button with the eight image
            eight_button = Button(numbers, image=eight_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_eight_audio)
            eight_button.place(x=460, y=350)

            ##---------------------------------------

            nine_image = Image.open("9.png")
            nine_image = nine_image.resize((120, 120))
            nine_photo = ImageTk.PhotoImage(nine_image)

            # Create a label to display the nine image
            nine_label = Label(numbers, image=nine_photo)
            nine_label.image = nine_photo
            nine_label.place(x=600, y=350)

            # Define function to play audio on button click
            def play_nine_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("9.mp3")
                    pygame.mixer.music.play()

            # Create a button with the nine image
            nine_button = Button(numbers, image=nine_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_nine_audio)
            nine_button.place(x=600, y=350)

            ##---------------------------------------

            ten_image = Image.open("10.png")
            ten_image = ten_image.resize((120, 120))
            ten_photo = ImageTk.PhotoImage(ten_image)

            # Create a label to display the ten image
            ten_label = Label(numbers, image=ten_photo)
            ten_label.image = ten_photo
            ten_label.place(x=740, y=350)

            # Define function to play audio on button click
            def play_ten_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("10.mp3")
                    pygame.mixer.music.play()

            # Create a button with the ten image
            ten_button = Button(numbers, image=ten_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                command=play_ten_audio)
            ten_button.place(x=740, y=350)

            def new():
                new = tk.Toplevel()
                new.geometry('1060x595+250+100')
                new.title('Teachify - For Kids')

                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.png")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(new, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                ##---------------------------------------

                eleven_image = Image.open("11.png")
                eleven_image = eleven_image.resize((120, 120))
                eleven_photo = ImageTk.PhotoImage(eleven_image)

                # Create a label to display the image
                eleven_label = Label(new, image=eleven_photo)
                eleven_label.image = eleven_photo
                eleven_label.place(x=130, y=200)

                # Define function to play audio on button click
                def play_eleven_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("11a.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                eleven_button = Button(new, image=eleven_photo, bg='white', relief=FLAT, bd=0,
                                       highlightthickness=0, command=play_eleven_audio)
                eleven_button.place(x=130, y=200)

                ##---------------------------------------

                # Load and resize the image
                twelve_image = Image.open("12.png")
                twelve_image = twelve_image.resize((120, 120))
                twelve_photo = ImageTk.PhotoImage(twelve_image)

                # Create a label to display the image
                twelve_label = Label(new, image=twelve_photo)
                twelve_label.image = twelve_photo
                twelve_label.place(x=300, y=200)

                # Define function to play audio on button click
                def play_twelve_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("12a.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                twelve_button = Button(new, image=twelve_photo, bg='white', relief=FLAT, bd=0,
                                       highlightthickness=0, command=play_twelve_audio)
                twelve_button.place(x=300, y=200)

                ##---------------------------------------

                # Load and resize the image
                thirteen_image = Image.open("13.png")
                thirteen_image = thirteen_image.resize((120, 120))
                thirteen_photo = ImageTk.PhotoImage(thirteen_image)

                # Create a label to display the image
                thirteen_label = Label(new, image=thirteen_photo)
                thirteen_label.image = thirteen_photo
                thirteen_label.place(x=470, y=200)

                # Define function to play audio on button click
                def play_thirteen_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("13a.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                thirteen_button = Button(new, image=thirteen_photo, bg='white', relief=FLAT, bd=0,
                                         highlightthickness=0, command=play_thirteen_audio)
                thirteen_button.place(x=470, y=200)

                ##---------------------------------------

                # Load and resize the image
                fourteen_image = Image.open("14.png")
                fourteen_image = fourteen_image.resize((120, 120))
                fourteen_photo = ImageTk.PhotoImage(fourteen_image)

                # Create a label to display the image
                fourteen_label = Label(new, image=fourteen_photo)
                fourteen_label.image = fourteen_photo
                fourteen_label.place(x=640, y=200)

                # Define function to play audio on button click
                def play_fourteen_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("14a.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                fourteen_button = Button(new, image=fourteen_photo, bg='white', relief=FLAT, bd=0,
                                         highlightthickness=0, command=play_fourteen_audio)
                fourteen_button.place(x=640, y=200)

                ##---------------------------------------

                fifteen_image = Image.open("15.png")
                fifteen_image = fifteen_image.resize((120, 120))
                fifteen_photo = ImageTk.PhotoImage(fifteen_image)

                # Create a label to display the image
                fifteen_label = Label(new, image=fifteen_photo)
                fifteen_label.image = fifteen_photo
                fifteen_label.place(x=810, y=200)

                # Define function to play audio on button click
                def play_fifteen_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("15a.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                fifteen_button = Button(new, image=fifteen_photo, bg='white', relief=FLAT, bd=0,
                                        highlightthickness=0, command=play_fifteen_audio)
                fifteen_button.place(x=810, y=200)

                ##---------------------------------------

                # Load and resize the image
                sixteen_image = Image.open("16.png")
                sixteen_image = sixteen_image.resize((120, 120))
                sixteen_photo = ImageTk.PhotoImage(sixteen_image)

                # Create a label to display the image
                sixteen_label = Label(new, image=sixteen_photo)
                sixteen_label.image = sixteen_photo
                sixteen_label.place(x=130, y=350)

                # Define function to play audio on button click
                def play_sixteen_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("16.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                sixteen_button = Button(new, image=sixteen_photo, bg='white', relief=FLAT, bd=0,
                                        highlightthickness=0, command=play_sixteen_audio)
                sixteen_button.place(x=130, y=350)

                ##---------------------------------------

                # Load and resize the image
                seventeen_image = Image.open("17.png")
                seventeen_image = seventeen_image.resize((120, 120))
                seventeen_photo = ImageTk.PhotoImage(seventeen_image)

                # Create a label to display the image
                seventeen_label = Label(new, image=seventeen_photo)
                seventeen_label.image = seventeen_photo
                seventeen_label.place(x=300, y=350)

                # Define function to play audio on button click
                def play_seventeen_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("17.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                seventeen_button = Button(new, image=seventeen_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0, command=play_seventeen_audio)
                seventeen_button.place(x=300, y=350)
                ##---------------------------------------

                eighteen_image = Image.open("18.png")
                eighteen_image = eighteen_image.resize((120, 120))
                eighteen_photo = ImageTk.PhotoImage(eighteen_image)

                # Create a label to display the image
                eighteen_label = Label(new, image=eighteen_photo)
                eighteen_label.image = eighteen_photo
                eighteen_label.place(x=470, y=350)

                # Define function to play audio on button click
                def play_eighteen_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("18.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                eighteen_button = Button(new, image=eighteen_photo, bg='white', relief=FLAT, bd=0,
                                         highlightthickness=0, command=play_eighteen_audio)
                eighteen_button.place(x=470, y=350)
                ##---------------------------------------

                nineteen_image = Image.open("19.png")
                nineteen_image = nineteen_image.resize((120, 120))
                nineteen_photo = ImageTk.PhotoImage(nineteen_image)

                # Create a label to display the image
                nineteen_label = Label(new, image=nineteen_photo)
                nineteen_label.image = nineteen_photo
                nineteen_label.place(x=640, y=350)

                # Define function to play audio on button click
                def play_nineteen_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("19.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                nineteen_button = Button(new, image=nineteen_photo, bg='white', relief=FLAT, bd=0,
                                         highlightthickness=0, command=play_nineteen_audio)
                nineteen_button.place(x=640, y=350)

                ##---------------------------------------

                twenty_image = Image.open("20.png")
                twenty_image = twenty_image.resize((120, 120))
                twenty_photo = ImageTk.PhotoImage(twenty_image)

                # Create a label to display the image
                twenty_label = Label(new, image=twenty_photo)
                twenty_label.image = twenty_photo
                twenty_label.place(x=810, y=350)

                # Define function to play audio on button click
                def play_twenty_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("20.mp3")
                        pygame.mixer.music.play()

                # Create a button with the image
                twenty_button = Button(new, image=twenty_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                       command=play_twenty_audio)
                twenty_button.place(x=810, y=350)

                numberslabel = Label(new, text='NUMBERS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                numberslabel.place(x=395, y=35)

            nextButton = Button(numbers, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                activebackground='white',
                                cursor='hand2', command=new)
            nextButton.place(x=840, y=480)

        numbers_btn = Button(maths, text='NUMBERS', font=('Arial', 20, 'bold'), bd=1, command=numbers,
                             bg='#ffffff')
        numbers_btn.place(x=325, y=390)

    maths_btn = Button(three_six, text='MATHS', font=('Arial', 20, 'bold'), bd=1, command=maths,
                       bg='#efd2aa')
    maths_btn.place(x=480, y=160)

    # ======================================================CREATE ALPHABETS BUTTON =================================================#

    def alphabets():
        alphabets = tk.Toplevel()
        alphabets.geometry('1060x595+250+100')
        alphabets.title('Teachify - For Kids')

        # Create a frame to hold the image
        image_frame = Frame(alphabets, bg='white', width=500, height=500)
        image_frame.pack(side=LEFT, padx=0, pady=0)

        # Load the  image
        bg_image = Image.open("COURSES_BG_ICON.png")
        bg_image = bg_image.resize((1050, 595))
        photo = ImageTk.PhotoImage(bg_image)

        # Create a label to display the image
        image_label = Label(image_frame, image=photo, bg='white')
        image_label.image = photo
        image_label.pack()

        alphabetslabel = Label(alphabets, text='ALPHABETS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
        alphabetslabel.place(x=395, y=35)

        def back():
            alphabets.destroy()

        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
        back_button = Button(alphabets, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                             height=74, width=76)
        back_button.image = back_button_image
        back_button.place(x=60, y=460)

        # ***************************************


        # Initialize Pygame mixer
        pygame.mixer.init()




        # Define function for the 'a' window
        def a():
            a = Toplevel()
            a.geometry('1060x595+250+100')
            a.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(a, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(a, text='ALPHABET - A', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            A_Label = Label(a, text='A', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            A_Label.place(x=120, y=230)
            A_Label = Label(a, text='a', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            A_Label.place(x=250, y=285)

            # Load the apple image
            apple_image = Image.open("a.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("a.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(a, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            # Create a button with image next1.png
            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(a, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [a.destroy(), b()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

        # Create a button for 'A' in the main window
        btn_A = Button(alphabets, text='A', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, bd=1, command=a)
        btn_A.place(x=75, y=180)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()

        def b():
            b = tk.Toplevel()
            b.geometry('1060x595+250+100')
            b.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(b, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(b, text='ALPHABET - B', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            B_Label = Label(b, text='B', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            B_Label.place(x=120, y=230)
            B_Label = Label(b, text='b', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            B_Label.place(x=250, y=285)

            # Load the apple image
            apple_image = Image.open("bat.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("b.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(b, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)



            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(b, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [b.destroy(), c()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(b, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [b.destroy(), a()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_B = Button(alphabets, text='B', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=b)
        btn_B.place(x=165, y=180)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()

        def c():
            c = tk.Toplevel()
            c.geometry('1060x595+250+100')
            c.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(c, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(c, text='ALPHABET - C', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            C_Label = Label(c, text='C', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            C_Label.place(x=120, y=230)
            C_Label = Label(c, text='c', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            C_Label.place(x=250, y=285)

            # Load the apple image
            apple_image = Image.open("c.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("c.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(c, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(c, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [c.destroy(), d()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(c, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [c.destroy(), b()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_C = Button(alphabets, text='C', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=c)
        btn_C.place(x=255, y=180)

        # ***************************************
        # Initialize Pygame mixer
        pygame.mixer.init()
        def d():
            D = tk.Toplevel()
            D.geometry('1060x595+250+100')
            D.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(D, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(D, text='ALPHABET - D', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            D_Label = Label(D, text='D', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            D_Label.place(x=120, y=230)
            D_Label = Label(D, text='d', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            D_Label.place(x=250, y=285)

            # Load the apple image
            apple_image = Image.open("d.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("d.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(D, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(D, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [D.destroy(), E()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(D, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [D.destroy(), c()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_D = Button(alphabets, text='D', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=d)
        btn_D.place(x=348, y=180)

        # ***************************************
        # Initialize Pygame mixer
        pygame.mixer.init()

        def E():
            E = tk.Toplevel()
            E.geometry('1060x595+250+100')
            E.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(E, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(E, text='ALPHABET - E', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            E_Label = Label(E, text='E', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            E_Label.place(x=120, y=230)
            E_Label = Label(E, text='e', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            E_Label.place(x=250, y=285)

            # Load the apple image
            apple_image = Image.open("e.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("e.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(E, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(E, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [E.destroy(), F()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(E, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [E.destroy(), d()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_E = Button(alphabets, text='E', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=E)
        btn_E.place(x=435, y=180)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def F():
            F = tk.Toplevel()
            F.geometry('1060x595+250+100')
            F.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(F, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(F, text='ALPHABET - F', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            F_Label = Label(F, text='F', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            F_Label.place(x=120, y=230)
            F_Label = Label(F, text='f', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            F_Label.place(x=230, y=300)

            # Load the apple image
            apple_image = Image.open("frog.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("f.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(F, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(F, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [F.destroy(), G()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(F, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [F.destroy(), E()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_F = Button(alphabets, text='F', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=F)
        btn_F.place(x=525, y=180)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def G():
            G = tk.Toplevel()
            G.geometry('1060x595+250+100')
            G.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(G, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(G, text='ALPHABET - G', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            G_Label = Label(G, text='G', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            G_Label.place(x=120, y=230)
            G_Label = Label(G, text='g', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            G_Label.place(x=250, y=285)

            # Load the apple image
            apple_image = Image.open("goat.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("g.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(G, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(G, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [G.destroy(), H()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(G, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [G.destroy(), F()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_G = Button(alphabets, text='G', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=G)
        btn_G.place(x=615, y=180)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()


        def H():
            H = tk.Toplevel()
            H.geometry('1060x595+250+100')
            H.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(H, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(H, text='ALPHABET - H', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            H_Label = Label(H, text='H', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            H_Label.place(x=120, y=230)
            H_Label = Label(H, text='h', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            H_Label.place(x=250, y=290)

            # Load the apple image
            apple_image = Image.open("h for hat.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("h.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(H, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)
            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(H, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [H.destroy(), I()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(H, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [H.destroy(), G()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_H = Button(alphabets, text='H', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=H)
        btn_H.place(x=705, y=180)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def I():
            I = tk.Toplevel()
            I.geometry('1060x595+250+100')
            I.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(I, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(I, text='ALPHABET - I', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            I_Label = Label(I, text='I', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            I_Label.place(x=120, y=230)
            I_Label = Label(I, text='i', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            I_Label.place(x=250, y=285)

            # Load the apple image
            apple_image = Image.open("insect.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("i.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(I, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(I, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [I.destroy(), j()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(I, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [I.destroy(), H()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_i = Button(alphabets, text='I', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=I)
        btn_i.place(x=795, y=180)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def j():
            j = tk.Toplevel()
            j.geometry('1060x595+250+100')
            j.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(j, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(j, text='ALPHABET - J', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            j_Label = Label(j, text='J', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            j_Label.place(x=120, y=230)
            j_Label = Label(j, text='j', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            j_Label.place(x=230, y=285)

            # Load the apple image
            apple_image = Image.open("j.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("j.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(j, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)


            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(j, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [j.destroy(), K()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(j, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [j.destroy(), I()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_J = Button(alphabets, text='J', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=j)
        btn_J.place(x=885, y=180)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()

        def K():
            K = tk.Toplevel()
            K.geometry('1060x595+250+100')
            K.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(K, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(K, text='ALPHABET - K', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            K_Label = Label(K, text='K', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            K_Label.place(x=120, y=230)
            K_Label = Label(K, text='k', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            K_Label.place(x=255, y=290)

            # Load the apple image
            apple_image = Image.open("kite.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)


            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("K.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(K, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)


            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(K, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [K.destroy(), L()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(K, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [K.destroy(), j()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_K = Button(alphabets, text='K', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=K)
        btn_K.place(x=75, y=300)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()

        def L():
            L = tk.Toplevel()
            L.geometry('1060x595+250+100')
            L.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(L, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(L, text='ALPHABET - L', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            L_Label = Label(L, text='L', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            L_Label.place(x=120, y=230)
            L_Label = Label(L, text='l', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            L_Label.place(x=245, y=290)

            # Load the apple image
            apple_image = Image.open("leaf.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("l.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(L, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(L, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [L.destroy(), M()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(L, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [L.destroy(), K()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_L = Button(alphabets, text='L', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=L)
        btn_L.place(x=165, y=300)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def M():
            M = tk.Toplevel()
            M.geometry('1060x595+250+100')
            M.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(M, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(M, text='ALPHABET - M', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            M_Label = Label(M, text='M', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            M_Label.place(x=120, y=230)
            M_Label = Label(M, text='m', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            M_Label.place(x=260, y=290)

            # Load the apple image
            apple_image = Image.open("monkey.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("m.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(M, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(M, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [M.destroy(), N()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(M, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [M.destroy(), L()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_M = Button(alphabets, text='M', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=M)
        btn_M.place(x=255, y=300)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()

        def N():
            N = tk.Toplevel()
            N.geometry('1060x595+250+100')
            N.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(N, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(N, text='ALPHABET - N', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            N_Label = Label(N, text='N', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            N_Label.place(x=120, y=230)
            N_Label = Label(N, text='n', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            N_Label.place(x=245, y=290)

            # Load the apple image
            apple_image = Image.open("n.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("n.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(N, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(N, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [N.destroy(), O()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(N, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [N.destroy(), M()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_N = Button(alphabets, text='N', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=N)
        btn_N.place(x=348, y=300)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def O():
            O = tk.Toplevel()
            O.geometry('1060x595+250+100')
            O.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(O, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(O, text='ALPHABET - O', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            O_Label = Label(O, text='O', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            O_Label.place(x=120, y=230)
            O_Label = Label(O, text='o', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            O_Label.place(x=260, y=290)

            # Load the apple image
            apple_image = Image.open("ocean.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("o.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(O, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(O, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [O.destroy(), P()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(O, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [O.destroy(), N()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_O = Button(alphabets, text='O', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=O)
        btn_O.place(x=435, y=300)

        # ***************************************
        # Initialize Pygame mixer
        pygame.mixer.init()

        def P():
            P = tk.Toplevel()
            P.geometry('1060x595+250+100')
            P.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(P, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(P, text='ALPHABET - P', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            P_Label = Label(P, text='P', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            P_Label.place(x=120, y=230)
            P_Label = Label(P, text='p', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            P_Label.place(x=235, y=290)

            # Load the apple image
            apple_image = Image.open("plum.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("p.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(P, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(P, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [P.destroy(), Q()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(P, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [P.destroy(), O()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_P = Button(alphabets, text='P', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=P)
        btn_P.place(x=525, y=300)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()

        def Q():
            Q = tk.Toplevel()
            Q.geometry('1060x595+250+100')
            Q.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(Q, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(Q, text='ALPHABET - Q', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            Q_Label = Label(Q, text='Q', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            Q_Label.place(x=120, y=230)
            Q_Label = Label(Q, text='q', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            Q_Label.place(x=260, y=290)

            # Load the apple image
            apple_image = Image.open("queen.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("q.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(Q, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(Q, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [Q.destroy(), R()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(Q, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [Q.destroy(), P()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_Q = Button(alphabets, text='Q', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=Q)
        btn_Q.place(x=615, y=300)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()

        def R():
            R = tk.Toplevel()
            R.geometry('1060x595+250+100')
            R.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(R, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(R, text='ALPHABET - R', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            R_Label = Label(R, text='R', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            R_Label.place(x=120, y=230)
            R_Label = Label(R, text='r', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            R_Label.place(x=260, y=290)

            # Load the apple image
            apple_image = Image.open("rat.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("r.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(R, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(R, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [R.destroy(), S()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(R, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [R.destroy(), Q()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_R = Button(alphabets, text='R', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=R)
        btn_R.place(x=705, y=300)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()




        def S():
            S = tk.Toplevel()
            S.geometry('1060x595+250+100')
            S.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(S, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(S, text='ALPHABET - S', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            S_Label = Label(S, text='S', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            S_Label.place(x=120, y=230)
            S_Label = Label(S, text='s', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            S_Label.place(x=245, y=290)

            # Load the apple image
            apple_image = Image.open("s.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("s.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(S, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(S, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [S.destroy(), T()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(S, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [S.destroy(), R()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_S = Button(alphabets, text='S', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=S)
        btn_S.place(x=795, y=300)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def T():
            T = tk.Toplevel()
            T.geometry('1060x595+250+100')
            T.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(T, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(T, text='ALPHABET - T', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            T_Label = Label(T, text='T', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            T_Label.place(x=120, y=230)
            T_Label = Label(T, text='t', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            T_Label.place(x=220, y=290)

            # Load the apple image
            apple_image = Image.open("tap.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("t.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(T, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(T, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [T.destroy(), U()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(T, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [T.destroy(), S()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_T = Button(alphabets, text='T', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=T)
        btn_T.place(x=885, y=300)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()


        def U():
            U = tk.Toplevel()
            U.geometry('1060x595+250+100')
            U.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(U, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(U, text='ALPHABET - U', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            U_Label = Label(U, text='U', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            U_Label.place(x=120, y=230)
            U_Label = Label(U, text='u', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            U_Label.place(x=245, y=290)

            # Load the apple image
            apple_image = Image.open("u.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("u.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(U, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(U, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [U.destroy(), V()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(U, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [U.destroy(), T()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_U = Button(alphabets, text='U', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=U)
        btn_U.place(x=255, y=420)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def V():
            V = tk.Toplevel()
            V.geometry('1060x595+250+100')
            V.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(V, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(V, text='ALPHABET - V', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            V_Label = Label(V, text='V', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            V_Label.place(x=120, y=230)
            V_Label = Label(V, text='v', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            V_Label.place(x=240, y=290)

            # Load the apple image
            apple_image = Image.open("v.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("v.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(V, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(V, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [V.destroy(), W()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(V, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [V.destroy(), U()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_V = Button(alphabets, text='V', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=V)
        btn_V.place(x=348, y=420)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()

        def W():
            W = tk.Toplevel()
            W.geometry('1060x595+250+100')
            W.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(W, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(W, text='ALPHABET - W', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            W_Label = Label(W, text='W', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            W_Label.place(x=120, y=230)
            W_Label = Label(W, text='w', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            W_Label.place(x=285, y=290)

            # Load the apple image
            apple_image = Image.open("well.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("w.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(W, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(W, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [W.destroy(), X()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(W, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [W.destroy(), V()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_W = Button(alphabets, text='W', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=W)
        btn_W.place(x=435, y=420)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def X():
            X = tk.Toplevel()
            X.geometry('1060x595+250+100')
            X.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(X, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(X, text='ALPHABET - V', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            X_Label = Label(X, text='X', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            X_Label.place(x=120, y=230)
            X_Label = Label(X, text='x', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            X_Label.place(x=240, y=290)

            # Load the apple image
            apple_image = Image.open("x.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("x.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(X, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(X, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [X.destroy(), Y()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(X, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [X.destroy(), W()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_X = Button(alphabets, text='X', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=X)
        btn_X.place(x=525, y=420)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def Y():
            Y = tk.Toplevel()
            Y.geometry('1060x595+250+100')
            Y.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(Y, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(Y, text='ALPHABET - Y', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            # Load the apple image
            apple_image = Image.open("y.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("y.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(Y, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            Y_Label = Label(Y, text='Y', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            Y_Label.place(x=120, y=230)
            Y_Label = Label(Y, text='y', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            Y_Label.place(x=225, y=290)

            next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
            next_button = Button(Y, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [Y.destroy(), Z()])
            next_button.image = next_button_image
            next_button.place(x=930, y=460)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(Y, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [Y.destroy(), X()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_Y = Button(alphabets, text='Y', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=Y)
        btn_Y.place(x=615, y=420)

        # ***************************************

        # Initialize Pygame mixer
        pygame.mixer.init()
        def Z():
            Z = tk.Toplevel()
            Z.geometry('1060x595+250+100')
            Z.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(Z, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(Z, text='ALPHABET - Z', font=('castellar', 29, 'bold'), fg='red3',
                                   bg='#fffdf0')
            alphabetslabel.place(x=380, y=35)

            Z_Label = Label(Z, text='Z', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
            Z_Label.place(x=120, y=230)
            Z_Label = Label(Z, text='z', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
            Z_Label.place(x=240, y=290)

            # Load the apple image
            apple_image = Image.open("zz.png")
            apple_image = apple_image.resize((300, 300))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("z.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(Z, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=600, y=180)

            back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
            back_button = Button(Z, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [Z.destroy(), Y()])
            back_button.image = back_button_image
            back_button.place(x=110, y=460)

        btn_Z = Button(alphabets, text='Z', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                       width=2, command=Z)
        btn_Z.place(x=705, y=420)

    alphabets_btn = Button(three_six, text='ALPHABETS', font=('Arial', 20, 'bold'), bd=1, command=alphabets,
                           bg='#efd2aa')
    alphabets_btn.place(x=435, y=235)



    #---------------nursury poems------

    # Initialize Pygame mixer
    pygame.mixer.init()

    def poems():
        poems = tk.Toplevel()
        poems.geometry('1060x595+250+100')
        poems.title('Teachify - For Kids')

        # Create a frame to hold the image
        image_frame = Frame(poems, bg='white', width=500, height=500)
        image_frame.pack(side=LEFT, padx=0, pady=0)

        # Load the  image
        bg_image = Image.open("COURSES_BG_ICON.png")
        bg_image = bg_image.resize((1050, 595))
        photo = ImageTk.PhotoImage(bg_image)

        # Create a label to display the image
        image_label = Label(image_frame, image=photo, bg='white')
        image_label.image = photo
        image_label.pack()

        poemslabel = Label(poems, text='NURSERY RHYMES', font=('castellar', 29, 'bold'), fg='red3',
                           bg='#fffdf0')
        poemslabel.place(x=320, y=35)

        def poem1():
            poem1 = tk.Toplevel()
            poem1.geometry('1060x595+250+100')
            poem1.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(poem1, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("poem1bg.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            text_label = Label(poem1,
                               text="Twinkle, twinkle, little star,\nHow I wonder what you are.\nUp above the world so high,\nLike a diamond in the sky.",
                               font=("Bradley Hand", 36), bg='white')
            text_label.place(x=240, y=190)

            zero_image = Image.open("speak.png")
            zero_image = zero_image.resize((56, 56))
            zero_photo = ImageTk.PhotoImage(zero_image)

            # Create a label to display the zero image
            zero_label = Label(poem1, image=zero_photo)
            zero_label.image = zero_photo
            zero_label.place(x=100, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("Twinkle Twinkle Little star .mp3")
                    pygame.mixer.music.play()

            # Create a button with the zero image
            zero_button = Button(poem1, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_audio)
            zero_button.place(x=100, y=200)





        poem1_btn = Button(poems, font=('Arial', 20, 'bold'), text="Twinkle Twinkle Tittle Star", bg='#efd2aa', bd=1,
                           command=poem1)

        poem1_btn.place(x=130, y=190)

        def poem2():
            poem2 = tk.Toplevel()
            poem2.geometry('1060x595+250+100')
            poem2.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(poem2, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("poem2bg.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            text_label = Label(poem2,
                               text='Jack and Jill went up the hill\nTo fetch a pail of water.\nJack fell down and broke his crow\nAnd Jill came tumbling after.\nThen up got Jack and said to Jill,\nAs in his arms he took her,\n“Brush off that dirt for you’re not hurt,\nLet’s fetch that pail of water.”\nSo Jack and Jill went up the hill\nTo fetch the pail of water,\nAnd took it home to Mother dear,\nWho thanked her son and daughter.',
                               font=("Bradley Hand", 28), bg='white')
            text_label.place(x=240, y=40)

            zero_image = Image.open("speak.png")
            zero_image = zero_image.resize((56, 56))
            zero_photo = ImageTk.PhotoImage(zero_image)

            # Create a label to display the zero image
            zero_label = Label(poem2, image=zero_photo)
            zero_label.image = zero_photo
            zero_label.place(x=100, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("Jack And Jill .mp3")
                    pygame.mixer.music.play()

            # Create a button with the zero image
            zero_button = Button(poem2, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_audio)
            zero_button.place(x=100, y=200)

        poem2_btn = Button(poems, font=('Arial', 20, 'bold'), text="Jack And Jill", bg='#efd2aa', bd=1,
                           command=poem2)

        poem2_btn.place(x=130, y=260)

        def poem3():
            poem3 = tk.Toplevel()
            poem3.geometry('1060x595+250+100')
            poem3.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(poem3, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("poem3bg.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            text_label = Label(poem3,
                               text="I'm a little teapot,\nShort and stout,\nHere is my handle\nHere is my spout\nWhen I get all steamed up,\nHear me shout,\nTip me over and pour me out!\nI'm a very special teapot,\nYes, it's true,\nHere's an example of what I can do,\nI can turn my handle into a spout,\nTip me over and pour me out!",
                               font=("Bradley Hand", 28), bg='white')
            text_label.place(x=240, y=40)

            zero_image = Image.open("speak.png")
            zero_image = zero_image.resize((56, 56))
            zero_photo = ImageTk.PhotoImage(zero_image)

            # Create a label to display the zero image
            zero_label = Label(poem3, image=zero_photo)
            zero_label.image = zero_photo
            zero_label.place(x=100, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("I'm A Little Teapot .mp3")
                    pygame.mixer.music.play()

            # Create a button with the zero image
            zero_button = Button(poem3, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_audio)
            zero_button.place(x=100, y=200)



        poem3_btn = Button(poems, font=('Arial', 20, 'bold'), text="I'm a little teapot", bg='#efd2aa', bd=1,
                           command=poem3)

        poem3_btn.place(x=130, y=330)

        def poem4():
            poem4 = tk.Toplevel()
            poem4.geometry('1060x595+250+100')
            poem4.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(poem4, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("poem4bg.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            text_label = Label(poem4,
                               text="Humpty Dumpty sat on a wall.\nHumpty Dumpty had a great fall.\nAll the king’s horses and all the king’s men\ncouldn’t put Humpty together again.\nHumpty Dumpty sat on a wall.\nHumpty Dumpty had a great fall.\nAll the king’s horses and all the king’s men\ncouldn’t put Humpty together again.\nHumpty Dumpty sat on a wall.\nHumpty Dumpty had a great fall.\nAll the king’s horses and all the king’s men\ncouldn’t put Humpty together again.",
                               font=("Bradley Hand", 28), bg='white')
            text_label.place(x=200, y=40)

            zero_image = Image.open("speak.png")
            zero_image = zero_image.resize((56, 56))
            zero_photo = ImageTk.PhotoImage(zero_image)

            # Create a label to display the zero image
            zero_label = Label(poem4, image=zero_photo)
            zero_label.image = zero_photo
            zero_label.place(x=100, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("Humpty Dumpty .mp3")
                    pygame.mixer.music.play()

            # Create a button with the zero image
            zero_button = Button(poem4, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_audio)
            zero_button.place(x=100, y=200)


        poem4_btn = Button(poems, font=('Arial', 20, 'bold'), text="Humpty Dumpty", bg='#efd2aa', bd=1,
                           command=poem4)

        poem4_btn.place(x=130, y=400)

        def poem5():
            poem5 = tk.Toplevel()
            poem5.geometry('1060x595+250+100')
            poem5.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(poem5, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("poem5bg.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            text_label = Label(poem5,
                               text="Ring-a-ring-a-rosies\nA pocket full of posies\nA tissue, a tissue\nWe all fall down\nThe king has sent his daughter\nTo fetch a pail of water\nA tissue, a tissue\nWe all fall down\nThe robin on the steeple\nIs singing to the people\nA tissue, a tissue\nWe all fall down\nThe wedding bells are ringing\nThe boys and girls are singing\nA tissue, a tissue\nWe all fall down",
                               font=("Bradley Hand", 24), bg='white')
            text_label.place(x=290, y=7)

            zero_image = Image.open("speak.png")
            zero_image = zero_image.resize((56, 56))
            zero_photo = ImageTk.PhotoImage(zero_image)

            # Create a label to display the zero image
            zero_label = Label(poem5, image=zero_photo)
            zero_label.image = zero_photo
            zero_label.place(x=100, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("evokids - Ring Around The Rosie.mp3")
                    pygame.mixer.music.play()

            # Create a button with the zero image
            zero_button = Button(poem5, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_audio)
            zero_button.place(x=100, y=200)

        poem5_btn = Button(poems, font=('Arial', 20, 'bold'), text="Ring around the roses", bg='#efd2aa', bd=1,
                           command=poem5)

        poem5_btn.place(x=600, y=190)

        def poem6():
            poem6 = tk.Toplevel()
            poem6.geometry('1060x595+250+100')
            poem6.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(poem6, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("poem6bg.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            text_label = Label(poem6,
                               text="Row, row, row your boat\nGently down the stream\nMerrily merrily, merrily, merrily\nLife is but a dream\nRow, row, row your boat\nGently down the stream\nMerrily merrily, merrily, merrily\nLife is but a dream\nRow, row, row your boat\nGently down the stream\nMerrily merrily, merrily, merrily\nLife is but a dream\nRow, row, row your boat\nGently down the stream\nMerrily merrily, merrily, merrily\nLife is but a dream",
                               font=("Bradley Hand", 22), bg='white')
            text_label.place(x=290, y=10)

            zero_image = Image.open("speak.png")
            zero_image = zero_image.resize((56, 56))
            zero_photo = ImageTk.PhotoImage(zero_image)

            # Create a label to display the zero image
            zero_label = Label(poem6, image=zero_photo)
            zero_label.image = zero_photo
            zero_label.place(x=100, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("Row Row Row Your Boat .mp3")
                    pygame.mixer.music.play()

            # Create a button with the zero image
            zero_button = Button(poem6, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_audio)
            zero_button.place(x=100, y=200)

        poem6_btn = Button(poems, font=('Arial', 20, 'bold'), text="Row,Row,Row your boat.", bg='#efd2aa', bd=1,
                           command=poem6)

        poem6_btn.place(x=600, y=260)

        def poem8():
            poem8 = tk.Toplevel()
            poem8.geometry('1060x595+250+100')
            poem8.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(poem8, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("poem8bg.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            text_label = Label(poem8,
                               text="Baa, baa black sheep\nHave you any wool\nYes sir, yes sir\nThree bags full.\n\nOne for my master\nAnd one for my dame\nAnd one for the little boy\nWho lives down the lane",
                               font=("Bradley Hand", 26), bg='white')
            text_label.place(x=320, y=100)

            zero_image = Image.open("speak.png")
            zero_image = zero_image.resize((56, 56))
            zero_photo = ImageTk.PhotoImage(zero_image)

            # Create a label to display the zero image
            zero_label = Label(poem8, image=zero_photo)
            zero_label.image = zero_photo
            zero_label.place(x=100, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("BAA BAA BLACK SHEEP .mp3")
                    pygame.mixer.music.play()

            # Create a button with the zero image
            zero_button = Button(poem8, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_audio)
            zero_button.place(x=100, y=200)

        poem8_btn = Button(poems, font=('Arial', 20, 'bold'), text="Baa Baa Black Sheep.", bg='#efd2aa', bd=1,
                           command=poem8)

        poem8_btn.place(x=600, y=330)

        def poem7():
            poem7 = tk.Toplevel()
            poem7.geometry('1060x595+250+100')
            poem7.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(poem7, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("poem7bg.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            text_label = Label(poem7,
                               text="Incy wincy spider\nclimbed up the water spout,\nDown came the rain\nand washed poor Wincy out,\n\nOut came the sun shine\nand dried up all the rain,\nAnd Incy Wincy spider\nclimbed up the spout again.",
                               font=("Bradley Hand", 26), bg='white')
            text_label.place(x=320, y=100)

            zero_image = Image.open("speak.png")
            zero_image = zero_image.resize((56, 56))
            zero_photo = ImageTk.PhotoImage(zero_image)

            # Create a label to display the zero image
            zero_label = Label(poem7, image=zero_photo)
            zero_label.image = zero_photo
            zero_label.place(x=100, y=200)

            # Define function to play audio on button click
            def play_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("Incy Wincy Spider .mp3")
                    pygame.mixer.music.play()

            # Create a button with the zero image
            zero_button = Button(poem7, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                 command=play_audio)
            zero_button.place(x=100, y=200)



        poem7_btn = Button(poems, font=('Arial', 20, 'bold'), text="Incy Wincy spider.", bg='#efd2aa', bd=1,
                           command=poem7)

        poem7_btn.place(x=600, y=400)

    poems_btn = Button(three_six, font=('Arial', 20, 'bold'), text="NURSERY RHYMES", bg='#efd2aa', bd=1,command=poems)


    poems_btn.place(x=390,y = 310)


    ##========================================================PICTURE BOOK BUTTON===========================================================
    def book():
        book = tk.Toplevel()
        book.geometry('1060x595+250+100')
        book.title('Teachify - For Kids')

        # Create a frame to hold the image
        image_frame = Frame(book, bg='white', width=500, height=500)
        image_frame.pack(side=LEFT, padx=0, pady=0)

        # Load the  image
        bg_image = Image.open("new_bg.png")
        bg_image = bg_image.resize((1050, 595))
        photo = ImageTk.PhotoImage(bg_image)

        # Create a label to display the image
        image_label = Label(image_frame, image=photo, bg='white')
        image_label.image = photo
        image_label.pack()

        booklabel = Label(book, text='PICTURE BOOK', font=('castellar', 29, 'bold'), fg='red3', bg='#ffffff')
        booklabel.place(x=240, y=95)

        def back():
            book.destroy()

        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
        back_button = Button(book, image=back_button_image, bd=0, command=back, bg='#ffffff',
                             height=74, width=76)
        back_button.image = back_button_image
        back_button.place(x=90, y=380)

        def emo():
            emo = tk.Toplevel()
            emo.geometry('1060x595+250+100')
            emo.title('Teachify - For Kids')

            # Load the sunset image
            sunset_image = Image.open("COURSES_BG_ICON.jpg")
            sunset_image = sunset_image.resize((1050, 595))
            sunset_photo = ImageTk.PhotoImage(sunset_image)

            # Create a label to display the sunset image
            sunset_label = Label(emo, image=sunset_photo)
            sunset_label.image = sunset_photo
            sunset_label.place(x=0, y=0)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("angry.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(emo, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=80, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("confused.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(emo, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=310, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("cry.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(emo, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=540, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("disappointed.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(emo, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=770, y=210)

            numberslabel = Label(emo, text='HUMAN EMOTIONS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            numberslabel.place(x=300, y=35)

            def back():
                emo.destroy()

            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
            back_button = Button(emo, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                 height=74, width=76)
            back_button.image = back_button_image
            back_button.place(x=60, y=460)

            def neww():
                neww = tk.Toplevel()
                neww.geometry('1060x595+250+100')
                neww.title('Teachify - For Kids')

                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(neww, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("disgusted.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(neww, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=80, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("happy - Copy.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(neww, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("jelous.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(neww, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("loving - Copy.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(neww, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=770, y=210)

                numberslabel = Label(neww, text='HUMAN EMOTIONS', font=('castellar', 29, 'bold'), fg='red3',
                                     bg='#fffdf0')
                numberslabel.place(x=300, y=35)

                def back():
                    neww.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(neww, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def back():
                    neww.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(neww, image=back_button_image, bd=0, command=back, bg='#fff7ea', height=74,
                                     width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                next_button_image = ImageTk.PhotoImage(Image.open("next2.png").resize((50, 50)))

                def open_new_window():
                    neww.after(1, lambda: [neww.destroy(),
                                           new1()])  # Delay the destruction of current window and creation of new window by 100ms

                next_button = Button(neww, image=next_button_image, bg='#fff7ea', bd=0, command=open_new_window)
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                def new1():
                    new1 = tk.Toplevel()
                    new1.geometry('1060x595+250+100')
                    new1.title('Teachify - For Kids')

                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(new1, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    numberslabel = Label(new1, text='HUMAN EMOTIONS', font=('castellar', 29, 'bold'), fg='red3',
                                         bg='#fffdf0')
                    numberslabel.place(x=300, y=35)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("nervous.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(new1, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=80, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("proud.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(new1, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=310, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("sad.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(new1, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=540, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("scared.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(new1, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=770, y=210)

                    def back():
                        new1.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(new1, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    def new2():
                        new2 = tk.Toplevel()
                        new2.geometry('1060x595+250+100')
                        new2.title('Teachify - For Kids')

                        # Load the sunset image
                        sunset_image = Image.open("COURSES_BG_ICON.jpg")
                        sunset_image = sunset_image.resize((1050, 595))
                        sunset_photo = ImageTk.PhotoImage(sunset_image)

                        # Create a label to display the sunset image
                        sunset_label = Label(new2, image=sunset_photo)
                        sunset_label.image = sunset_photo
                        sunset_label.place(x=0, y=0)

                        numberslabel = Label(new2, text='HUMAN EMOTIONS', font=('castellar', 29, 'bold'), fg='red3',
                                             bg='#fffdf0')
                        numberslabel.place(x=300, y=35)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("shy.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(new2, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=80, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("sick.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(new2, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=310, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("silly.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(new2, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=540, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("surprised .png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(new2, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=770, y=210)

                        def back():
                            new2.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(new2, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                             height=74, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=460)

                    nextButton = Button(new1, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=new2)
                    nextButton.place(x=840, y=480)

                nextButton = Button(neww, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=new1)
                nextButton.place(x=840, y=480)

            nextButton = Button(emo, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                activebackground='white',
                                cursor='hand2', command=neww)
            nextButton.place(x=840, y=480)

        emotions_btn = Button(book, text='HUMAN EMOTIONS', font=('Arial', 20, 'bold'), bd=1,
                              bg='#ffffff', command=emo)
        emotions_btn.place(x=270, y=170)

        # PLANETS##############################################################

        # Initialize Pygame mixer
        pygame.mixer.init()

        def planets():
            planets = tk.Toplevel()
            planets.geometry('1060x595+250+100')
            planets.title('Teachify - For Kids')

            # Load the sunset image
            sunset_image = Image.open("COURSES_BG_ICON.jpg")
            sunset_image = sunset_image.resize((1050, 595))
            sunset_photo = ImageTk.PhotoImage(sunset_image)

            # Create a label to display the sunset image
            sunset_label = Label(planets, image=sunset_photo)
            sunset_label.image = sunset_photo
            sunset_label.place(x=0, y=0)

            numberslabel = Label(planets, text='PLANETS', font=('castellar', 29, 'bold'), fg='red3',
                                 bg='#fffdf0')
            numberslabel.place(x=410, y=35)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("earth.png")
            apple_image = apple_image.resize((250, 250))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("earth.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(planets, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=100, y=210)
            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("jupiter .png")
            apple_image = apple_image.resize((250, 250))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("jupiter.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(planets, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=400, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("mercury.png")
            apple_image = apple_image.resize((250, 250))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Define function to play audio on button click
            def play_apple_audio():
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.load("mercury.mp3")
                    pygame.mixer.music.play()

            apple_button = Button(planets, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                  command=play_apple_audio)
            apple_button.image = apple_photo
            apple_button.place(x=700, y=210)

            def back():
                planets.destroy()

            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
            back_button = Button(planets, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                 height=75, width=76)
            back_button.image = back_button_image
            back_button.place(x=60, y=465)

            def planets2():
                planets2 = tk.Toplevel()
                planets2.geometry('1060x595+250+100')
                planets2.title('Teachify - For Kids')

                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(planets2, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                numberslabel = Label(planets2, text='PLANETS', font=('castellar', 29, 'bold'), fg='red3',
                                     bg='#fffdf0')
                numberslabel.place(x=410, y=35)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("neptune.png")
                apple_image = apple_image.resize((250, 250))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("neptune.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(planets2, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=100, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("sun.png")
                apple_image = apple_image.resize((250, 250))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(planets2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=400, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("saturn.png")
                apple_image = apple_image.resize((250, 250))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("saturn.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(planets2, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=700, y=210)

                def back():
                    planets2.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(planets2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=75, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=465)

                def planets3():
                    planets3 = tk.Toplevel()
                    planets3.geometry('1060x595+250+100')
                    planets3.title('Teachify - For Kids')

                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(planets3, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    numberslabel = Label(planets3, text='PLANETS', font=('castellar', 29, 'bold'), fg='red3',
                                         bg='#fffdf0')
                    numberslabel.place(x=410, y=35)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("uranus.png")
                    apple_image = apple_image.resize((250, 250))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Define function to play audio on button click
                    def play_apple_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("uranus.mp3")
                            pygame.mixer.music.play()

                    apple_button = Button(planets3, image=apple_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0,
                                          command=play_apple_audio)
                    apple_button.image = apple_photo
                    apple_button.place(x=100, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("venus.png")
                    apple_image = apple_image.resize((250, 250))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Define function to play audio on button click
                    def play_apple_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("venus.mp3")
                            pygame.mixer.music.play()

                    apple_button = Button(planets3, image=apple_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0,
                                          command=play_apple_audio)
                    apple_button.image = apple_photo
                    apple_button.place(x=400, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("mars.png")
                    apple_image = apple_image.resize((250, 250))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Define function to play audio on button click
                    def play_apple_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("mars.mp3")
                            pygame.mixer.music.play()

                    apple_button = Button(planets3, image=apple_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0,
                                          command=play_apple_audio)
                    apple_button.image = apple_photo
                    apple_button.place(x=700, y=210)

                    def back():
                        planets3.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(planets3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=75, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=465)

                nextButton = Button(planets2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=planets3)
                nextButton.place(x=840, y=480)

                ##---------------------------------------------------

            nextButton = Button(planets, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                activebackground='white',
                                cursor='hand2', command=planets2)
            nextButton.place(x=840, y=480)

        planets_btn = Button(book, text='PLANETS', font=('Arial', 20, 'bold'), bd=1,
                             bg='#ffffff', command=planets)
        planets_btn.place(x=315, y=390)

        ## FRUITS #######################################################

        def fruits():
            fruits = tk.Toplevel()
            fruits.geometry('1060x595+250+100')
            fruits.title('Teachify - For Kids')
            # Load the sunset image
            sunset_image = Image.open("COURSES_BG_ICON.jpg")
            sunset_image = sunset_image.resize((1050, 595))
            sunset_photo = ImageTk.PhotoImage(sunset_image)

            # Create a label to display the sunset image
            sunset_label = Label(fruits, image=sunset_photo)
            sunset_label.image = sunset_photo
            sunset_label.place(x=0, y=0)

            booklabel = Label(fruits, text='FRUITS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            booklabel.place(x=430, y=35)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("banana.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(fruits, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=80, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("cherry.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(fruits, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=310, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("grapes .png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(fruits, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=540, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("kiwi.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(fruits, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=770, y=210)

            def back():
                fruits.destroy()

            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
            back_button = Button(fruits, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                 height=74, width=76)
            back_button.image = back_button_image
            back_button.place(x=60, y=460)

            def fruits2():
                fruits2 = tk.Toplevel()
                fruits2.geometry('1060x595+250+100')
                fruits2.title('Teachify - For Kids')
                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(fruits2, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                booklabel = Label(fruits2, text='FRUITS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                booklabel.place(x=430, y=35)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("orange.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(fruits2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=80, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("pear.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(fruits2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("peach.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(fruits2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("pineapple.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(fruits2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=770, y=210)

                def back():
                    fruits2.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(fruits2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def fruits3():
                    fruits3 = tk.Toplevel()
                    fruits3.geometry('1060x595+250+100')
                    fruits3.title('Teachify - For Kids')
                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(fruits3, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    booklabel = Label(fruits3, text='FRUITS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                    booklabel.place(x=430, y=35)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("pomogranate.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(fruits3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=80, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("pumpkin.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(fruits3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=310, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("raspberry.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(fruits3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=540, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("strawberry.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(fruits3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=770, y=210)

                    def back():
                        fruits3.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(fruits3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    def fruits4():
                        fruits4 = tk.Toplevel()
                        fruits4.geometry('1060x595+250+100')
                        fruits4.title('Teachify - For Kids')
                        # Load the sunset image
                        sunset_image = Image.open("COURSES_BG_ICON.jpg")
                        sunset_image = sunset_image.resize((1050, 595))
                        sunset_photo = ImageTk.PhotoImage(sunset_image)

                        # Create a label to display the sunset image
                        sunset_label = Label(fruits4, image=sunset_photo)
                        sunset_label.image = sunset_photo
                        sunset_label.place(x=0, y=0)

                        booklabel = Label(fruits4, text='FRUITS', font=('castellar', 29, 'bold'), fg='red3',
                                          bg='#fffdf0')
                        booklabel.place(x=430, y=35)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("plum.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(fruits4, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=80, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("tomato.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(fruits4, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=310, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("watermelon.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(fruits4, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=540, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("apple.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(fruits4, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=770, y=210)

                        def back():
                            fruits4.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(fruits4, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                             height=74, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=460)

                    nextButton = Button(fruits3, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=fruits4)
                    nextButton.place(x=840, y=480)

                nextButton = Button(fruits2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=fruits3)
                nextButton.place(x=840, y=480)

            nextButton = Button(fruits, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                activebackground='white',
                                cursor='hand2', command=fruits2)
            nextButton.place(x=840, y=480)

        fruits_btn = Button(book, text='FRUITS', font=('Arial', 20, 'bold'), bd=1,
                            bg='#ffffff', command=fruits)
        fruits_btn.place(x=220, y=240)

        ## VEGETABLES #######################################################

        def vegetables():
            vegetables = tk.Toplevel()
            vegetables.geometry('1060x595+250+100')
            vegetables.title('Teachify - For Kids')
            # Load the sunset image
            sunset_image = Image.open("COURSES_BG_ICON.jpg")
            sunset_image = sunset_image.resize((1050, 595))
            sunset_photo = ImageTk.PhotoImage(sunset_image)

            # Create a label to display the sunset image
            sunset_label = Label(vegetables, image=sunset_photo)
            sunset_label.image = sunset_photo
            sunset_label.place(x=0, y=0)

            booklabel = Label(vegetables, text='VEGETABLES', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            booklabel.place(x=390, y=35)

            ##---------------------------------------------------

            apple_image = Image.open("onions.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(vegetables, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=80, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("tomato.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(vegetables, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=310, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("carrots.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(vegetables, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=540, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("cauliflower.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(vegetables, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=770, y=210)

            def back():
                vegetables.destroy()

            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
            back_button = Button(vegetables, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                 height=74, width=76)
            back_button.image = back_button_image
            back_button.place(x=60, y=460)

            def vegetables2():
                vegetables2 = tk.Toplevel()
                vegetables2.geometry('1060x595+250+100')
                vegetables2.title('Teachify - For Kids')
                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(vegetables2, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                booklabel = Label(vegetables2, text='VEGETABLES', font=('castellar', 29, 'bold'), fg='red3',
                                  bg='#fffdf0')
                booklabel.place(x=390, y=35)

                ##---------------------------------------------------

                apple_image = Image.open("corn.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(vegetables2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=80, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("cucumber.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(vegetables2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("eggplant.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(vegetables2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("garlic.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(vegetables2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=770, y=210)

                def back():
                    vegetables2.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(vegetables2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def vegetables3():
                    vegetables3 = tk.Toplevel()
                    vegetables3.geometry('1060x595+250+100')
                    vegetables3.title('Teachify - For Kids')
                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(vegetables3, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    booklabel = Label(vegetables3, text='VEGETABLES', font=('castellar', 29, 'bold'), fg='red3',
                                      bg='#fffdf0')
                    booklabel.place(x=390, y=35)

                    ##---------------------------------------------------

                    apple_image = Image.open("peas.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(vegetables3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=80, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("potato.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(vegetables3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=310, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("spinach.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(vegetables3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=540, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("mushroom.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(vegetables3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=770, y=210)

                    def back():
                        vegetables3.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(vegetables3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                nextButton = Button(vegetables2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=vegetables3)
                nextButton.place(x=840, y=480)

            nextButton = Button(vegetables, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                activebackground='white',
                                cursor='hand2', command=vegetables2)
            nextButton.place(x=840, y=480)

        vegetables_btn = Button(book, text='VEGETABLES', font=('Arial', 20, 'bold'), bd=1,
                                bg='#ffffff', command=vegetables)
        vegetables_btn.place(x=370, y=240)

        ## CLIMATE #######################################################

        def climate():
            climate = tk.Toplevel()
            climate.geometry('1060x595+250+100')
            climate.title('Teachify - For Kids')
            # Load the sunset image
            sunset_image = Image.open("COURSES_BG_ICON.jpg")
            sunset_image = sunset_image.resize((1050, 595))
            sunset_photo = ImageTk.PhotoImage(sunset_image)

            # Create a label to display the sunset image
            sunset_label = Label(climate, image=sunset_photo)
            sunset_label.image = sunset_photo
            sunset_label.place(x=0, y=0)

            booklabel = Label(climate, text='CLIMATE', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            booklabel.place(x=390, y=35)

            ##---------------------------------------------------

            apple_image = Image.open("cloudy.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(climate, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=80, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("sunny.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(climate, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=310, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("rainy.png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(climate, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=540, y=210)

            ##---------------------------------------------------

            # Load the apple image
            apple_image = Image.open("lightning .png")
            apple_image = apple_image.resize((200, 200))
            apple_photo = ImageTk.PhotoImage(apple_image)

            # Create a label to display the apple image
            apple_label = Label(climate, image=apple_photo, bg='white')
            apple_label.image = apple_photo
            apple_label.place(x=770, y=210)

            def back():
                climate.destroy()

            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
            back_button = Button(climate, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                 height=74, width=76)
            back_button.image = back_button_image
            back_button.place(x=60, y=460)

            def climate2():
                climate2 = tk.Toplevel()
                climate2.geometry('1060x595+250+100')
                climate2.title('Teachify - For Kids')
                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(climate2, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                booklabel = Label(climate2, text='CLIMATE', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                booklabel.place(x=390, y=35)

                ##---------------------------------------------------

                apple_image = Image.open("hot.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(climate2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=80, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("cold.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(climate2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("freezing.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(climate2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("sunny.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(climate2, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=770, y=210)

                def back():
                    climate2.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(climate2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def climate3():
                    climate3 = tk.Toplevel()
                    climate3.geometry('1060x595+250+100')
                    climate3.title('Teachify - For Kids')
                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(climate3, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    booklabel = Label(climate3, text='CLIMATE', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                    booklabel.place(x=390, y=35)

                    ##---------------------------------------------------

                    apple_image = Image.open("foggy.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(climate3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=180, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("windy.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(climate3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=410, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("stormy.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(climate3, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=500, y=210)

                    def back():
                        climate3.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(climate3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    ##---------------------------------------------------

                nextButton = Button(climate2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=climate3)
                nextButton.place(x=840, y=480)

            nextButton = Button(climate, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                activebackground='white',
                                cursor='hand2', command=climate2)
            nextButton.place(x=840, y=480)

        climate_btn = Button(book, text='CLIMATE', font=('Arial', 20, 'bold'), bd=1,
                             bg='#ffffff', command=climate)
        climate_btn.place(x=320, y=320)

    picturebk_btn = Button(three_six, text='PICTURE BOOK', font=('Arial', 20, 'bold'), bd=1, command=book,
                           bg='#efd2aa')
    picturebk_btn.place(x=415, y=385)


# ============================================= CREATE 3-6 YEARS BUTTON ====================================================#
btn3_6y = Button(root, text='3-6 YEARS', font=('Arial', 20, 'bold'), bd=0, relief=GROOVE, fg='white', bg='#1e7922',
                 command=three_six_page)
btn3_6y.place(x=450, y=200)


# =================================================CREATE 7-11 YEARS BUTTON======================================================#
def seven_eleven_page():
    seven_eleven = tk.Toplevel()
    seven_eleven.geometry('1060x595+250+100')
    seven_eleven.title('Teachify - For Kids')

    # Create a frame to hold the image
    image_frame = Frame(seven_eleven, bg='white', width=500, height=500)
    image_frame.pack(side=LEFT, padx=0, pady=0)

    # Load the image
    bg_image = Image.open("bg3.png")
    bg_image = bg_image.resize((1050, 595))
    photo = ImageTk.PhotoImage(bg_image)

    # Create a label to display the image
    image_label = Label(image_frame, image=photo, bg='white')
    image_label.image = photo  # to prevent garbage collection
    image_label.pack()

    def back():
        seven_eleven.destroy()

    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
    back_button = Button(seven_eleven, image=back_button_image, bd=0, bg='#efd2aa', command=back,
                         height=50, width=50)
    back_button.image = back_button_image
    back_button.place(x=275, y=400)

    def courses_page1():
        courses = tk.Toplevel()
        courses.geometry('1060x595+250+100')
        courses.title('Teachify - For Kids')

        # Create a frame to hold the image
        image_frame = Frame(courses, bg='white', width=500, height=500)
        image_frame.pack(side=LEFT, padx=0, pady=0)

        # Load the  image
        bg_image = Image.open("new_bg.png")
        bg_image = bg_image.resize((1050, 595))
        photo = ImageTk.PhotoImage(bg_image)

        # Create a label to display the image
        image_label = Label(image_frame, image=photo, bg='white')
        image_label.image = photo
        image_label.pack()

        courseslabel = Label(courses, text='COURSES', font=('castellar', 29, 'bold'), fg='red3', bg='#ffffff')
        courseslabel.place(x=310, y=95)

        def back():
            courses.destroy()

        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
        back_button = Button(courses, image=back_button_image, bd=0, command=back, bg='#ffffff',
                             height=74, width=76)
        back_button.image = back_button_image
        back_button.place(x=90, y=380)

        # -----------CREATE COURSE BUTTONS-----------------------

        # -------------------ALPHABETS---------------


        def alphabets():
            alphabets = tk.Toplevel()
            alphabets.geometry('1060x595+250+100')
            alphabets.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(alphabets, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            alphabetslabel = Label(alphabets, text='ALPHABETS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            alphabetslabel.place(x=395, y=35)

            def back():
                alphabets.destroy()

            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
            back_button = Button(alphabets, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                 height=74, width=76)
            back_button.image = back_button_image
            back_button.place(x=60, y=460)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            # Define function for the 'a' window
            def a():
                a = Toplevel()
                a.geometry('1060x595+250+100')
                a.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(a, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(a, text='ALPHABET - A', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                A_Label = Label(a, text='A', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                A_Label.place(x=120, y=230)
                A_Label = Label(a, text='a', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                A_Label.place(x=250, y=285)

                # Load the apple image
                apple_image = Image.open("a.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("a.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(a, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                # Create a button with image next1.png
                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(a, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [a.destroy(), b()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

            # Create a button for 'A' in the main window
            btn_A = Button(alphabets, text='A', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, bd=1, command=a)
            btn_A.place(x=75, y=180)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def b():
                b = tk.Toplevel()
                b.geometry('1060x595+250+100')
                b.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(b, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(b, text='ALPHABET - B', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                B_Label = Label(b, text='B', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                B_Label.place(x=120, y=230)
                B_Label = Label(b, text='b', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                B_Label.place(x=250, y=285)

                # Load the apple image
                apple_image = Image.open("bat.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("b.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(b, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(b, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [b.destroy(), c()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(b, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [b.destroy(), a()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_B = Button(alphabets, text='B', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=b)
            btn_B.place(x=165, y=180)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def c():
                c = tk.Toplevel()
                c.geometry('1060x595+250+100')
                c.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(c, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(c, text='ALPHABET - C', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                C_Label = Label(c, text='C', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                C_Label.place(x=120, y=230)
                C_Label = Label(c, text='c', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                C_Label.place(x=250, y=285)

                # Load the apple image
                apple_image = Image.open("c.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("c.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(c, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(c, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [c.destroy(), d()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(c, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [c.destroy(), b()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_C = Button(alphabets, text='C', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=c)
            btn_C.place(x=255, y=180)

            # ***************************************
            # Initialize Pygame mixer
            pygame.mixer.init()

            def d():
                D = tk.Toplevel()
                D.geometry('1060x595+250+100')
                D.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(D, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(D, text='ALPHABET - D', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                D_Label = Label(D, text='D', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                D_Label.place(x=120, y=230)
                D_Label = Label(D, text='d', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                D_Label.place(x=250, y=285)

                # Load the apple image
                apple_image = Image.open("d.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("d.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(D, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(D, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [D.destroy(), E()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(D, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [D.destroy(), c()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_D = Button(alphabets, text='D', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=d)
            btn_D.place(x=348, y=180)

            # ***************************************
            # Initialize Pygame mixer
            pygame.mixer.init()

            def E():
                E = tk.Toplevel()
                E.geometry('1060x595+250+100')
                E.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(E, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(E, text='ALPHABET - E', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                E_Label = Label(E, text='E', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                E_Label.place(x=120, y=230)
                E_Label = Label(E, text='e', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                E_Label.place(x=250, y=285)

                # Load the apple image
                apple_image = Image.open("e.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("e.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(E, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(E, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [E.destroy(), F()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(E, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [E.destroy(), d()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_E = Button(alphabets, text='E', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=E)
            btn_E.place(x=435, y=180)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def F():
                F = tk.Toplevel()
                F.geometry('1060x595+250+100')
                F.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(F, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(F, text='ALPHABET - F', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                F_Label = Label(F, text='F', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                F_Label.place(x=120, y=230)
                F_Label = Label(F, text='f', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                F_Label.place(x=230, y=300)

                # Load the apple image
                apple_image = Image.open("frog.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("f.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(F, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(F, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [F.destroy(), G()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(F, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [F.destroy(), E()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_F = Button(alphabets, text='F', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=F)
            btn_F.place(x=525, y=180)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def G():
                G = tk.Toplevel()
                G.geometry('1060x595+250+100')
                G.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(G, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(G, text='ALPHABET - G', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                G_Label = Label(G, text='G', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                G_Label.place(x=120, y=230)
                G_Label = Label(G, text='g', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                G_Label.place(x=250, y=285)

                # Load the apple image
                apple_image = Image.open("goat.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("g.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(G, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(G, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [G.destroy(), H()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(G, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [G.destroy(), F()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_G = Button(alphabets, text='G', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=G)
            btn_G.place(x=615, y=180)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def H():
                H = tk.Toplevel()
                H.geometry('1060x595+250+100')
                H.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(H, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(H, text='ALPHABET - H', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                H_Label = Label(H, text='H', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                H_Label.place(x=120, y=230)
                H_Label = Label(H, text='h', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                H_Label.place(x=250, y=290)

                # Load the apple image
                apple_image = Image.open("h for hat.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("h.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(H, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)
                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(H, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [H.destroy(), I()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(H, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [H.destroy(), G()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_H = Button(alphabets, text='H', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=H)
            btn_H.place(x=705, y=180)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def I():
                I = tk.Toplevel()
                I.geometry('1060x595+250+100')
                I.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(I, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(I, text='ALPHABET - I', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                I_Label = Label(I, text='I', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                I_Label.place(x=120, y=230)
                I_Label = Label(I, text='i', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                I_Label.place(x=250, y=285)

                # Load the apple image
                apple_image = Image.open("insect.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("i.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(I, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(I, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [I.destroy(), j()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(I, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [I.destroy(), H()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_i = Button(alphabets, text='I', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=I)
            btn_i.place(x=795, y=180)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def j():
                j = tk.Toplevel()
                j.geometry('1060x595+250+100')
                j.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(j, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(j, text='ALPHABET - J', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                j_Label = Label(j, text='J', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                j_Label.place(x=120, y=230)
                j_Label = Label(j, text='j', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                j_Label.place(x=230, y=285)

                # Load the apple image
                apple_image = Image.open("j.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("j.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(j, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(j, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [j.destroy(), K()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(j, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [j.destroy(), I()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_J = Button(alphabets, text='J', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=j)
            btn_J.place(x=885, y=180)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def K():
                K = tk.Toplevel()
                K.geometry('1060x595+250+100')
                K.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(K, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(K, text='ALPHABET - K', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                K_Label = Label(K, text='K', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                K_Label.place(x=120, y=230)
                K_Label = Label(K, text='k', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                K_Label.place(x=255, y=290)

                # Load the apple image
                apple_image = Image.open("kite.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("K.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(K, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(K, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [K.destroy(), L()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(K, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [K.destroy(), j()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_K = Button(alphabets, text='K', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=K)
            btn_K.place(x=75, y=300)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def L():
                L = tk.Toplevel()
                L.geometry('1060x595+250+100')
                L.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(L, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(L, text='ALPHABET - L', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                L_Label = Label(L, text='L', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                L_Label.place(x=120, y=230)
                L_Label = Label(L, text='l', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                L_Label.place(x=245, y=290)

                # Load the apple image
                apple_image = Image.open("leaf.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("l.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(L, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(L, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [L.destroy(), M()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(L, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [L.destroy(), K()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_L = Button(alphabets, text='L', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=L)
            btn_L.place(x=165, y=300)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def M():
                M = tk.Toplevel()
                M.geometry('1060x595+250+100')
                M.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(M, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(M, text='ALPHABET - M', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                M_Label = Label(M, text='M', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                M_Label.place(x=120, y=230)
                M_Label = Label(M, text='m', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                M_Label.place(x=260, y=290)

                # Load the apple image
                apple_image = Image.open("monkey.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("m.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(M, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(M, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [M.destroy(), N()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(M, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [M.destroy(), L()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_M = Button(alphabets, text='M', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=M)
            btn_M.place(x=255, y=300)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def N():
                N = tk.Toplevel()
                N.geometry('1060x595+250+100')
                N.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(N, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(N, text='ALPHABET - N', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                N_Label = Label(N, text='N', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                N_Label.place(x=120, y=230)
                N_Label = Label(N, text='n', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                N_Label.place(x=245, y=290)

                # Load the apple image
                apple_image = Image.open("n.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("n.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(N, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(N, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [N.destroy(), O()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(N, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [N.destroy(), M()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_N = Button(alphabets, text='N', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=N)
            btn_N.place(x=348, y=300)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def O():
                O = tk.Toplevel()
                O.geometry('1060x595+250+100')
                O.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(O, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(O, text='ALPHABET - O', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                O_Label = Label(O, text='O', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                O_Label.place(x=120, y=230)
                O_Label = Label(O, text='o', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                O_Label.place(x=260, y=290)

                # Load the apple image
                apple_image = Image.open("ocean.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("o.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(O, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(O, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [O.destroy(), P()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(O, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [O.destroy(), N()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_O = Button(alphabets, text='O', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=O)
            btn_O.place(x=435, y=300)

            # ***************************************
            # Initialize Pygame mixer
            pygame.mixer.init()

            def P():
                P = tk.Toplevel()
                P.geometry('1060x595+250+100')
                P.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(P, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(P, text='ALPHABET - P', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                P_Label = Label(P, text='P', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                P_Label.place(x=120, y=230)
                P_Label = Label(P, text='p', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                P_Label.place(x=235, y=290)

                # Load the apple image
                apple_image = Image.open("plum.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("p.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(P, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(P, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [P.destroy(), Q()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(P, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [P.destroy(), O()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_P = Button(alphabets, text='P', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=P)
            btn_P.place(x=525, y=300)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def Q():
                Q = tk.Toplevel()
                Q.geometry('1060x595+250+100')
                Q.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(Q, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(Q, text='ALPHABET - Q', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                Q_Label = Label(Q, text='Q', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                Q_Label.place(x=120, y=230)
                Q_Label = Label(Q, text='q', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                Q_Label.place(x=260, y=290)

                # Load the apple image
                apple_image = Image.open("queen.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("q.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(Q, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(Q, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [Q.destroy(), R()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(Q, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [Q.destroy(), P()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_Q = Button(alphabets, text='Q', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=Q)
            btn_Q.place(x=615, y=300)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def R():
                R = tk.Toplevel()
                R.geometry('1060x595+250+100')
                R.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(R, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(R, text='ALPHABET - R', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                R_Label = Label(R, text='R', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                R_Label.place(x=120, y=230)
                R_Label = Label(R, text='r', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                R_Label.place(x=260, y=290)

                # Load the apple image
                apple_image = Image.open("rat.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("r.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(R, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(R, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [R.destroy(), S()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(R, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [R.destroy(), Q()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_R = Button(alphabets, text='R', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=R)
            btn_R.place(x=705, y=300)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def S():
                S = tk.Toplevel()
                S.geometry('1060x595+250+100')
                S.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(S, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(S, text='ALPHABET - S', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                S_Label = Label(S, text='S', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                S_Label.place(x=120, y=230)
                S_Label = Label(S, text='s', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                S_Label.place(x=245, y=290)

                # Load the apple image
                apple_image = Image.open("s.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("s.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(S, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(S, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [S.destroy(), T()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(S, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [S.destroy(), R()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_S = Button(alphabets, text='S', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=S)
            btn_S.place(x=795, y=300)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def T():
                T = tk.Toplevel()
                T.geometry('1060x595+250+100')
                T.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(T, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(T, text='ALPHABET - T', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                T_Label = Label(T, text='T', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                T_Label.place(x=120, y=230)
                T_Label = Label(T, text='t', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                T_Label.place(x=220, y=290)

                # Load the apple image
                apple_image = Image.open("tap.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("t.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(T, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(T, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [T.destroy(), U()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(T, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [T.destroy(), S()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_T = Button(alphabets, text='T', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=T)
            btn_T.place(x=885, y=300)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def U():
                U = tk.Toplevel()
                U.geometry('1060x595+250+100')
                U.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(U, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(U, text='ALPHABET - U', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                U_Label = Label(U, text='U', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                U_Label.place(x=120, y=230)
                U_Label = Label(U, text='u', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                U_Label.place(x=245, y=290)

                # Load the apple image
                apple_image = Image.open("u.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("u.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(U, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(U, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [U.destroy(), V()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(U, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [U.destroy(), T()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_U = Button(alphabets, text='U', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=U)
            btn_U.place(x=255, y=420)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def V():
                V = tk.Toplevel()
                V.geometry('1060x595+250+100')
                V.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(V, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(V, text='ALPHABET - V', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                V_Label = Label(V, text='V', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                V_Label.place(x=120, y=230)
                V_Label = Label(V, text='v', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                V_Label.place(x=240, y=290)

                # Load the apple image
                apple_image = Image.open("v.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("v.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(V, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(V, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [V.destroy(), W()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(V, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [V.destroy(), U()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_V = Button(alphabets, text='V', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=V)
            btn_V.place(x=348, y=420)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def W():
                W = tk.Toplevel()
                W.geometry('1060x595+250+100')
                W.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(W, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(W, text='ALPHABET - W', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                W_Label = Label(W, text='W', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                W_Label.place(x=120, y=230)
                W_Label = Label(W, text='w', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                W_Label.place(x=285, y=290)

                # Load the apple image
                apple_image = Image.open("well.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("w.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(W, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(W, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [W.destroy(), X()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(W, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [W.destroy(), V()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_W = Button(alphabets, text='W', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=W)
            btn_W.place(x=435, y=420)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def X():
                X = tk.Toplevel()
                X.geometry('1060x595+250+100')
                X.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(X, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(X, text='ALPHABET - V', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                X_Label = Label(X, text='X', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                X_Label.place(x=120, y=230)
                X_Label = Label(X, text='x', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                X_Label.place(x=240, y=290)

                # Load the apple image
                apple_image = Image.open("x.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("x.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(X, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(X, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [X.destroy(), Y()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(X, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [X.destroy(), W()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_X = Button(alphabets, text='X', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=X)
            btn_X.place(x=525, y=420)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def Y():
                Y = tk.Toplevel()
                Y.geometry('1060x595+250+100')
                Y.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(Y, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(Y, text='ALPHABET - Y', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                # Load the apple image
                apple_image = Image.open("y.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("y.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(Y, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                Y_Label = Label(Y, text='Y', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                Y_Label.place(x=120, y=230)
                Y_Label = Label(Y, text='y', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                Y_Label.place(x=225, y=290)

                next_button_image = ImageTk.PhotoImage(Image.open("nexxt.png").resize((50, 50)))
                next_button = Button(Y, image=next_button_image, bg='#fff7ea', bd=0, command=lambda: [Y.destroy(), Z()])
                next_button.image = next_button_image
                next_button.place(x=930, y=460)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(Y, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [Y.destroy(), X()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_Y = Button(alphabets, text='Y', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=Y)
            btn_Y.place(x=615, y=420)

            # ***************************************

            # Initialize Pygame mixer
            pygame.mixer.init()

            def Z():
                Z = tk.Toplevel()
                Z.geometry('1060x595+250+100')
                Z.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(Z, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                alphabetslabel = Label(Z, text='ALPHABET - Z', font=('castellar', 29, 'bold'), fg='red3',
                                       bg='#fffdf0')
                alphabetslabel.place(x=380, y=35)

                Z_Label = Label(Z, text='Z', font=('Arial', 130, 'bold'), fg='black', bg='#fff7ea')
                Z_Label.place(x=120, y=230)
                Z_Label = Label(Z, text='z', font=('Arial', 80, 'bold'), fg='red', bg='#fff7ea')
                Z_Label.place(x=240, y=290)

                # Load the apple image
                apple_image = Image.open("zz.png")
                apple_image = apple_image.resize((300, 300))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("z.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(Z, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=600, y=180)

                back_button_image = ImageTk.PhotoImage(Image.open("backk.png").resize((50, 50)))
                back_button = Button(Z, image=back_button_image, bg='#fff7ea', bd=0, command=lambda: [Z.destroy(), Y()])
                back_button.image = back_button_image
                back_button.place(x=110, y=460)

            btn_Z = Button(alphabets, text='Z', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0', height=1,
                           width=2, command=Z)
            btn_Z.place(x=705, y=420)

        alphabets_btn = Button(courses, font=('Arial', 20, 'bold'), text="Alphabets", bg='#ffffff', bd=0.5,
                               command=alphabets)
        alphabets_btn.place(x=325, y=230)

        # -----------------------MATHS----------------------------------
        def maths():
            maths = tk.Toplevel()
            maths.geometry('1060x595+250+100')
            maths.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(maths, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("new_bg.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            mathslabel = Label(maths, text='MATHS', font=('castellar', 29, 'bold'), fg='red3', bg='#ffffff')
            mathslabel.place(x=320, y=110)

            def back():
                maths.destroy()

            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
            back_button = Button(maths, image=back_button_image, bd=0, command=back, bg='#ffffff',
                                 height=50, width=50)
            back_button.image = back_button_image
            back_button.place(x=90, y=410)

            def tables_pg():
                tables = tk.Toplevel()
                tables.geometry('1060x595+250+100')
                tables.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(tables, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                tb_label = Label(tables, text='MATHS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                tb_label.place(x=420, y=35)

                def table_one_pg():
                    tab_lab1 = Label(tables, text="1   x   1   =   1      ", font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    tab_lab1.place(x=120, y=170)

                    tab_lab2 = Label(tables, text="1   x   2   =   2      ", font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    tab_lab2.place(x=120, y=240)

                    tab_lab3 = Label(tables, text="1   x   3   =   3      ", font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    tab_lab3.place(x=120, y=310)

                    tab_lab4 = Label(tables, text="1   x   4   =   4      ", font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    tab_lab4.place(x=120, y=380)

                    tab_lab5 = Label(tables, text="1   x   5   =   5      ", font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    tab_lab5.place(x=120, y=450)

                    tab_lab6 = Label(tables, text="1   x   6   =   6    ", font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    tab_lab6.place(x=620, y=170)

                    tab_lab7 = Label(tables, text="1   x   7   =   7    ", font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    tab_lab7.place(x=620, y=240)

                    tab_lab8 = Label(tables, text="1   x   8   =   8    ", font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    tab_lab8.place(x=620, y=310)

                    tab_lab9 = Label(tables, text="1   x   9   =   9    ", font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    tab_lab9.place(x=620, y=380)

                    tab_lab10 = Label(tables, text="1   x   10   = 10  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab10.place(x=620, y=450)

                table_one_btn = Button(tables, text='1', font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                       command=table_one_pg)
                table_one_btn.place(x=270, y=510)

                def table_two_pg():
                    tab_lab11 = Label(tables, text="2   x   1   =   2      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab11.place(x=120, y=170)

                    tab_lab12 = Label(tables, text="2   x   2   =   4      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab12.place(x=120, y=240)

                    tab_lab13 = Label(tables, text="2   x   3   =   6      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab13.place(x=120, y=310)

                    tab_lab14 = Label(tables, text="2   x   4   =   8      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab14.place(x=120, y=380)

                    tab_lab15 = Label(tables, text="2   x   5   =   10      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab15.place(x=120, y=450)

                    tab_lab16 = Label(tables, text="2   x   6   =   12  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab16.place(x=620, y=170)

                    tab_lab17 = Label(tables, text="2   x   7   =   14  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab17.place(x=620, y=240)

                    tab_lab18 = Label(tables, text="2   x   8   =   16  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab18.place(x=620, y=310)

                    tab_lab19 = Label(tables, text="2   x   9   =   18  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab19.place(x=620, y=380)

                    tab_lab20 = Label(tables, text="2   x   10   =  20 ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab20.place(x=620, y=450)

                table_two_btn = Button(tables, text='2', font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                       command=table_two_pg)
                table_two_btn.place(x=300, y=510)

                def table_three_pg():
                    tab_lab21 = Label(tables, text="3   x   1   =   3      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab21.place(x=120, y=170)

                    tab_lab22 = Label(tables, text="3   x   2   =   6      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab22.place(x=120, y=240)

                    tab_lab23 = Label(tables, text="3   x   3   =   9      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab23.place(x=120, y=310)

                    tab_lab24 = Label(tables, text="3   x   4   =   12     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab24.place(x=120, y=380)

                    tab_lab25 = Label(tables, text="3   x   5   =   15     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab25.place(x=120, y=450)

                    tab_lab26 = Label(tables, text="3   x   6   =   18   ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab26.place(x=620, y=170)

                    tab_lab27 = Label(tables, text="3   x   7   =   21  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab27.place(x=620, y=240)

                    tab_lab28 = Label(tables, text="3   x   8   =   24  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab28.place(x=620, y=310)

                    tab_lab29 = Label(tables, text="3   x   9   =   27  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab29.place(x=620, y=380)

                    tab_lab30 = Label(tables, text="3   x   10  =  30  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab30.place(x=620, y=450)

                table_three_btn = Button(tables, text='3', font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                         command=table_three_pg)
                table_three_btn.place(x=330, y=510)

                def table_four_pg():
                    tab_lab31 = Label(tables, text="4   x   1   =   4      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab31.place(x=120, y=170)

                    tab_lab32 = Label(tables, text="4   x   2   =   8      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab32.place(x=120, y=240)

                    tab_lab33 = Label(tables, text="4   x   3   =   12     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab33.place(x=120, y=310)

                    tab_lab34 = Label(tables, text="4   x   4   =   16     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab34.place(x=120, y=380)

                    tab_lab35 = Label(tables, text="4   x   5   =   20     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab35.place(x=120, y=450)

                    tab_lab36 = Label(tables, text="4   x   6   =   24  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab36.place(x=620, y=170)

                    tab_lab37 = Label(tables, text="4   x   7   =   28  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab37.place(x=620, y=240)

                    tab_lab38 = Label(tables, text="4   x   8   =   32  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab38.place(x=620, y=310)

                    tab_lab39 = Label(tables, text="4   x   9   =   36  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab39.place(x=620, y=380)

                    tab_lab40 = Label(tables, text="4   x   10  =  40  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab40.place(x=620, y=450)

                table_four_btn = Button(tables, text='4', font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                        command=table_four_pg)
                table_four_btn.place(x=360, y=510)

                def table_five_pg():
                    tab_lab41 = Label(tables, text="5   x   1   =   5     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab41.place(x=120, y=170)

                    tab_lab42 = Label(tables, text="5   x   2   =   10     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab42.place(x=120, y=240)

                    tab_lab43 = Label(tables, text="5   x   3   =   15     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab43.place(x=120, y=310)

                    tab_lab44 = Label(tables, text="5   x   4   =   20      ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab44.place(x=120, y=380)

                    tab_lab45 = Label(tables, text="5   x   5   =   25     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab45.place(x=120, y=450)

                    tab_lab46 = Label(tables, text="5   x   6   =   30  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab46.place(x=620, y=170)

                    tab_lab47 = Label(tables, text="5   x   7   =   35  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab47.place(x=620, y=240)

                    tab_lab48 = Label(tables, text="5   x   8   =   40  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab48.place(x=620, y=310)

                    tab_lab49 = Label(tables, text="5   x   9   =   45  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab49.place(x=620, y=380)

                    tab_lab50 = Label(tables, text="5   x   10  =  50  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab50.place(x=620, y=450)

                table_five_btn = Button(tables, text='5', font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                        command=table_five_pg)
                table_five_btn.place(x=390, y=510)

                def table_six_pg():
                    tab_lab51 = Label(tables, text="6   x   1   =   6     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab51.place(x=120, y=170)

                    tab_lab52 = Label(tables, text="6   x   2   =   12    ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab52.place(x=120, y=240)

                    tab_lab53 = Label(tables, text="6   x   3   =   18    ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab53.place(x=120, y=310)

                    tab_lab54 = Label(tables, text="6   x   4   =   24     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab54.place(x=120, y=380)

                    tab_lab55 = Label(tables, text="6   x   5   =   30     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab55.place(x=120, y=450)

                    tab_lab56 = Label(tables, text="6   x   6   =   36 ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab56.place(x=620, y=170)

                    tab_lab57 = Label(tables, text="6   x   7   =   42  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab57.place(x=620, y=240)

                    tab_lab58 = Label(tables, text="6   x   8   =   48  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab58.place(x=620, y=310)

                    tab_lab59 = Label(tables, text="6   x   9   =   54  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab59.place(x=620, y=380)

                    tab_lab60 = Label(tables, text="6   x  10  =   60  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab60.place(x=620, y=450)

                table_six_btn = Button(tables, text="6", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                       command=table_six_pg)
                table_six_btn.place(x=420, y=510)

                def table_seven_pg():
                    tab_lab61 = Label(tables, text="7   x   1   =   7     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab61.place(x=120, y=170)

                    tab_lab62 = Label(tables, text="7   x   2   =   14     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab62.place(x=120, y=240)

                    tab_lab63 = Label(tables, text="7   x   3   =   21     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab63.place(x=120, y=310)

                    tab_lab64 = Label(tables, text="7   x   4   =   28     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab64.place(x=120, y=380)

                    tab_lab65 = Label(tables, text="7   x   5   =   35     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab65.place(x=120, y=450)

                    tab_lab66 = Label(tables, text="7   x   6   =   42  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab66.place(x=620, y=170)

                    tab_lab67 = Label(tables, text="7   x   7   =   49  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab67.place(x=620, y=240)

                    tab_lab68 = Label(tables, text="7   x   8   =   56  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab68.place(x=620, y=310)

                    tab_lab69 = Label(tables, text="7   x   9   =   63  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab69.place(x=620, y=380)

                    tab_lab70 = Label(tables, text="7   x   10  =  70  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab70.place(x=620, y=450)

                table_seven_btn = Button(tables, text="7", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                         command=table_seven_pg)
                table_seven_btn.place(x=450, y=510)

                def table_eight_pg():
                    tab_lab71 = Label(tables, text="8   x   1   =   8     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab71.place(x=120, y=170)

                    tab_lab72 = Label(tables, text="8   x   2   =   16     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab72.place(x=120, y=240)

                    tab_lab73 = Label(tables, text="8   x   3   =   24     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab73.place(x=120, y=310)

                    tab_lab74 = Label(tables, text="8   x   4   =   32     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab74.place(x=120, y=380)

                    tab_lab75 = Label(tables, text="8   x   5   =   40     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab75.place(x=120, y=450)

                    tab_lab76 = Label(tables, text="8   x   6   =   48  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab76.place(x=620, y=170)

                    tab_lab77 = Label(tables, text="8   x   7   =   56  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab77.place(x=620, y=240)

                    tab_lab78 = Label(tables, text="8   x   8   =   64  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab78.place(x=620, y=310)

                    tab_lab79 = Label(tables, text="8   x   9   =   72  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab79.place(x=620, y=380)

                    tab_lab80 = Label(tables, text="8   x   10  =  80  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab80.place(x=620, y=450)

                table_eight_btn = Button(tables, text="8", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                         command=table_eight_pg)
                table_eight_btn.place(x=480, y=510)

                def table_nineth_pg():
                    tab_lab81 = Label(tables, text="9   x   1   =   5     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab81.place(x=120, y=170)

                    tab_lab82 = Label(tables, text="9   x   2   =   18     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab82.place(x=120, y=240)

                    tab_lab83 = Label(tables, text="9   x   3   =   27     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab83.place(x=120, y=310)

                    tab_lab84 = Label(tables, text="9   x   4   =   36     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab84.place(x=120, y=380)

                    tab_lab85 = Label(tables, text="9   x   5   =   45     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab85.place(x=120, y=450)

                    tab_lab86 = Label(tables, text="9   x   6   =   54  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab86.place(x=620, y=170)

                    tab_lab87 = Label(tables, text="9   x   7   =   63  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab87.place(x=620, y=240)

                    tab_lab88 = Label(tables, text="9   x   8   =   72  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab88.place(x=620, y=310)

                    tab_lab89 = Label(tables, text="9   x   9   =   81  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab89.place(x=620, y=380)

                    tab_lab90 = Label(tables, text="9   x   10  =  90  ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab90.place(x=620, y=450)

                table_nineth_btn = Button(tables, text="9", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                          command=table_nineth_pg)
                table_nineth_btn.place(x=510, y=510)

                def table_tenth_pg():
                    tab_lab91 = Label(tables, text="10   x   1   =   10   ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab91.place(x=120, y=170)

                    tab_lab92 = Label(tables, text="10   x   2   =   20   ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab92.place(x=120, y=240)

                    tab_lab93 = Label(tables, text="10   x   3   =   30   ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab93.place(x=120, y=310)

                    tab_lab94 = Label(tables, text="10   x   4   =   40     ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab94.place(x=120, y=380)

                    tab_lab95 = Label(tables, text="10   x   5   =   50    ", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab95.place(x=120, y=450)

                    tab_lab96 = Label(tables, text="10   x   6   =   60", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab96.place(x=620, y=170)

                    tab_lab97 = Label(tables, text="10  x   7   =    70", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab97.place(x=620, y=240)

                    tab_lab98 = Label(tables, text="10  x   8   =    80", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab98.place(x=620, y=310)

                    tab_lab99 = Label(tables, text="10  x   9   =    90", font=('castellar', 29, 'bold'),
                                      bg='#fff7ea')
                    tab_lab99.place(x=620, y=380)

                    tab_lab100 = Label(tables, text="10  x  10  =   100", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab100.place(x=620, y=450)

                table_tenth_btn = Button(tables, text="10", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                         command=table_tenth_pg)
                table_tenth_btn.place(x=540, y=510)

                def table_eleven_pg():
                    tab_lab101 = Label(tables, text="11   x   1   =   11   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab101.place(x=120, y=170)

                    tab_lab102 = Label(tables, text="11   x   2   =   22    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab102.place(x=120, y=240)

                    tab_lab103 = Label(tables, text="11   x   3   =   33    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab103.place(x=120, y=310)

                    tab_lab104 = Label(tables, text="11   x   4   =   44    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab104.place(x=120, y=380)

                    tab_lab105 = Label(tables, text="11   x   5   =   55    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab105.place(x=120, y=450)

                    tab_lab106 = Label(tables, text="11   x   6   =   66 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab106.place(x=620, y=170)

                    tab_lab107 = Label(tables, text="11  x   7   =    77  ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab107.place(x=620, y=240)

                    tab_lab108 = Label(tables, text="11  x   8   =    88 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab108.place(x=620, y=310)

                    tab_lab109 = Label(tables, text="11  x   9   =    99 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab109.place(x=620, y=380)

                    tab_lab110 = Label(tables, text="11  x  10  =   110  ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab110.place(x=620, y=450)

                table_eleven_btn = Button(tables, text="11", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                          command=table_eleven_pg)
                table_eleven_btn.place(x=580, y=510)

                def table_twelve_pg():
                    tab_lab111 = Label(tables, text="12   x   1   =   10   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab111.place(x=120, y=170)

                    tab_lab112 = Label(tables, text="12   x   2   =   24    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab112.place(x=120, y=240)

                    tab_lab113 = Label(tables, text="12   x   3   =   36    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab113.place(x=120, y=310)

                    tab_lab114 = Label(tables, text="12   x   4   =   48   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab114.place(x=120, y=380)

                    tab_lab115 = Label(tables, text="12   x   5   =   60   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab115.place(x=120, y=450)

                    tab_lab116 = Label(tables, text="12   x   6   =   72 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab116.place(x=620, y=170)

                    tab_lab117 = Label(tables, text="12  x   7   =    84 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab117.place(x=620, y=240)

                    tab_lab118 = Label(tables, text="12  x   8   =    96 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab118.place(x=620, y=310)

                    tab_lab119 = Label(tables, text="12  x   9   =   108", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab119.place(x=620, y=380)

                    tab_lab120 = Label(tables, text="12  x  10  =   120", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab120.place(x=620, y=450)

                table_twelve_btn = Button(tables, text="12", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                          command=table_twelve_pg)
                table_twelve_btn.place(x=620, y=510)

                def table_thirteen_pg():
                    tab_lab121 = Label(tables, text="13   x   1   =   13   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab121.place(x=120, y=170)

                    tab_lab122 = Label(tables, text="13   x   2   =   26   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab122.place(x=120, y=240)

                    tab_lab123 = Label(tables, text="13   x   3   =   39   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab123.place(x=120, y=310)

                    tab_lab124 = Label(tables, text="13   x   4   =   52   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab124.place(x=120, y=380)

                    tab_lab125 = Label(tables, text="13   x   5   =   65   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab125.place(x=120, y=450)

                    tab_lab126 = Label(tables, text="13   x   6   =   78 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab126.place(x=620, y=170)

                    tab_lab127 = Label(tables, text="13  x   7   =    91 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab127.place(x=620, y=240)

                    tab_lab128 = Label(tables, text="13  x   8   =  104 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab128.place(x=620, y=310)

                    tab_lab129 = Label(tables, text="13  x   9   =  117  ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab129.place(x=620, y=380)

                    tab_lab130 = Label(tables, text="13  x  10  =   130 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab130.place(x=620, y=450)

                table_thirteen_btn = Button(tables, text="13", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                            command=table_thirteen_pg)
                table_thirteen_btn.place(x=660, y=510)

                def table_fourthteen_pg():
                    tab_lab131 = Label(tables, text="14   x   1   =  14   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab131.place(x=120, y=170)

                    tab_lab132 = Label(tables, text="14   x   2   =  28    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab132.place(x=120, y=240)

                    tab_lab133 = Label(tables, text="14   x   3   =  42    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab133.place(x=120, y=310)

                    tab_lab134 = Label(tables, text="14   x   4   =  56    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab134.place(x=120, y=380)

                    tab_lab135 = Label(tables, text="14   x   5   =  70    ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab135.place(x=120, y=450)

                    tab_lab136 = Label(tables, text="14   x   6   =  84 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab136.place(x=620, y=170)

                    tab_lab137 = Label(tables, text="14  x   7   =   98 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab137.place(x=620, y=240)

                    tab_lab138 = Label(tables, text="14  x   8   =  112 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab138.place(x=620, y=310)

                    tab_lab139 = Label(tables, text="14  x   9   =  126 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab139.place(x=620, y=380)

                    tab_lab140 = Label(tables, text="14  x  10  =   140 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab140.place(x=620, y=450)

                table_fourthteen_btn = Button(tables, text="14", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                              command=table_fourthteen_pg)
                table_fourthteen_btn.place(x=700, y=510)

                def table_fifthteen_pg():
                    tab_lab141 = Label(tables, text="15   x   1   =  15   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab141.place(x=120, y=170)

                    tab_lab142 = Label(tables, text="15   x   2   =  30   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab142.place(x=120, y=240)

                    tab_lab143 = Label(tables, text="15   x   3   =  45   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab143.place(x=120, y=310)

                    tab_lab144 = Label(tables, text="15   x   4   =   60   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab144.place(x=120, y=380)

                    tab_lab145 = Label(tables, text="15   x   5   =   75   ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab145.place(x=120, y=450)

                    tab_lab146 = Label(tables, text="15   x   6   =  90 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab146.place(x=620, y=170)

                    tab_lab147 = Label(tables, text="15  x   7   =  105 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab147.place(x=620, y=240)

                    tab_lab148 = Label(tables, text="15  x   8   =  120 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab148.place(x=620, y=310)

                    tab_lab149 = Label(tables, text="15  x   9   =  135 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab149.place(x=620, y=380)

                    tab_lab150 = Label(tables, text="15  x  10  =   150 ", font=('castellar', 29, 'bold'),
                                       bg='#fff7ea')
                    tab_lab150.place(x=620, y=450)

                table_fifthteen_btn = Button(tables, text="15", font=('castellar', 12, 'bold'), bg='#fffdf0', bd=1,
                                             command=table_fifthteen_pg)
                table_fifthteen_btn.place(x=740, y=510)

            table_btn = Button(maths, text="TABLES", font=('Arial', 20, 'bold'), bg='#ffffff',
                               command=tables_pg)
            table_btn.place(x=200, y=270)

            # ----------------------------------------- addition----------------------------------------------------------------------------------
            def additn():
                opr = tk.Toplevel()
                opr.geometry('1060x595+250+100')
                opr.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(opr, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()
                op_label = Label(opr, text='MATHS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                op_label.place(x=420, y=35)
                op_label = Label(opr, text='MATHS-Addition', font=('castellar', 29, 'bold'), fg='red3',
                                 bg='#fffdf0')
                op_label.place(x=320, y=35)

                def opr_ad_pg():
                    op_label = Label(opr, text='1   +   1   =   2     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='1   +   2   =   3     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='1   +   3   =   4     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='1   +   4   =   5     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='1   +   5   =   6   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='1   +   6   =   7   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='1   +   7   =   8   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='1   +   8   =   9   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='1   +   9   =   10  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='1   +   10   =  11  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="1", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=400, y=510)

                def opr_ad_pg():
                    op_label = Label(opr, text='2   +   1   =   2    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='2   +   2   =   4    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='2   +   3   =   5    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='2   +   4   =   6   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='2   +   5   =   7   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='2   +   6   =   8   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='2   +   7   =   9   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='2   +   8   =   10   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='2   +   9   =   11  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='2   +   10   =  12  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="2", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=430, y=510)

                def opr_ad_pg():
                    op_label = Label(opr, text='3   +   1   =   4     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='3   +   2   =   5     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='3   +   3   =   6     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='3   +   4   =   7     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='3   +   5   =   8     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='3   +   6   =   9   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='3   +   7   =   10   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='3   +   8   =   11   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='3   +   9   =   12   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='3   +   10   =  13  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="3", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=460, y=510)

                def opr_ad_pg():
                    op_label = Label(opr, text='4   +   1   =   5     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='4   +   2   =   6     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='4   +   3   =   7     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='4   +   4   =   8     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='4   +   5   =   9     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='4   +   6   =   10   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='4   +   7   =   11   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='4   +   8   =   12   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='4   +   9   =   13  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='4   +   10   =  14  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="4", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=490, y=510)

                def opr_ad_pg():
                    op_label = Label(opr, text='5   +   1   =   6     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='5   +   2   =   7     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='5   +   3   =   8     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='5   +   4   =   9     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='5   +   5   =   10     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='5   +   6   =   11   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='5   +   7   =   12   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='5   +   8   =   13   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='5   +   9   =   14  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='5   +   10   =  15  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="5", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=520, y=510)

                def opr_ad_pg():
                    op_label = Label(opr, text='6   +   1   =   7     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='6   +   2   =   8     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='6   +   3   =   9     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='6   +   4   =   10    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='6   +   5   =   11    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='6   +   6   =   12  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='6   +   7   =   13  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='6   +   8   =   14  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='6   +   9   =   15 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='6   +  10   =  16 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="6", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=550, y=510)

                def opr_ad_pg():
                    op_label = Label(opr, text='7   +   1   =   8     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='7   +   2   =   9     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='7   +   3   =   10    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='7   +   4   =   11    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='7   +   5   =   12    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='7   +   6   =   13  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='7   +   7   =   14  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='7   +   8   =   15  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='7   +   9   =   16 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='7   +   10   =  17  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="7", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=580, y=510)

                def opr_ad_pg():
                    op_label = Label(opr, text='8   +   1   =   9     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='8   +   2   =   10    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='8   +   3   =   11    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='8   +   4   =   12    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='8   +   5   =   13    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='8   +   6   =   14  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='8   +   7   =   15  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='8   +   8   =   16  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='8   +   9   =   17  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='8   +   10   =  18   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="8", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=610, y=510)

                def opr_ad_pg():
                    op_label = Label(opr, text='9   +   1   =   10    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='9   +   2   =   11    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='9   +   3   =   12    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='9   +   4   =   13    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='9   +   5   =   14    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='9   +   6   =   15  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='9   +   7   =   16  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='9   +   8   =   17  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='9   +   9   =   18  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='9   +   10   =  19  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="9", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=640, y=510)

                def opr_ad_pg():
                    op_label = Label(opr, text='10   +   1   =   11    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr, text='10   +   2   =   12    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr, text='10   +   3   =   13     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr, text='10   +   4   =   14    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr, text='10  +   5   =    15    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr, text='10   +   6   =   16  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr, text='10   +   7   =   17  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr, text='10   +   8   =   18  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr, text='10   +   9   =   19  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr, text='10   +   10   =  20 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr, text="10", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_ad_pg)
                opr_btn.place(x=670, y=510)

            additn_btn = Button(maths, text="ADDITION", font=('Arial', 20, 'bold'), bg='#ffffff',
                                command=additn)
            additn_btn.place(x=110, y=180)

            # -----------------------------SUbtract---------------------------------------------------------------------------
            def subtract_pg():
                opr1 = tk.Toplevel()
                opr1.geometry('1060x595+250+100')
                opr1.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(opr1, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()
                op_label = Label(opr1, text='MATHS-Subtraction', font=('castellar', 29, 'bold'), fg='red3',
                                 bg='#fffdf0')
                op_label.place(x=280, y=35)

                def opr_sub_pg():
                    op_label = Label(opr1, text='MATHS-Subtraction', font=('castellar', 29, 'bold'), fg='red3',
                                     bg='#fffdf0')
                    op_label.place(x=280, y=35)

                    op_label = Label(opr1, text='1   -   1   =   0   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="1", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=400, y=510)

                def opr_sub_pg():
                    op_label = Label(opr1, text='2   -   1   =   1   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='2   -   2   =   0   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='                     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="2", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=430, y=510)

                def opr_sub_pg():
                    op_label = Label(opr1, text='3   -   1   =   2   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='3   -   2   =   1   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='3   -   3   =   0  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="3", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=460, y=510)

                def opr_sub_pg():
                    op_label = Label(opr1, text='4   -   1   =   3   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='4   -   2   =   2   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='4   -   3   =   1   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='4   -   4   =   0   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="4", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=490, y=510)

                def opr_sub_pg():
                    op_label = Label(opr1, text='5   -   1   =   4      ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='5   -   2   =   3      ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='5   -   3   =   2       ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='5   -   4   =   1       ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='5   -   5   =   0       ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="5", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=520, y=510)

                def opr_sub_pg():
                    op_label = Label(opr1, text='6   -   1   =   5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='6   -   2   =   4   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='6   -   3   =   3   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='6   -   4   =   2  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='6   -   5   =   1  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='6   -   6   =   0  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="6", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=550, y=510)

                def opr_sub_pg():
                    op_label = Label(opr1, text='7   -   1   =   6   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='7   -   2   =   5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='7   -   3   =   4  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='7   -   4   =   3  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='7   -   5   =   2  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='7   -   6   =   1   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='7   -   7   =   0   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='                     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='                     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='                     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="7", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=580, y=510)

                def opr_sub_pg():
                    op_label = Label(opr1, text='8   -   1   =   7   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='8   -   2   =   6  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='8   -   3   =   5  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='8   -   4   =   4    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='8   -   5   =   3    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='8   -   6   =   2  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='8   -   7   =   1  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='8   -   8   =   0  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='                    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="8", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=610, y=510)

                def opr_sub_pg():
                    op_label = Label(opr1, text='9   -   1   =   8   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='9   -   2   =   7  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='9   -   3   =   6  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='9   -   4   =   5  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='9   -   5   =   4  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='9   -   6   =   3  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='9   -   7   =   2  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='9   -   8   =   1  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='9   -   9   =   0  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='                     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="9", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=640, y=510)

                def opr_sub_pg():
                    op_label = Label(opr1, text='10   -   1   =   9  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr1, text='10   -   2   =   8  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr1, text='10   -   3   =   7  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr1, text='10   -   4   =   6  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr1, text='10  -   5   =    5  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr1, text='10   -   6   =   4  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=170)

                    op_label = Label(opr1, text='10   -   7   =   3  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=240)

                    op_label = Label(opr1, text='10   -   8   =   2  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=310)

                    op_label = Label(opr1, text='10   -   9   =   1  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=380)

                    op_label = Label(opr1, text='10   -  10   =  0   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=620, y=450)

                opr_btn = Button(opr1, text="10", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=opr_sub_pg)
                opr_btn.place(x=670, y=510)

            subtract_btn = Button(maths, text="SUBTRACTION", font=('Arial', 20, 'bold'), bg='#ffffff',
                                  command=subtract_pg)
            subtract_btn.place(x=290, y=180)

            # -------------------------------------DIVISION------------------------------------------------------------------------------------------
            def div_pg():
                opr2 = tk.Toplevel()
                opr2.geometry('1060x595+250+100')
                opr2.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(opr2, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()
                op_label = Label(opr2, text='MATHS-DIVISON', font=('castellar', 29, 'bold'), fg='red3',
                                 bg='#fffdf0')
                op_label.place(x=320, y=35)

                def _opr_div_pg():
                    op_label = Label(opr2, text='MATHS-DIVISON', font=('castellar', 29, 'bold'), fg='red3',
                                     bg='#fffdf0')
                    op_label.place(x=320, y=35)
                    op_label = Label(opr2, text='1   ÷   1   =   1    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='1   ÷   2   =   0.5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='1   ÷   3   =   0.33   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='1   ÷   4   =   0.25   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='1   ÷   5   =   0.2   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='1   ÷   6   =   0.16 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='1   ÷   7   =   0.14 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='1   ÷   8   =   0.12 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='1   ÷   9   =   0.11  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='1   ÷  10   =   0.1  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="1", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=400, y=510)

                def _opr_div_pg():
                    op_label = Label(opr2, text='2   ÷   1   =   2   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='2   ÷   2   =   1    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='2   ÷   3   =   0.66  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='2   ÷   4   =   0.5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='2   ÷   5   =   0.4   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='2   ÷   6   =  0.33  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='2   ÷   7   =  0.28  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='2   ÷   8   =  0.25  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='2   ÷   9   =  0.22  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='2   ÷   10   =  0.2  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="2", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=430, y=510)

                def _opr_div_pg():
                    op_label = Label(opr2, text='3   ÷   1   =   3   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='3   ÷   2   =   1.5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='3   ÷   3   =   1     ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='3   ÷   4   =   0.75   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='3   ÷   5   =   0.6   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='3   ÷   6   =   0.5  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='3   ÷   7   =  0.42  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='3   ÷   8   =  0.37  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='3   ÷   9   =  0.33  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='3   ÷   10   =  0.3  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="3", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=460, y=510)

                def _opr_div_pg():
                    op_label = Label(opr2, text='4   ÷   1   =   4   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='4   ÷   2   =   2   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='4   ÷   3   =   1.33   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='4   ÷   4   =   1    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='4   ÷   5   =   0.8   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='4   ÷   6   =  0.66 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='4   ÷   7   =  0.57  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='4   ÷   8   =   0.5  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='4   ÷   9   =  0.44 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='4   ÷   10   =  0.4  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="4", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=490, y=510)

                def _opr_div_pg():
                    op_label = Label(opr2, text='5   ÷   1   =   5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='5   ÷   2   =   2.5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='5   ÷   3   =   1.6   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='5   ÷   4   =   1.25   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='5   ÷   5   =   1    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='5   ÷   6   =  0.83  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='5   ÷   7   =  0.71   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='5   ÷   8   =  0.62  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='5   ÷   9   =   0.55  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='5   ÷   10   =  0.5  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="5", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=520, y=510)

                def _opr_div_pg():
                    op_label = Label(opr2, text='6   ÷   1   =   6   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='6   ÷   2   =   3   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='6   ÷   3   =   2   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='6   ÷   4   =   1.5  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='6   ÷   5   =   1.2  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='6   ÷   6   =   1    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='6   ÷   7   =  0.85  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='6   ÷   8   =  0.75 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='6   ÷   9   =  0.66 ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='6   ÷  10   =  0.6  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="6", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=550, y=510)

                def _opr_div_pg():
                    op_label = Label(opr2, text='7   ÷   1   =   7   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='7   ÷   2   =   3.5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='7   ÷   3   =   2.33  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='7   ÷   4   =   1.75  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='7   ÷   5   =   1.4  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='7   ÷   6   =   1.1  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='7   ÷   7   =    1    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='7   ÷   8   =  0.85   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='7   ÷   9   =  0.77   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='7   ÷   10   =  0.7  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="7", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=580, y=510)

                def _opr_div_pg():
                    op_label = Label(opr2, text='8   ÷   1   =   8   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='8   ÷   2   =   4   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='8   ÷   3   =   2.6   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='8   ÷   4   =   2   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='8   ÷   5   =   1.6   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='8   ÷   6   =   1.3   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='8   ÷   7   =   1.1   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='8   ÷   8   =    1    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='8   ÷   9   =  0.88  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='8   ÷   10   = 0.8  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="8", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=610, y=510)

                def _opr_div_pg():
                    op_label = Label(opr2, text='9   ÷   1   =   9    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='9   ÷   2   =   4.5  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='9   ÷   3   =   3      ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='9   ÷   4   =   2.25   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='9   ÷   5   =   1.8   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='9   ÷   6   =   1.5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='9   ÷   7   =   1.2   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='9   ÷   8   =   1.1   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='9   ÷   9   =    1    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='9   ÷   10   =  0.9  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="9", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=640, y=510)

                def _opr_div_pg():
                    op_label = Label(opr2, text='10   ÷   1   =   10  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=170)

                    op_label = Label(opr2, text='10   ÷   2   =   5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=240)

                    op_label = Label(opr2, text='10   ÷   3   =   3.33    ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=310)

                    op_label = Label(opr2, text='10   ÷   4   =   2.5   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=380)

                    op_label = Label(opr2, text='10  ÷   5   =    2   ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=120, y=450)

                    op_label = Label(opr2, text='10   ÷   6   =   1.6  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=170)

                    op_label = Label(opr2, text='10   ÷   7   =   1.4  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=240)

                    op_label = Label(opr2, text='10   ÷   8   =   1.2  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=310)

                    op_label = Label(opr2, text='10   ÷   9   =   1.1  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=380)

                    op_label = Label(opr2, text='10   ÷   10   =  1  ', font=('castellar', 29, 'bold'),
                                     bg='#fff7ea')
                    op_label.place(x=600, y=450)

                opr_btn = Button(opr2, text="9", font=('castellar', 12, 'bold'), bg='#fff7ea',
                                 command=_opr_div_pg)
                opr_btn.place(x=640, y=510)

            division_btn = Button(maths, text='DIVISON', font=('Arial', 20, 'bold'), bg='#ffffff',
                                  command=div_pg)
            division_btn.place(x=540, y=180)
#-----------------------------------------------NUMBERS------------------------------------------------------------------------------
            # Initialize Pygame mixer
            pygame.mixer.init()

            def numbers():
                numbers = tk.Toplevel()
                numbers.geometry('1060x595+250+100')
                numbers.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(numbers, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                numberslabel = Label(numbers, text='NUMBERS', font=('castellar', 29, 'bold'), fg='red3',
                                     bg='#fffdf0')
                numberslabel.place(x=395, y=35)

                ##---------------------------------------

                zero_image = Image.open("0.png")
                zero_image = zero_image.resize((120, 120))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(numbers, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("0.mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(numbers, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)

                ##---------------------------------------

                # Load the one image
                one_image = Image.open("1.png")
                one_image = one_image.resize((120, 120))
                one_photo = ImageTk.PhotoImage(one_image)

                # Create a label to display the one image
                one_label = Label(numbers, image=one_photo)
                one_label.image = one_photo
                one_label.place(x=245, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("1.mp3")
                        pygame.mixer.music.play()

                # Create a button with the one image
                one_button = Button(numbers, image=one_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                    command=play_audio)
                one_button.place(x=245, y=200)

                ##---------------------------------------

                # Load the two image
                two_image = Image.open("2.png")
                two_image = two_image.resize((120, 120))
                two_photo = ImageTk.PhotoImage(two_image)

                # Create a label to display the two image
                two_label = Label(numbers, image=two_photo)
                two_label.image = two_photo
                two_label.place(x=390, y=200)

                # Define function to play audio on button click
                def play_two_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("2.mp3")
                        pygame.mixer.music.play()

                # Create a button with the two image
                two_button = Button(numbers, image=two_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                    command=play_two_audio)
                two_button.place(x=390, y=200)

                ##---------------------------------------

                # Load the three image
                three_image = Image.open("3.png")
                three_image = three_image.resize((120, 120))
                three_photo = ImageTk.PhotoImage(three_image)

                # Create a label to display the three image
                three_label = Label(numbers, image=three_photo)
                three_label.image = three_photo
                three_label.place(x=540, y=200)

                # Define function to play audio on button click
                def play_three_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("3.mp3")
                        pygame.mixer.music.play()

                # Create a button with the three image
                three_button = Button(numbers, image=three_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_three_audio)
                three_button.place(x=540, y=200)

                ##---------------------------------------

                four_image = Image.open("4.png")
                four_image = four_image.resize((120, 120))
                four_photo = ImageTk.PhotoImage(four_image)

                # Create a label to display the four image
                four_label = Label(numbers, image=four_photo)
                four_label.image = four_photo
                four_label.place(x=690, y=200)

                # Define function to play audio on button click
                def play_four_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("4.mp3")
                        pygame.mixer.music.play()

                # Create a button with the four image
                four_button = Button(numbers, image=four_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_four_audio)
                four_button.place(x=690, y=200)

                ##---------------------------------------

                # Load the five image
                five_image = Image.open("5.png")
                five_image = five_image.resize((120, 120))
                five_photo = ImageTk.PhotoImage(five_image)

                # Create a label to display the five image
                five_label = Label(numbers, image=five_photo)
                five_label.image = five_photo
                five_label.place(x=840, y=200)

                # Define function to play audio on button click
                def play_five_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("5.mp3")
                        pygame.mixer.music.play()

                # Create a button with the five image
                five_button = Button(numbers, image=five_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_five_audio)
                five_button.place(x=840, y=200)

                ##---------------------------------------

                six_image = Image.open("6.png")
                six_image = six_image.resize((120, 120))
                six_photo = ImageTk.PhotoImage(six_image)

                # Create a label to display the six image
                six_label = Label(numbers, image=six_photo)
                six_label.image = six_photo
                six_label.place(x=180, y=350)

                # Define function to play audio on button click
                def play_six_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("6.mp3")
                        pygame.mixer.music.play()

                # Create a button with the six image
                six_button = Button(numbers, image=six_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                    command=play_six_audio)
                six_button.place(x=180, y=350)

                ##---------------------------------------

                # Load and resize the image for seven
                seven_image = Image.open("7.png")
                seven_image = seven_image.resize((120, 120))
                seven_photo = ImageTk.PhotoImage(seven_image)

                # Create a label to display the seven image
                seven_label = Label(numbers, image=seven_photo)
                seven_label.image = seven_photo
                seven_label.place(x=320, y=350)

                # Define function to play audio on button click
                def play_seven_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("7.mp3")
                        pygame.mixer.music.play()

                # Create a button with the seven image
                seven_button = Button(numbers, image=seven_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_seven_audio)
                seven_button.place(x=320, y=350)

                ##---------------------------------------

                eight_image = Image.open("8.png")
                eight_image = eight_image.resize((120, 120))
                eight_photo = ImageTk.PhotoImage(eight_image)

                # Create a label to display the eight image
                eight_label = Label(numbers, image=eight_photo)
                eight_label.image = eight_photo
                eight_label.place(x=460, y=350)

                # Define function to play audio on button click
                def play_eight_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("8.mp3")
                        pygame.mixer.music.play()

                # Create a button with the eight image
                eight_button = Button(numbers, image=eight_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_eight_audio)
                eight_button.place(x=460, y=350)

                ##---------------------------------------

                nine_image = Image.open("9.png")
                nine_image = nine_image.resize((120, 120))
                nine_photo = ImageTk.PhotoImage(nine_image)

                # Create a label to display the nine image
                nine_label = Label(numbers, image=nine_photo)
                nine_label.image = nine_photo
                nine_label.place(x=600, y=350)

                # Define function to play audio on button click
                def play_nine_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("9.mp3")
                        pygame.mixer.music.play()

                # Create a button with the nine image
                nine_button = Button(numbers, image=nine_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_nine_audio)
                nine_button.place(x=600, y=350)

                ##---------------------------------------

                ten_image = Image.open("10.png")
                ten_image = ten_image.resize((120, 120))
                ten_photo = ImageTk.PhotoImage(ten_image)

                # Create a label to display the ten image
                ten_label = Label(numbers, image=ten_photo)
                ten_label.image = ten_photo
                ten_label.place(x=740, y=350)

                # Define function to play audio on button click
                def play_ten_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("10.mp3")
                        pygame.mixer.music.play()

                # Create a button with the ten image
                ten_button = Button(numbers, image=ten_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                    command=play_ten_audio)
                ten_button.place(x=740, y=350)

                def new():
                    new = tk.Toplevel()
                    new.geometry('1060x595+250+100')
                    new.title('Teachify - For Kids')

                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.png")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(new, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    ##---------------------------------------

                    eleven_image = Image.open("11.png")
                    eleven_image = eleven_image.resize((120, 120))
                    eleven_photo = ImageTk.PhotoImage(eleven_image)

                    # Create a label to display the image
                    eleven_label = Label(new, image=eleven_photo)
                    eleven_label.image = eleven_photo
                    eleven_label.place(x=130, y=200)

                    # Define function to play audio on button click
                    def play_eleven_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("11a.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    eleven_button = Button(new, image=eleven_photo, bg='white', relief=FLAT, bd=0,
                                           highlightthickness=0, command=play_eleven_audio)
                    eleven_button.place(x=130, y=200)

                    ##---------------------------------------

                    # Load and resize the image
                    twelve_image = Image.open("12.png")
                    twelve_image = twelve_image.resize((120, 120))
                    twelve_photo = ImageTk.PhotoImage(twelve_image)

                    # Create a label to display the image
                    twelve_label = Label(new, image=twelve_photo)
                    twelve_label.image = twelve_photo
                    twelve_label.place(x=300, y=200)

                    # Define function to play audio on button click
                    def play_twelve_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("12a.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    twelve_button = Button(new, image=twelve_photo, bg='white', relief=FLAT, bd=0,
                                           highlightthickness=0, command=play_twelve_audio)
                    twelve_button.place(x=300, y=200)

                    ##---------------------------------------

                    # Load and resize the image
                    thirteen_image = Image.open("13.png")
                    thirteen_image = thirteen_image.resize((120, 120))
                    thirteen_photo = ImageTk.PhotoImage(thirteen_image)

                    # Create a label to display the image
                    thirteen_label = Label(new, image=thirteen_photo)
                    thirteen_label.image = thirteen_photo
                    thirteen_label.place(x=470, y=200)

                    # Define function to play audio on button click
                    def play_thirteen_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("13a.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    thirteen_button = Button(new, image=thirteen_photo, bg='white', relief=FLAT, bd=0,
                                             highlightthickness=0, command=play_thirteen_audio)
                    thirteen_button.place(x=470, y=200)

                    ##---------------------------------------

                    # Load and resize the image
                    fourteen_image = Image.open("14.png")
                    fourteen_image = fourteen_image.resize((120, 120))
                    fourteen_photo = ImageTk.PhotoImage(fourteen_image)

                    # Create a label to display the image
                    fourteen_label = Label(new, image=fourteen_photo)
                    fourteen_label.image = fourteen_photo
                    fourteen_label.place(x=640, y=200)

                    # Define function to play audio on button click
                    def play_fourteen_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("14a.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    fourteen_button = Button(new, image=fourteen_photo, bg='white', relief=FLAT, bd=0,
                                             highlightthickness=0, command=play_fourteen_audio)
                    fourteen_button.place(x=640, y=200)

                    ##---------------------------------------

                    fifteen_image = Image.open("15.png")
                    fifteen_image = fifteen_image.resize((120, 120))
                    fifteen_photo = ImageTk.PhotoImage(fifteen_image)

                    # Create a label to display the image
                    fifteen_label = Label(new, image=fifteen_photo)
                    fifteen_label.image = fifteen_photo
                    fifteen_label.place(x=810, y=200)

                    # Define function to play audio on button click
                    def play_fifteen_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("15a.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    fifteen_button = Button(new, image=fifteen_photo, bg='white', relief=FLAT, bd=0,
                                            highlightthickness=0, command=play_fifteen_audio)
                    fifteen_button.place(x=810, y=200)

                    ##---------------------------------------

                    # Load and resize the image
                    sixteen_image = Image.open("16.png")
                    sixteen_image = sixteen_image.resize((120, 120))
                    sixteen_photo = ImageTk.PhotoImage(sixteen_image)

                    # Create a label to display the image
                    sixteen_label = Label(new, image=sixteen_photo)
                    sixteen_label.image = sixteen_photo
                    sixteen_label.place(x=130, y=350)

                    # Define function to play audio on button click
                    def play_sixteen_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("16.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    sixteen_button = Button(new, image=sixteen_photo, bg='white', relief=FLAT, bd=0,
                                            highlightthickness=0, command=play_sixteen_audio)
                    sixteen_button.place(x=130, y=350)

                    ##---------------------------------------

                    # Load and resize the image
                    seventeen_image = Image.open("17.png")
                    seventeen_image = seventeen_image.resize((120, 120))
                    seventeen_photo = ImageTk.PhotoImage(seventeen_image)

                    # Create a label to display the image
                    seventeen_label = Label(new, image=seventeen_photo)
                    seventeen_label.image = seventeen_photo
                    seventeen_label.place(x=300, y=350)

                    # Define function to play audio on button click
                    def play_seventeen_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("17.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    seventeen_button = Button(new, image=seventeen_photo, bg='white', relief=FLAT, bd=0,
                                              highlightthickness=0, command=play_seventeen_audio)
                    seventeen_button.place(x=300, y=350)
                    ##---------------------------------------

                    eighteen_image = Image.open("18.png")
                    eighteen_image = eighteen_image.resize((120, 120))
                    eighteen_photo = ImageTk.PhotoImage(eighteen_image)

                    # Create a label to display the image
                    eighteen_label = Label(new, image=eighteen_photo)
                    eighteen_label.image = eighteen_photo
                    eighteen_label.place(x=470, y=350)

                    # Define function to play audio on button click
                    def play_eighteen_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("18.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    eighteen_button = Button(new, image=eighteen_photo, bg='white', relief=FLAT, bd=0,
                                             highlightthickness=0, command=play_eighteen_audio)
                    eighteen_button.place(x=470, y=350)
                    ##---------------------------------------

                    nineteen_image = Image.open("19.png")
                    nineteen_image = nineteen_image.resize((120, 120))
                    nineteen_photo = ImageTk.PhotoImage(nineteen_image)

                    # Create a label to display the image
                    nineteen_label = Label(new, image=nineteen_photo)
                    nineteen_label.image = nineteen_photo
                    nineteen_label.place(x=640, y=350)

                    # Define function to play audio on button click
                    def play_nineteen_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("19.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    nineteen_button = Button(new, image=nineteen_photo, bg='white', relief=FLAT, bd=0,
                                             highlightthickness=0, command=play_nineteen_audio)
                    nineteen_button.place(x=640, y=350)

                    ##---------------------------------------

                    twenty_image = Image.open("20.png")
                    twenty_image = twenty_image.resize((120, 120))
                    twenty_photo = ImageTk.PhotoImage(twenty_image)

                    # Create a label to display the image
                    twenty_label = Label(new, image=twenty_photo)
                    twenty_label.image = twenty_photo
                    twenty_label.place(x=810, y=350)

                    # Define function to play audio on button click
                    def play_twenty_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("20.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the image
                    twenty_button = Button(new, image=twenty_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                           command=play_twenty_audio)
                    twenty_button.place(x=810, y=350)






                    numberslabel = Label(new, text='NUMBERS', font=('castellar', 29, 'bold'), fg='red3',
                                         bg='#fffdf0')
                    numberslabel.place(x=395, y=35)

                nextButton = Button(numbers, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=new)
                nextButton.place(x=840, y=480)

            numbers2_btn = Button(maths, text="NUMBERS", font=('Arial', 20, 'bold'), bg='#ffffff',command= numbers)
            numbers2_btn.place(x=480, y=350)
            # -----------------------------------calculator-------------------------------------------------------------------------
            def calc_pg():
                cal = tk.Toplevel()
                cal.geometry('1060x595+250+100')
                cal.title('Teachify - For Kids')
                # Create a frame to hold the image
                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.png")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(cal, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)
                blank_label = Label(cal, text="                                     ", bd=2, font=('Arial', 20, 'bold'),
                                    bg='black')
                blank_label.place(x=550, y=400)

                op_label = Label(cal, text='MATHS-CALCULATOR', font=('castellar', 29, 'bold'), fg='red3',
                                 bg='#fffdf0')
                op_label.place(x=280, y=35)

                class CalculatorUI():
                    def __init__(self, master):
                        self.master = master
                        master.title("Calculator")

                        # Create labels and entry fields
                        self.label1 = tk.Label(master, text="Enter Number 1:", font=('Arial', 20, 'bold'), bg='#fffdf0')
                        self.label1.place(x=300, y=200)

                        self.label2 = tk.Label(master, text="Enter Number 2:", font=('Arial', 20, 'bold'), bg='#fffdf0')
                        self.label2.place(x=300, y=300)

                        self.label3 = tk.Label(master, text="Result:", font=('Arial', 20, 'bold'), bg='#fffdf0')
                        self.label3.place(x=300, y=400)

                        self.entry1 = tk.Entry(master, font=('Arial', 20, 'bold'), bg='#ffffff')
                        self.entry1.place(x=550, y=200)

                        self.entry2 = tk.Entry(master, font=('Arial', 20, 'bold'), bg='#ffffff')
                        self.entry2.place(x=550, y=300)

                        self.result = tk.Label(master, text="                   ", font=('Arial', 20, 'bold'),
                                               fg='white', bg='black')
                        self.result.place(x=550, y=400)

                        # Create buttons to perform calculations
                        self.add_button = tk.Button(master, text=" + ", font=('Arial', 20, 'bold'), bg='#fffdf0',
                                                    command=self.add)
                        self.add_button.place(x=400, y=470)

                        self.subtract_button = tk.Button(master, text=" - ", font=('Arial', 20, 'bold'), bg='#fffdf0',
                                                         command=self.subtract)
                        self.subtract_button.place(x=460, y=470)

                        self.multiply_button = tk.Button(master, text=" x ", font=('Arial', 20, 'bold'), bg='#fffdf0',
                                                         command=self.multiply)
                        self.multiply_button.place(x=520, y=470)

                        self.divide_button = tk.Button(master, text=" / ", font=('Arial', 20, 'bold'), bg='#fffdf0',
                                                       command=self.divide)
                        self.divide_button.place(x=580, y=470)

                    def add(self):
                        try:
                            num1 = int(self.entry1.get())
                            num2 = int(self.entry2.get())
                            result = num1 + num2
                            self.result.config(text=str(result))
                        except ValueError:
                            self.result.config(text="Invalid input")

                    def subtract(self):
                        try:
                            num1 = int(self.entry1.get())
                            num2 = int(self.entry2.get())
                            result = num1 - num2
                            self.result.config(text=str(result))
                        except ValueError:
                            self.result.config(text="Invalid input")

                    def multiply(self):
                        try:
                            num1 = int(self.entry1.get())
                            num2 = int(self.entry2.get())
                            result = num1 * num2
                            self.result.config(text=str(result))
                        except ValueError:
                            self.result.config(text="Invalid input")

                    def divide(self):
                        try:
                            num1 = int(self.entry1.get())
                            num2 = int(self.entry2.get())
                            result = num1 / num2
                            self.result.config(text=str(result))
                        except ValueError:
                            self.result.config(text="Invalid input")
                        except ZeroDivisionError:
                            self.result.config(text="Cannot divide by zero")

                CalculatorUI(cal)

            calc_btn = Button(maths, text="Calculator", font=('Arial', 20, 'bold'), bg='#ffffff',
                              command=calc_pg)
            calc_btn.place(x=120, y=350)
#-------------------------------------------------SQRT-----------------------------------------------------------------------------------
            def sqrt_pg():
                sqrt = tk.Toplevel()
                sqrt.geometry('1060x595+250+100')
                sqrt.title('Teachify - For Kids')
                # Create a frame to hold the image
                image_frame = Frame(sqrt, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("COURSES_BG_ICON.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                op_label = Label(sqrt, text='MATHS-SQUARE ROOTS', font=('castellar', 29, 'bold'), fg='red3',
                                 bg='#fffdf0')
                op_label.place(x=260, y=35)
                sqrt_label = Label(sqrt, text=' √1   =    1    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=120, y=170)

                sqrt_label = Label(sqrt, text=' √4   =    2    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=120, y=240)

                sqrt_label = Label(sqrt, text=' √9   =    3    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=120, y=310)

                sqrt_label = Label(sqrt, text='√16   =    4    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=120, y=380)

                sqrt_label = Label(sqrt, text='√25   =    5    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=120, y=450)

                sqrt_label = Label(sqrt, text='√36   =    6    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=600, y=170)

                sqrt_label = Label(sqrt, text='√49   =    7    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=600, y=240)

                sqrt_label = Label(sqrt, text='√64   =    8    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=600, y=310)

                sqrt_label = Label(sqrt, text='√81   =    9    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=600, y=380)

                sqrt_label = Label(sqrt, text='√100   =  10    ', font=('castellar', 29, 'bold'),
                                   bg='#fff7ea')
                sqrt_label.place(x=600, y=450)

            sq_btn = Button(maths, text="SQUARE ROOT", font=('Arial', 20, 'bold'), bg='#ffffff',
                            command=sqrt_pg)
            sq_btn.place(x=370, y=270)

# ==========================================FUN QUIZ==============================================================

            def app():
                app = tk.Toplevel()
                app.title("Teachify - For Kids")
                app.geometry("240x300")
                app.config(bg='#7F7FFF')

                num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                def submt(var1):
                    if var1.get() == str(resultPLUS()):
                        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
                        correct.place(relx=0.3, rely=0.2)
                    else:
                        wrong = Label(app, text="Wrong!!!", fg="red", font=("Courier", 16))
                        wrong.place(relx=0.3, rely=0.2)

                def try_again():
                    try_again.num1update = random.choice(num)
                    try_again.num2update = random.choice(num)
                    newQ = Label(app, text=f"{try_again.num1update}+{try_again.num2update}", font=("Courier", 16))
                    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

                def resultPLUS():
                    try_again
                    return try_again.num1update + try_again.num2update

                start = Button(app, text="Start", command=try_again)
                start.place(relx=0.45, rely=0.2)

                solving = Entry(app)
                solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

                submit = Button(app, text="Submit", command=lambda: submt(solving))
                submit.place(x=30, y=230)

                try_again = Button(app, text="Try Again", command=try_again)
                try_again.place(x=90, y=230)

                # Clear button
                clear = tk.Button(app, text="Clear", command=lambda: solving.delete(0, tk.END))
                clear.place(x=160, y=230)

            quiz_btn = Button(maths, text="FUN QUIZ", font=('Arial', 20, 'bold'), bg='#ffffff', command=app)

            quiz_btn.place(x=300, y=350)

        maths_btn = Button(courses, font=('Arial', 20, 'bold'), text="Maths", bg='#ffffff', bd=1, command=maths)
        maths_btn.place(x=350, y=150)

        # ----------------GENERAL KNOWLEDGE----------------------------
        def gk():
            gk = tk.Toplevel()
            gk.geometry('1060x595+250+100')
            gk.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(gk, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            gklabel = Label(gk, text='GENERAL KNOWLEDGE', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
            gklabel.place(x=270, y=35)

            def emo():
                emo = tk.Toplevel()
                emo.geometry('1060x595+250+100')
                emo.title('Teachify - For Kids')

                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(emo, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("angry.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(emo, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=80, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("confused.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(emo, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("cry.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(emo, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("disappointed.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(emo, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=770, y=210)

                numberslabel = Label(emo, text='HUMAN EMOTIONS', font=('castellar', 29, 'bold'), fg='red3',
                                     bg='#fffdf0')
                numberslabel.place(x=300, y=35)

                def back():
                    emo.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(emo, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def neww():
                    neww = tk.Toplevel()
                    neww.geometry('1060x595+250+100')
                    neww.title('Teachify - For Kids')

                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(neww, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("disgusted.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(neww, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=80, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("happy - Copy.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(neww, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=310, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("jelous.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(neww, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=540, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("loving - Copy.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(neww, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=770, y=210)

                    numberslabel = Label(neww, text='HUMAN EMOTIONS', font=('castellar', 29, 'bold'), fg='red3',
                                         bg='#fffdf0')
                    numberslabel.place(x=300, y=35)

                    def back():
                        neww.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(neww, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    def back():
                        neww.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(neww, image=back_button_image, bd=0, command=back, bg='#fff7ea', height=74,
                                         width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    next_button_image = ImageTk.PhotoImage(Image.open("next2.png").resize((50, 50)))

                    def open_new_window():
                        neww.after(1, lambda: [neww.destroy(),
                                               new1()])  # Delay the destruction of current window and creation of new window by 100ms

                    next_button = Button(neww, image=next_button_image, bg='#fff7ea', bd=0, command=open_new_window)
                    next_button.image = next_button_image
                    next_button.place(x=930, y=460)

                    def new1():
                        new1 = tk.Toplevel()
                        new1.geometry('1060x595+250+100')
                        new1.title('Teachify - For Kids')

                        # Load the sunset image
                        sunset_image = Image.open("COURSES_BG_ICON.jpg")
                        sunset_image = sunset_image.resize((1050, 595))
                        sunset_photo = ImageTk.PhotoImage(sunset_image)

                        # Create a label to display the sunset image
                        sunset_label = Label(new1, image=sunset_photo)
                        sunset_label.image = sunset_photo
                        sunset_label.place(x=0, y=0)

                        numberslabel = Label(new1, text='HUMAN EMOTIONS', font=('castellar', 29, 'bold'), fg='red3',
                                             bg='#fffdf0')
                        numberslabel.place(x=300, y=35)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("nervous.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(new1, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=80, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("proud.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(new1, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=310, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("sad.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(new1, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=540, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("scared.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(new1, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=770, y=210)

                        def back():
                            new1.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(new1, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                             height=74, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=460)

                        def new2():
                            new2 = tk.Toplevel()
                            new2.geometry('1060x595+250+100')
                            new2.title('Teachify - For Kids')

                            # Load the sunset image
                            sunset_image = Image.open("COURSES_BG_ICON.jpg")
                            sunset_image = sunset_image.resize((1050, 595))
                            sunset_photo = ImageTk.PhotoImage(sunset_image)

                            # Create a label to display the sunset image
                            sunset_label = Label(new2, image=sunset_photo)
                            sunset_label.image = sunset_photo
                            sunset_label.place(x=0, y=0)

                            numberslabel = Label(new2, text='HUMAN EMOTIONS', font=('castellar', 29, 'bold'), fg='red3',
                                                 bg='#fffdf0')
                            numberslabel.place(x=300, y=35)

                            ##---------------------------------------------------

                            # Load the apple image
                            apple_image = Image.open("shy.png")
                            apple_image = apple_image.resize((200, 200))
                            apple_photo = ImageTk.PhotoImage(apple_image)

                            # Create a label to display the apple image
                            apple_label = Label(new2, image=apple_photo, bg='white')
                            apple_label.image = apple_photo
                            apple_label.place(x=80, y=210)

                            ##---------------------------------------------------

                            # Load the apple image
                            apple_image = Image.open("sick.png")
                            apple_image = apple_image.resize((200, 200))
                            apple_photo = ImageTk.PhotoImage(apple_image)

                            # Create a label to display the apple image
                            apple_label = Label(new2, image=apple_photo, bg='white')
                            apple_label.image = apple_photo
                            apple_label.place(x=310, y=210)

                            ##---------------------------------------------------

                            # Load the apple image
                            apple_image = Image.open("silly.png")
                            apple_image = apple_image.resize((200, 200))
                            apple_photo = ImageTk.PhotoImage(apple_image)

                            # Create a label to display the apple image
                            apple_label = Label(new2, image=apple_photo, bg='white')
                            apple_label.image = apple_photo
                            apple_label.place(x=540, y=210)

                            ##---------------------------------------------------

                            # Load the apple image
                            apple_image = Image.open("surprised .png")
                            apple_image = apple_image.resize((200, 200))
                            apple_photo = ImageTk.PhotoImage(apple_image)

                            # Create a label to display the apple image
                            apple_label = Label(new2, image=apple_photo, bg='white')
                            apple_label.image = apple_photo
                            apple_label.place(x=770, y=210)

                            def back():
                                new2.destroy()

                            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                            back_button = Button(new2, image=back_button_image, bd=0, command=back, bg='#fff7ea',
                                                 height=74, width=76)
                            back_button.image = back_button_image
                            back_button.place(x=60, y=460)

                        nextButton = Button(new1, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                            activebackground='white',
                                            cursor='hand2', command=new2)
                        nextButton.place(x=840, y=480)

                    nextButton = Button(neww, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=new1)
                    nextButton.place(x=840, y=480)

                nextButton = Button(emo, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=neww)
                nextButton.place(x=840, y=480)

            emotions_btn = Button(gk, text='HUMAN EMOTIONS', font=('Arial', 20, 'bold'), bd=1,
                                  bg='#ffffff', command=emo)
            emotions_btn.place(x=380, y=230)

            # PLANETS##############################################################

            # Initialize Pygame mixer
            pygame.mixer.init()

            def planets():
                planets = tk.Toplevel()
                planets.geometry('1060x595+250+100')
                planets.title('Teachify - For Kids')

                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(planets, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                numberslabel = Label(planets, text='PLANETS', font=('castellar', 29, 'bold'), fg='red3',
                                     bg='#fffdf0')
                numberslabel.place(x=410, y=35)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("earth.png")
                apple_image = apple_image.resize((250, 250))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("earth.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(planets, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=100, y=210)
                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("jupiter .png")
                apple_image = apple_image.resize((250, 250))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("jupiter.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(planets, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=400, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("mercury.png")
                apple_image = apple_image.resize((250, 250))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("mercury.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(planets, image=apple_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = apple_photo
                apple_button.place(x=700, y=210)

                def back():
                    planets.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(planets, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=75, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=465)

                def planets2():
                    planets2 = tk.Toplevel()
                    planets2.geometry('1060x595+250+100')
                    planets2.title('Teachify - For Kids')

                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(planets2, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    numberslabel = Label(planets2, text='PLANETS', font=('castellar', 29, 'bold'), fg='red3',
                                         bg='#fffdf0')
                    numberslabel.place(x=410, y=35)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("neptune.png")
                    apple_image = apple_image.resize((250, 250))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Define function to play audio on button click
                    def play_apple_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("neptune.mp3")
                            pygame.mixer.music.play()

                    apple_button = Button(planets2, image=apple_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0,
                                          command=play_apple_audio)
                    apple_button.image = apple_photo
                    apple_button.place(x=100, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("sun.png")
                    apple_image = apple_image.resize((250, 250))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(planets2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=400, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("saturn.png")
                    apple_image = apple_image.resize((250, 250))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Define function to play audio on button click
                    def play_apple_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("saturn.mp3")
                            pygame.mixer.music.play()

                    apple_button = Button(planets2, image=apple_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0,
                                          command=play_apple_audio)
                    apple_button.image = apple_photo
                    apple_button.place(x=700, y=210)

                    def back():
                        planets2.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(planets2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=75, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=465)

                    def planets3():
                        planets3 = tk.Toplevel()
                        planets3.geometry('1060x595+250+100')
                        planets3.title('Teachify - For Kids')

                        # Load the sunset image
                        sunset_image = Image.open("COURSES_BG_ICON.jpg")
                        sunset_image = sunset_image.resize((1050, 595))
                        sunset_photo = ImageTk.PhotoImage(sunset_image)

                        # Create a label to display the sunset image
                        sunset_label = Label(planets3, image=sunset_photo)
                        sunset_label.image = sunset_photo
                        sunset_label.place(x=0, y=0)

                        numberslabel = Label(planets3, text='PLANETS', font=('castellar', 29, 'bold'), fg='red3',
                                             bg='#fffdf0')
                        numberslabel.place(x=410, y=35)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("uranus.png")
                        apple_image = apple_image.resize((250, 250))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Define function to play audio on button click
                        def play_apple_audio():
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.load("uranus.mp3")
                                pygame.mixer.music.play()

                        apple_button = Button(planets3, image=apple_photo, bg='white', relief=FLAT, bd=0,
                                              highlightthickness=0,
                                              command=play_apple_audio)
                        apple_button.image = apple_photo
                        apple_button.place(x=100, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("venus.png")
                        apple_image = apple_image.resize((250, 250))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Define function to play audio on button click
                        def play_apple_audio():
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.load("venus.mp3")
                                pygame.mixer.music.play()

                        apple_button = Button(planets3, image=apple_photo, bg='white', relief=FLAT, bd=0,
                                              highlightthickness=0,
                                              command=play_apple_audio)
                        apple_button.image = apple_photo
                        apple_button.place(x=400, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("mars.png")
                        apple_image = apple_image.resize((250, 250))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Define function to play audio on button click
                        def play_apple_audio():
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.load("mars.mp3")
                                pygame.mixer.music.play()

                        apple_button = Button(planets3, image=apple_photo, bg='white', relief=FLAT, bd=0,
                                              highlightthickness=0,
                                              command=play_apple_audio)
                        apple_button.image = apple_photo
                        apple_button.place(x=700, y=210)

                        def back():
                            planets3.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(planets3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                             height=75, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=465)

                    nextButton = Button(planets2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=planets3)
                    nextButton.place(x=840, y=480)

                    ##---------------------------------------------------

                nextButton = Button(planets, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=planets2)
                nextButton.place(x=840, y=480)

            planets_btn = Button(gk, text='PLANETS', font=('Arial', 20, 'bold'), bd=1,
                                 bg='#ffffff', command=planets)
            planets_btn.place(x=445, y=450)

            ## FRUITS #######################################################

            def fruits():
                fruits = tk.Toplevel()
                fruits.geometry('1060x595+250+100')
                fruits.title('Teachify - For Kids')
                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(fruits, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                booklabel = Label(fruits, text='FRUITS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                booklabel.place(x=430, y=35)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("banana.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(fruits, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=80, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("cherry.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(fruits, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("grapes .png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(fruits, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("kiwi.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(fruits, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=770, y=210)

                def back():
                    fruits.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(fruits, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def fruits2():
                    fruits2 = tk.Toplevel()
                    fruits2.geometry('1060x595+250+100')
                    fruits2.title('Teachify - For Kids')
                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(fruits2, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    booklabel = Label(fruits2, text='FRUITS', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                    booklabel.place(x=430, y=35)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("orange.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(fruits2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=80, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("pear.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(fruits2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=310, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("peach.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(fruits2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=540, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("pineapple.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(fruits2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=770, y=210)

                    def back():
                        fruits2.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(fruits2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    def fruits3():
                        fruits3 = tk.Toplevel()
                        fruits3.geometry('1060x595+250+100')
                        fruits3.title('Teachify - For Kids')
                        # Load the sunset image
                        sunset_image = Image.open("COURSES_BG_ICON.jpg")
                        sunset_image = sunset_image.resize((1050, 595))
                        sunset_photo = ImageTk.PhotoImage(sunset_image)

                        # Create a label to display the sunset image
                        sunset_label = Label(fruits3, image=sunset_photo)
                        sunset_label.image = sunset_photo
                        sunset_label.place(x=0, y=0)

                        booklabel = Label(fruits3, text='FRUITS', font=('castellar', 29, 'bold'), fg='red3',
                                          bg='#fffdf0')
                        booklabel.place(x=430, y=35)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("pomogranate.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(fruits3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=80, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("pumpkin.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(fruits3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=310, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("raspberry.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(fruits3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=540, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("strawberry.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(fruits3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=770, y=210)

                        def back():
                            fruits3.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(fruits3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                             height=74, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=460)

                        def fruits4():
                            fruits4 = tk.Toplevel()
                            fruits4.geometry('1060x595+250+100')
                            fruits4.title('Teachify - For Kids')
                            # Load the sunset image
                            sunset_image = Image.open("COURSES_BG_ICON.jpg")
                            sunset_image = sunset_image.resize((1050, 595))
                            sunset_photo = ImageTk.PhotoImage(sunset_image)

                            # Create a label to display the sunset image
                            sunset_label = Label(fruits4, image=sunset_photo)
                            sunset_label.image = sunset_photo
                            sunset_label.place(x=0, y=0)

                            booklabel = Label(fruits4, text='FRUITS', font=('castellar', 29, 'bold'), fg='red3',
                                              bg='#fffdf0')
                            booklabel.place(x=430, y=35)

                            ##---------------------------------------------------

                            # Load the apple image
                            apple_image = Image.open("plum.png")
                            apple_image = apple_image.resize((200, 200))
                            apple_photo = ImageTk.PhotoImage(apple_image)

                            # Create a label to display the apple image
                            apple_label = Label(fruits4, image=apple_photo, bg='white')
                            apple_label.image = apple_photo
                            apple_label.place(x=80, y=210)

                            ##---------------------------------------------------

                            # Load the apple image
                            apple_image = Image.open("tomato.png")
                            apple_image = apple_image.resize((200, 200))
                            apple_photo = ImageTk.PhotoImage(apple_image)

                            # Create a label to display the apple image
                            apple_label = Label(fruits4, image=apple_photo, bg='white')
                            apple_label.image = apple_photo
                            apple_label.place(x=310, y=210)

                            ##---------------------------------------------------

                            # Load the apple image
                            apple_image = Image.open("watermelon.png")
                            apple_image = apple_image.resize((200, 200))
                            apple_photo = ImageTk.PhotoImage(apple_image)

                            # Create a label to display the apple image
                            apple_label = Label(fruits4, image=apple_photo, bg='white')
                            apple_label.image = apple_photo
                            apple_label.place(x=540, y=210)

                            ##---------------------------------------------------

                            # Load the apple image
                            apple_image = Image.open("apple.png")
                            apple_image = apple_image.resize((200, 200))
                            apple_photo = ImageTk.PhotoImage(apple_image)

                            # Create a label to display the apple image
                            apple_label = Label(fruits4, image=apple_photo, bg='white')
                            apple_label.image = apple_photo
                            apple_label.place(x=770, y=210)

                            def back():
                                fruits4.destroy()

                            back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                            back_button = Button(fruits4, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                                 height=74, width=76)
                            back_button.image = back_button_image
                            back_button.place(x=60, y=460)

                        nextButton = Button(fruits3, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                            activebackground='white',
                                            cursor='hand2', command=fruits4)
                        nextButton.place(x=840, y=480)

                    nextButton = Button(fruits2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=fruits3)
                    nextButton.place(x=840, y=480)

                nextButton = Button(fruits, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=fruits2)
                nextButton.place(x=840, y=480)

            fruits_btn = Button(gk, text='FRUITS', font=('Arial', 20, 'bold'), bd=1,
                                bg='#ffffff', command=fruits)
            fruits_btn.place(x=350, y=300)

            ## VEGETABLES #######################################################

            def vegetables():
                vegetables = tk.Toplevel()
                vegetables.geometry('1060x595+250+100')
                vegetables.title('Teachify - For Kids')
                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(vegetables, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                booklabel = Label(vegetables, text='VEGETABLES', font=('castellar', 29, 'bold'), fg='red3',
                                  bg='#fffdf0')
                booklabel.place(x=390, y=35)

                ##---------------------------------------------------

                apple_image = Image.open("onions.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(vegetables, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=80, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("tomato.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(vegetables, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("carrots.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(vegetables, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("cauliflower.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(vegetables, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=770, y=210)

                def back():
                    vegetables.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(vegetables, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def vegetables2():
                    vegetables2 = tk.Toplevel()
                    vegetables2.geometry('1060x595+250+100')
                    vegetables2.title('Teachify - For Kids')
                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(vegetables2, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    booklabel = Label(vegetables2, text='VEGETABLES', font=('castellar', 29, 'bold'), fg='red3',
                                      bg='#fffdf0')
                    booklabel.place(x=390, y=35)

                    ##---------------------------------------------------

                    apple_image = Image.open("corn.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(vegetables2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=80, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("cucumber.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(vegetables2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=310, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("eggplant.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(vegetables2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=540, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("garlic.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(vegetables2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=770, y=210)

                    def back():
                        vegetables2.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(vegetables2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    def vegetables3():
                        vegetables3 = tk.Toplevel()
                        vegetables3.geometry('1060x595+250+100')
                        vegetables3.title('Teachify - For Kids')
                        # Load the sunset image
                        sunset_image = Image.open("COURSES_BG_ICON.jpg")
                        sunset_image = sunset_image.resize((1050, 595))
                        sunset_photo = ImageTk.PhotoImage(sunset_image)

                        # Create a label to display the sunset image
                        sunset_label = Label(vegetables3, image=sunset_photo)
                        sunset_label.image = sunset_photo
                        sunset_label.place(x=0, y=0)

                        booklabel = Label(vegetables3, text='VEGETABLES', font=('castellar', 29, 'bold'), fg='red3',
                                          bg='#fffdf0')
                        booklabel.place(x=390, y=35)

                        ##---------------------------------------------------

                        apple_image = Image.open("peas.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(vegetables3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=80, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("potato.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(vegetables3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=310, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("spinach.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(vegetables3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=540, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("mushroom.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(vegetables3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=770, y=210)

                        def back():
                            vegetables3.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(vegetables3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                             height=74, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=460)

                    nextButton = Button(vegetables2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=vegetables3)
                    nextButton.place(x=840, y=480)

                nextButton = Button(vegetables, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=vegetables2)
                nextButton.place(x=840, y=480)

            vegetables_btn = Button(gk, text='VEGETABLES', font=('Arial', 20, 'bold'), bd=1,
                                    bg='#ffffff', command=vegetables)
            vegetables_btn.place(x=500, y=300)

            ## CLIMATE #######################################################

            def climate():
                climate = tk.Toplevel()
                climate.geometry('1060x595+250+100')
                climate.title('Teachify - For Kids')
                # Load the sunset image
                sunset_image = Image.open("COURSES_BG_ICON.jpg")
                sunset_image = sunset_image.resize((1050, 595))
                sunset_photo = ImageTk.PhotoImage(sunset_image)

                # Create a label to display the sunset image
                sunset_label = Label(climate, image=sunset_photo)
                sunset_label.image = sunset_photo
                sunset_label.place(x=0, y=0)

                booklabel = Label(climate, text='CLIMATE', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                booklabel.place(x=390, y=35)

                ##---------------------------------------------------

                apple_image = Image.open("cloudy.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(climate, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=80, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("sunny.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(climate, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("rainy.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(climate, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the apple image
                apple_image = Image.open("lightning.png")
                apple_image = apple_image.resize((200, 200))
                apple_photo = ImageTk.PhotoImage(apple_image)

                # Create a label to display the apple image
                apple_label = Label(climate, image=apple_photo, bg='white')
                apple_label.image = apple_photo
                apple_label.place(x=770, y=210)

                def back():
                    climate.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(climate, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def climate2():
                    climate2 = tk.Toplevel()
                    climate2.geometry('1060x595+250+100')
                    climate2.title('Teachify - For Kids')
                    # Load the sunset image
                    sunset_image = Image.open("COURSES_BG_ICON.jpg")
                    sunset_image = sunset_image.resize((1050, 595))
                    sunset_photo = ImageTk.PhotoImage(sunset_image)

                    # Create a label to display the sunset image
                    sunset_label = Label(climate2, image=sunset_photo)
                    sunset_label.image = sunset_photo
                    sunset_label.place(x=0, y=0)

                    booklabel = Label(climate2, text='CLIMATE', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                    booklabel.place(x=390, y=35)

                    ##---------------------------------------------------

                    apple_image = Image.open("hot.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(climate2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=80, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("cold.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(climate2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=310, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("freezing.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(climate2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=540, y=210)

                    ##---------------------------------------------------

                    # Load the apple image
                    apple_image = Image.open("sunny.png")
                    apple_image = apple_image.resize((200, 200))
                    apple_photo = ImageTk.PhotoImage(apple_image)

                    # Create a label to display the apple image
                    apple_label = Label(climate2, image=apple_photo, bg='white')
                    apple_label.image = apple_photo
                    apple_label.place(x=770, y=210)

                    def back():
                        climate2.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(climate2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    def climate3():
                        climate3 = tk.Toplevel()
                        climate3.geometry('1060x595+250+100')
                        climate3.title('Teachify - For Kids')
                        # Load the sunset image
                        sunset_image = Image.open("COURSES_BG_ICON.jpg")
                        sunset_image = sunset_image.resize((1050, 595))
                        sunset_photo = ImageTk.PhotoImage(sunset_image)

                        # Create a label to display the sunset image
                        sunset_label = Label(climate3, image=sunset_photo)
                        sunset_label.image = sunset_photo
                        sunset_label.place(x=0, y=0)

                        booklabel = Label(climate3, text='CLIMATE', font=('castellar', 29, 'bold'), fg='red3',
                                          bg='#fffdf0')
                        booklabel.place(x=390, y=35)

                        ##---------------------------------------------------

                        apple_image = Image.open("foggy.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(climate3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=180, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("windy.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(climate3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=410, y=210)

                        ##---------------------------------------------------

                        # Load the apple image
                        apple_image = Image.open("stormy.png")
                        apple_image = apple_image.resize((200, 200))
                        apple_photo = ImageTk.PhotoImage(apple_image)

                        # Create a label to display the apple image
                        apple_label = Label(climate3, image=apple_photo, bg='white')
                        apple_label.image = apple_photo
                        apple_label.place(x=640, y=210)

                        def back():
                            climate3.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(climate3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                             height=74, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=460)

                        ##---------------------------------------------------

                    nextButton = Button(climate2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=climate3)
                    nextButton.place(x=840, y=480)

                nextButton = Button(climate, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=climate2)
                nextButton.place(x=840, y=480)

            climate_btn = Button(gk, text='CLIMATE', font=('Arial', 20, 'bold'), bd=1,
                                 bg='#ffffff', command=climate)
            climate_btn.place(x=750, y=380)

            #========ANIMALS

            # Initialize Pygame mixer
            pygame.mixer.init()

            def animal():
                animal = tk.Toplevel()
                animal.geometry('1060x595+250+100')
                animal.title('Teachify - For Kids')
                # Load the animal image
                animal_image = Image.open("COURSES_BG_ICON.jpg")
                animal_image = animal_image.resize((1050, 595))
                animal_photo = ImageTk.PhotoImage(animal_image)

                # Create a label to display the animal image
                animal_label = Label(animal, image=animal_photo)
                animal_label.image = animal_photo
                animal_label.place(x=0, y=0)

                booklabel = Label(animal, text='animal', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                booklabel.place(x=390, y=35)

                ##---------------------------------------------------

                animal_image = Image.open("lion.png")
                animal_image = animal_image.resize((200, 200))
                animal_photo = ImageTk.PhotoImage(animal_image)

                # Create a label to display the animal image
                animal_label = Label(animal, image=animal_photo, bg='white')
                animal_label.image = animal_photo
                animal_label.place(x=80, y=210)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("lion.mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(animal, image=animal_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=80, y=210)

                ##---------------------------------------------------

                # Load the animal image
                animal_image = Image.open("DUCK.png")
                animal_image = animal_image.resize((200, 200))
                animal_photo = ImageTk.PhotoImage(animal_image)

                # Create a label to display the animal image
                animal_label = Label(animal, image=animal_photo, bg='white')
                animal_label.image = animal_photo
                animal_label.place(x=310, y=210)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("duck.mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(animal, image=animal_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the animal image
                animal_image = Image.open("GOAT.png")
                animal_image = animal_image.resize((200, 200))
                animal_photo = ImageTk.PhotoImage(animal_image)

                # Create a label to display the animal image
                animal_label = Label(animal, image=animal_photo, bg='white')
                animal_label.image = animal_photo
                animal_label.place(x=540, y=210)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("goat.mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(animal, image=animal_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the animal image
                animal_image = Image.open("DOG.png")
                animal_image = animal_image.resize((200, 200))
                animal_photo = ImageTk.PhotoImage(animal_image)

                # Create a label to display the animal image
                animal_label = Label(animal, image=animal_photo, bg='white')
                animal_label.image = animal_photo
                animal_label.place(x=770, y=210)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("dog.mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(animal, image=animal_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=770, y=210)


                def back():
                    animal.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(animal, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def animal2():
                    animal2 = tk.Toplevel()
                    animal2.geometry('1060x595+250+100')
                    animal2.title('Teachify - For Kids')
                    # Load the animal image
                    animal_image = Image.open("COURSES_BG_ICON.jpg")
                    animal_image = animal_image.resize((1050, 595))
                    animal_photo = ImageTk.PhotoImage(animal_image)

                    # Create a label to display the animal image
                    animal_label = Label(animal2, image=animal_photo)
                    animal_label.image = animal_photo
                    animal_label.place(x=0, y=0)

                    booklabel = Label(animal2, text='animal', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                    booklabel.place(x=390, y=35)

                    ##---------------------------------------------------

                    animal_image = Image.open("CAT.png")
                    animal_image = animal_image.resize((200, 200))
                    animal_photo = ImageTk.PhotoImage(animal_image)

                    # Create a label to display the animal image
                    animal_label = Label(animal2, image=animal_photo, bg='white')
                    animal_label.image = animal_photo
                    animal_label.place(x=80, y=210)

                    # Define function to play audio on button click
                    def play_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("cat.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the zero image
                    zero_button = Button(animal2, image=animal_photo, bg='white', relief=FLAT, bd=0,
                                         highlightthickness=0,
                                         command=play_audio)
                    zero_button.place(x=80, y=210)

                    ##---------------------------------------------------

                    # Load the animal image
                    animal_image = Image.open("ELEPHANT.png")
                    animal_image = animal_image.resize((200, 200))
                    animal_photo = ImageTk.PhotoImage(animal_image)

                    # Create a label to display the animal image
                    animal_label = Label(animal2, image=animal_photo, bg='white')
                    animal_label.image = animal_photo
                    animal_label.place(x=310, y=210)

                    def play_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("elephant.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the zero image
                    zero_button = Button(animal2, image=animal_photo, bg='white', relief=FLAT, bd=0,
                                         highlightthickness=0,
                                         command=play_audio)
                    zero_button.place(x=310, y=210)



                    ##---------------------------------------------------

                    # Load the animal image
                    animal_image = Image.open("SHEEP.png")
                    animal_image = animal_image.resize((200, 200))
                    animal_photo = ImageTk.PhotoImage(animal_image)

                    # Create a label to display the animal image
                    animal_label = Label(animal2, image=animal_photo, bg='white')
                    animal_label.image = animal_photo
                    animal_label.place(x=540, y=210)

                    def play_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("sheep.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the zero image
                    zero_button = Button(animal2, image=animal_photo, bg='white', relief=FLAT, bd=0,
                                         highlightthickness=0,
                                         command=play_audio)
                    zero_button.place(x=540, y=210)



                    ##---------------------------------------------------

                    # Load the animal image
                    animal_image = Image.open("PARROT.png")
                    animal_image = animal_image.resize((200, 200))
                    animal_photo = ImageTk.PhotoImage(animal_image)

                    # Create a label to display the animal image
                    animal_label = Label(animal2, image=animal_photo, bg='white')
                    animal_label.image = animal_photo
                    animal_label.place(x=770, y=210)

                    def play_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("parrot.mp3")
                            pygame.mixer.music.play()

                    # Create a button with the zero image
                    zero_button = Button(animal2, image=animal_photo, bg='white', relief=FLAT, bd=0,
                                         highlightthickness=0,
                                         command=play_audio)
                    zero_button.place(x=770, y=210)

                    def back():
                        animal2.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(animal2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    def animal3():
                        animal3 = tk.Toplevel()
                        animal3.geometry('1060x595+250+100')
                        animal3.title('Teachify - For Kids')
                        # Load the animal image
                        animal_image = Image.open("COURSES_BG_ICON.jpg")
                        animal_image = animal_image.resize((1050, 595))
                        animal_photo = ImageTk.PhotoImage(animal_image)

                        # Create a label to display the animal image
                        animal_label = Label(animal3, image=animal_photo)
                        animal_label.image = animal_photo
                        animal_label.place(x=0, y=0)

                        booklabel = Label(animal3, text='animal', font=('castellar', 29, 'bold'), fg='red3',
                                          bg='#fffdf0')
                        booklabel.place(x=390, y=35)

                        ##---------------------------------------------------

                        animal_image = Image.open("PIG.png")
                        animal_image = animal_image.resize((200, 200))
                        animal_photo = ImageTk.PhotoImage(animal_image)

                        # Create a label to display the animal image
                        animal_label = Label(animal3, image=animal_photo, bg='white')
                        animal_label.image = animal_photo
                        animal_label.place(x=180, y=210)

                        def play_audio():
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.load("pig.mp3")
                                pygame.mixer.music.play()

                        # Create a button with the zero image
                        zero_button = Button(animal3, image=animal_photo, bg='white', relief=FLAT, bd=0,
                                             highlightthickness=0,
                                             command=play_audio)
                        zero_button.place(x=180, y=210)

                        ##---------------------------------------------------

                        # Load the animal image
                        animal_image = Image.open("COW.png")
                        animal_image = animal_image.resize((200, 200))
                        animal_photo = ImageTk.PhotoImage(animal_image)

                        # Create a label to display the animal image
                        animal_label = Label(animal3, image=animal_photo, bg='white')
                        animal_label.image = animal_photo
                        animal_label.place(x=410, y=210)

                        def play_audio():
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.load("cow.mp3")
                                pygame.mixer.music.play()

                        # Create a button with the zero image
                        zero_button = Button(animal3, image=animal_photo, bg='white', relief=FLAT, bd=0,
                                             highlightthickness=0,
                                             command=play_audio)
                        zero_button.place(x=410, y=210)

                        ##---------------------------------------------------

                        # Load the animal image
                        animal_image = Image.open("MONKEY.png")
                        animal_image = animal_image.resize((200, 200))
                        animal_photo = ImageTk.PhotoImage(animal_image)

                        # Create a label to display the animal image
                        animal_label = Label(animal3, image=animal_photo, bg='white')
                        animal_label.image = animal_photo
                        animal_label.place(x=640, y=210)

                        def play_audio():
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.load("monkey.mp3")
                                pygame.mixer.music.play()

                        # Create a button with the zero image
                        zero_button = Button(animal3, image=animal_photo, bg='white', relief=FLAT, bd=0,
                                             highlightthickness=0,
                                             command=play_audio)
                        zero_button.place(x=640, y=210)

                        def back():
                            animal3.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(animal3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                             height=74, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=460)

                        ##---------------------------------------------------

                    nextButton = Button(animal2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=animal3)
                    nextButton.place(x=840, y=480)

                nextButton = Button(animal, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=animal2)
                nextButton.place(x=840, y=480)

            animal_btn = Button(gk, text='animal', font=('Arial', 20, 'bold'), bd=1,
                                bg='#ffffff', command=animal)
            animal_btn.place(x=620, y=450)


            #========instruments

            # Initialize Pygame mixer
            pygame.mixer.init()

            def instrument():
                instrument = tk.Toplevel()
                instrument.geometry('1060x595+250+100')
                instrument.title('Teachify - For Kids')
                # Load the instrument image
                instrument_image = Image.open("COURSES_BG_ICON.jpg")
                instrument_image = instrument_image.resize((1050, 595))
                instrument_photo = ImageTk.PhotoImage(instrument_image)

                # Create a label to display the instrument image
                instrument_label = Label(instrument, image=instrument_photo)
                instrument_label.image = instrument_photo
                instrument_label.place(x=0, y=0)

                booklabel = Label(instrument, text='instrument', font=('castellar', 29, 'bold'), fg='red3',
                                  bg='#fffdf0')
                booklabel.place(x=390, y=35)

                ##---------------------------------------------------

                instrument_image = Image.open("FRENCH HORN.png")
                instrument_image = instrument_image.resize((200, 200))
                instrument_photo = ImageTk.PhotoImage(instrument_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("french horn.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(instrument, image=instrument_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = instrument_photo
                apple_button.place(x=80, y=210)


                ##---------------------------------------------------

                # Load the instrument image
                instrument_image = Image.open("UKULELE.png")
                instrument_image = instrument_image.resize((200, 200))
                instrument_photo = ImageTk.PhotoImage(instrument_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("ukulele.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(instrument, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                      highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = instrument_photo
                apple_button.place(x=310, y=210)

                ##---------------------------------------------------

                # Load the instrument image
                instrument_image = Image.open("SAXOPHONE.png")
                instrument_image = instrument_image.resize((200, 200))
                instrument_photo = ImageTk.PhotoImage(instrument_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("saxophone.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(instrument, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                      highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = instrument_photo
                apple_button.place(x=540, y=210)

                ##---------------------------------------------------

                # Load the instrument image
                instrument_image = Image.open("GRAND PIANO.png")
                instrument_image = instrument_image.resize((200, 200))
                instrument_photo = ImageTk.PhotoImage(instrument_image)

                # Define function to play audio on button click
                def play_apple_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("piano.mp3")
                        pygame.mixer.music.play()

                apple_button = Button(instrument, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                      highlightthickness=0,
                                      command=play_apple_audio)
                apple_button.image = instrument_photo
                apple_button.place(x=770, y=210)

                def back():
                    instrument.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(instrument, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def instrument2():
                    instrument2 = tk.Toplevel()
                    instrument2.geometry('1060x595+250+100')
                    instrument2.title('Teachify - For Kids')
                    # Load the instrument image
                    instrument_image = Image.open("COURSES_BG_ICON.jpg")
                    instrument_image = instrument_image.resize((1050, 595))
                    instrument_photo = ImageTk.PhotoImage(instrument_image)

                    # Create a label to display the instrument image
                    instrument_label = Label(instrument2, image=instrument_photo)
                    instrument_label.image = instrument_photo
                    instrument_label.place(x=0, y=0)

                    booklabel = Label(instrument2, text='instrument', font=('castellar', 29, 'bold'), fg='red3',
                                      bg='#fffdf0')
                    booklabel.place(x=390, y=35)

                    ##---------------------------------------------------

                    instrument_image = Image.open("DRUMS.png")
                    instrument_image = instrument_image.resize((200, 200))
                    instrument_photo = ImageTk.PhotoImage(instrument_image)

                    # Define function to play audio on button click
                    def play_apple_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("drums.mp3")
                            pygame.mixer.music.play()

                    apple_button = Button(instrument2, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0,
                                          command=play_apple_audio)
                    apple_button.image = instrument_photo
                    apple_button.place(x=80, y=210)

                    ##---------------------------------------------------

                    # Load the instrument image
                    instrument_image = Image.open("DOUBLE BASS.png")
                    instrument_image = instrument_image.resize((200, 200))
                    instrument_photo = ImageTk.PhotoImage(instrument_image)

                    def play_apple_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("double bass.mp3")
                            pygame.mixer.music.play()

                    apple_button = Button(instrument2, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0,
                                          command=play_apple_audio)
                    apple_button.image = instrument_photo
                    apple_button.place(x=310, y=210)

                    ##---------------------------------------------------

                    # Load the instrument image
                    instrument_image = Image.open("TROMBONE.png")
                    instrument_image = instrument_image.resize((200, 200))
                    instrument_photo = ImageTk.PhotoImage(instrument_image)

                    def play_apple_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("trombone.mp3")
                            pygame.mixer.music.play()

                    apple_button = Button(instrument2, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0,
                                          command=play_apple_audio)
                    apple_button.image = instrument_photo
                    apple_button.place(x=540, y=210)

                    ##---------------------------------------------------

                    # Load the instrument image
                    instrument_image = Image.open("TRUMPET.png")
                    instrument_image = instrument_image.resize((200, 200))
                    instrument_photo = ImageTk.PhotoImage(instrument_image)

                    def play_apple_audio():
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.load("trumpet.mp3")
                            pygame.mixer.music.play()

                    apple_button = Button(instrument2, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                          highlightthickness=0,
                                          command=play_apple_audio)
                    apple_button.image = instrument_photo
                    apple_button.place(x=770, y=210)

                    def back():
                        instrument2.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(instrument2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    def instrument3():
                        instrument3 = tk.Toplevel()
                        instrument3.geometry('1060x595+250+100')
                        instrument3.title('Teachify - For Kids')
                        # Load the instrument image
                        instrument_image = Image.open("COURSES_BG_ICON.jpg")
                        instrument_image = instrument_image.resize((1050, 595))
                        instrument_photo = ImageTk.PhotoImage(instrument_image)

                        # Create a label to display the instrument image
                        instrument_label = Label(instrument3, image=instrument_photo)
                        instrument_label.image = instrument_photo
                        instrument_label.place(x=0, y=0)

                        booklabel = Label(instrument3, text='instrument', font=('castellar', 29, 'bold'), fg='red3',
                                          bg='#fffdf0')
                        booklabel.place(x=390, y=35)

                        ##---------------------------------------------------

                        instrument_image = Image.open("MANDOLIN.png")
                        instrument_image = instrument_image.resize((200, 200))
                        instrument_photo = ImageTk.PhotoImage(instrument_image)

                        def play_apple_audio():
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.load("mandolin.mp3")
                                pygame.mixer.music.play()

                        apple_button = Button(instrument3, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                              highlightthickness=0,
                                              command=play_apple_audio)
                        apple_button.image = instrument_photo
                        apple_button.place(x=180, y=210)

                        ##---------------------------------------------------

                        # Load the instrument image
                        instrument_image = Image.open("CLASSICAL GUITAR.png")
                        instrument_image = instrument_image.resize((200, 200))
                        instrument_photo = ImageTk.PhotoImage(instrument_image)

                        def play_apple_audio():
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.load("GUITAR.mp3")
                                pygame.mixer.music.play()

                        apple_button = Button(instrument3, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                              highlightthickness=0,
                                              command=play_apple_audio)
                        apple_button.image = instrument_photo
                        apple_button.place(x=410, y=210)

                        ##---------------------------------------------------

                        # Load the instrument image
                        instrument_image = Image.open("VIOLOIN.png")
                        instrument_image = instrument_image.resize((200, 200))
                        instrument_photo = ImageTk.PhotoImage(instrument_image)



                        def play_apple_audio():
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.load("violin.mp3")
                                pygame.mixer.music.play()

                        apple_button = Button(instrument3, image=instrument_photo, bg='white', relief=FLAT, bd=0,
                                              highlightthickness=0,
                                              command=play_apple_audio)
                        apple_button.image = instrument_photo
                        apple_button.place(x=640, y=210)


                        def back():
                            instrument3.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(instrument3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                             height=74, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=460)

                        ##---------------------------------------------------

                    nextButton = Button(instrument2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=instrument3)
                    nextButton.place(x=840, y=480)

                nextButton = Button(instrument, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=instrument2)
                nextButton.place(x=840, y=480)

            instrument_btn = Button(gk, text='INSTRUMENTS', font=('Arial', 20, 'bold'), bd=1,
                                    bg='#ffffff', command=instrument)
            instrument_btn.place(x=510, y=380)

            def festival():
                festival = tk.Toplevel()
                festival.geometry('1060x595+250+100')
                festival.title('Teachify - For Kids')
                # Load the festival image
                festival_image = Image.open("COURSES_BG_ICON.jpg")
                festival_image = festival_image.resize((1050, 595))
                festival_photo = ImageTk.PhotoImage(festival_image)

                # Create a label to display the festival image
                festival_label = Label(festival, image=festival_photo)
                festival_label.image = festival_photo
                festival_label.place(x=0, y=0)

                booklabel = Label(festival, text='festival', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
                booklabel.place(x=390, y=35)

                ##---------------------------------------------------

                festival_image = Image.open("diwali.png")
                festival_image = festival_image.resize((200, 200))
                festival_photo = ImageTk.PhotoImage(festival_image)

                # Create a label to display the festival image
                festival_label = Label(festival, image=festival_photo, bg='white')
                festival_label.image = festival_photo
                festival_label.place(x=80, y=210)

                festival_label = Label(festival, text='DIWALI', font=('castellar', 14, 'bold'), fg='red3', bg='#fffdf0')
                festival_label.place(x=100, y=430)
                ##---------------------------------------------------

                # Load the festival image
                festival_image = Image.open("holi.png")
                festival_image = festival_image.resize((200, 200))
                festival_photo = ImageTk.PhotoImage(festival_image)

                # Create a label to display the festival image
                festival_label = Label(festival, image=festival_photo, bg='white')
                festival_label.image = festival_photo
                festival_label.place(x=310, y=210)

                festival_label = Label(festival, text='HOLI', font=('castellar', 14, 'bold'), fg='red3',
                                       bg='#fffdf0')
                festival_label.place(x=340, y=430)

                ##---------------------------------------------------

                # Load the festival image
                festival_image = Image.open("makarsankranti.png")
                festival_image = festival_image.resize((200, 200))
                festival_photo = ImageTk.PhotoImage(festival_image)

                # Create a label to display the festival image
                festival_label = Label(festival, image=festival_photo, bg='white')
                festival_label.image = festival_photo
                festival_label.place(x=540, y=210)

                festival_label = Label(festival, text='MAKARSANKRANTI', font=('castellar', 14, 'bold'), fg='red3',
                                       bg='#fffdf0')
                festival_label.place(x=540, y=430)
                ##---------------------------------------------------

                # Load the festival image
                festival_image = Image.open("Christmas-Day.png")
                festival_image = festival_image.resize((200, 200))
                festival_photo = ImageTk.PhotoImage(festival_image)

                # Create a label to display the festival image
                festival_label = Label(festival, image=festival_photo, bg='white')
                festival_label.image = festival_photo
                festival_label.place(x=770, y=210)
                festival_label = Label(festival, text='CHRISTMAS', font=('castellar', 14, 'bold'), fg='red3',
                                       bg='#fffdf0')
                festival_label.place(x=795, y=430)

                def back():
                    festival.destroy()

                back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                back_button = Button(festival, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                     height=74, width=76)
                back_button.image = back_button_image
                back_button.place(x=60, y=460)

                def festival2():
                    festival2 = tk.Toplevel()
                    festival2.geometry('1060x595+250+100')
                    festival2.title('Teachify - For Kids')
                    # Load the festival image
                    festival_image = Image.open("COURSES_BG_ICON.jpg")
                    festival_image = festival_image.resize((1050, 595))
                    festival_photo = ImageTk.PhotoImage(festival_image)

                    # Create a label to display the festival image
                    festival_label = Label(festival2, image=festival_photo)
                    festival_label.image = festival_photo
                    festival_label.place(x=0, y=0)

                    booklabel = Label(festival2, text='festival', font=('castellar', 29, 'bold'), fg='red3',
                                      bg='#fffdf0')
                    booklabel.place(x=390, y=35)

                    ##---------------------------------------------------

                    festival_image = Image.open("Bhai-Dooj.png")
                    festival_image = festival_image.resize((200, 200))
                    festival_photo = ImageTk.PhotoImage(festival_image)

                    # Create a label to display the festival image
                    festival_label = Label(festival2, image=festival_photo, bg='white')
                    festival_label.image = festival_photo
                    festival_label.place(x=80, y=210)

                    festival_label = Label(festival2, text='BHAI DOOJ', font=('castellar', 14, 'bold'), fg='red3',
                                           bg='#fffdf0')
                    festival_label.place(x=80, y=430)

                    ##---------------------------------------------------

                    # Load the festival image
                    festival_image = Image.open("pongal.png")
                    festival_image = festival_image.resize((200, 200))
                    festival_photo = ImageTk.PhotoImage(festival_image)

                    # Create a label to display the festival image
                    festival_label = Label(festival2, image=festival_photo, bg='white')
                    festival_label.image = festival_photo
                    festival_label.place(x=310, y=210)

                    festival_label = Label(festival2, text='PONGAL', font=('castellar', 14, 'bold'), fg='red3',
                                           bg='#fffdf0')
                    festival_label.place(x=320, y=430)

                    ##---------------------------------------------------

                    # Load the festival image
                    festival_image = Image.open("Guru-Purnima.png")
                    festival_image = festival_image.resize((200, 200))
                    festival_photo = ImageTk.PhotoImage(festival_image)

                    # Create a label to display the festival image
                    festival_label = Label(festival2, image=festival_photo, bg='white')
                    festival_label.image = festival_photo
                    festival_label.place(x=540, y=210)

                    festival_label = Label(festival2, text='GURU PURNIMA', font=('castellar', 14, 'bold'), fg='red3',
                                           bg='#fffdf0')
                    festival_label.place(x=540, y=430)

                    ##---------------------------------------------------

                    # Load the festival image
                    festival_image = Image.open("hallowen.png")
                    festival_image = festival_image.resize((200, 200))
                    festival_photo = ImageTk.PhotoImage(festival_image)

                    # Create a label to display the festival image
                    festival_label = Label(festival2, image=festival_photo, bg='white')
                    festival_label.image = festival_photo
                    festival_label.place(x=770, y=210)

                    festival_label = Label(festival2, text='HALLOWEN', font=('castellar', 14, 'bold'), fg='red3',
                                           bg='#fffdf0')
                    festival_label.place(x=795, y=430)

                    def back():
                        festival2.destroy()

                    back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                    back_button = Button(festival2, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                         height=74, width=76)
                    back_button.image = back_button_image
                    back_button.place(x=60, y=460)

                    def festival3():
                        festival3 = tk.Toplevel()
                        festival3.geometry('1060x595+250+100')
                        festival3.title('Teachify - For Kids')
                        # Load the festival image
                        festival_image = Image.open("COURSES_BG_ICON.jpg")
                        festival_image = festival_image.resize((1050, 595))
                        festival_photo = ImageTk.PhotoImage(festival_image)

                        # Create a label to display the festival image
                        festival_label = Label(festival3, image=festival_photo)
                        festival_label.image = festival_photo
                        festival_label.place(x=0, y=0)

                        booklabel = Label(festival3, text='festival', font=('castellar', 29, 'bold'), fg='red3',
                                          bg='#fffdf0')
                        booklabel.place(x=390, y=35)

                        ##---------------------------------------------------

                        festival_image = Image.open("DUSSERA.png")
                        festival_image = festival_image.resize((200, 200))
                        festival_photo = ImageTk.PhotoImage(festival_image)

                        # Create a label to display the festival image
                        festival_label = Label(festival3, image=festival_photo, bg='white')
                        festival_label.image = festival_photo
                        festival_label.place(x=180, y=210)

                        festival_label = Label(festival3, text='DUSSERA', font=('castellar', 14, 'bold'), fg='red3',
                                               bg='#fffdf0')
                        festival_label.place(x=180, y=430)

                        ##---------------------------------------------------

                        # Load the festival image
                        festival_image = Image.open("RAM NAVMI.png")
                        festival_image = festival_image.resize((200, 200))
                        festival_photo = ImageTk.PhotoImage(festival_image)

                        # Create a label to display the festival image
                        festival_label = Label(festival3, image=festival_photo, bg='white')
                        festival_label.image = festival_photo
                        festival_label.place(x=410, y=210)

                        festival_label = Label(festival3, text='RAM NAVMI', font=('castellar', 14, 'bold'), fg='red3',
                                               bg='#fffdf0')
                        festival_label.place(x=410, y=430)

                        ##---------------------------------------------------

                        # Load the festival image
                        festival_image = Image.open("GANESH CHATURTHI.png")
                        festival_image = festival_image.resize((200, 200))
                        festival_photo = ImageTk.PhotoImage(festival_image)

                        # Create a label to display the festival image
                        festival_label = Label(festival3, image=festival_photo, bg='white')
                        festival_label.image = festival_photo
                        festival_label.place(x=640, y=210)

                        festival_label = Label(festival3, text='GANESH CHATURTHI', font=('castellar', 14, 'bold'),
                                               fg='red3',
                                               bg='#fffdf0')
                        festival_label.place(x=640, y=430)

                        def back():
                            festival3.destroy()

                        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
                        back_button = Button(festival3, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                                             height=74, width=76)
                        back_button.image = back_button_image
                        back_button.place(x=60, y=460)

                        ##---------------------------------------------------

                    nextButton = Button(festival2, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                        activebackground='white',
                                        cursor='hand2', command=festival3)
                    nextButton.place(x=840, y=480)

                nextButton = Button(festival, text='NEXT', font=('castellar', 10, 'bold'), bd=0, bg='white',
                                    activebackground='white',
                                    cursor='hand2', command=festival2)
                nextButton.place(x=840, y=480)

            festival_btn = Button(gk, text='FESTIVALS', font=('Arial', 20, 'bold'), bd=1,
                                  bg='#ffffff', command=festival)
            festival_btn.place(x=310, y=380)



            #======rainbow

            def rainbow():
                rb = tk.Toplevel()
                rb.geometry('1060x595+250+100')
                rb.title('Teachify - For Kids')
                # Load the festival image
                rb_image = Image.open("COURSES_BG_ICON.jpg")
                rb_image = rb_image.resize((1050, 595))
                rb_photo = ImageTk.PhotoImage(rb_image)

                # Create a label to display the festival image
                rb_label = Label(rb, image=rb_photo)
                rb_label.image = rb_photo
                rb_label.place(x=0, y=0)

                rb_label = Label(rb, text='RAINBOW', font=('castellar', 29, 'bold'), fg='red3',
                                 bg='#fffdf0')
                rb_label.place(x=390, y=35)
                # Create seven buttons for the colors of the rainbow
                button1 = tk.Button(rb, text="Violet", bg="violet", font=('Arial', 20, 'bold'), bd=1)
                button2 = tk.Button(rb, text="Indigo", bg="indigo", font=('Arial', 20, 'bold'), bd=1)
                button3 = tk.Button(rb, text="Blue", bg="blue", font=('Arial', 20, 'bold'), bd=1)
                button4 = tk.Button(rb, text="Green", bg="green", font=('Arial', 20, 'bold'), bd=1)
                button5 = tk.Button(rb, text="Yellow", bg="yellow", font=('Arial', 20, 'bold'), bd=1)
                button6 = tk.Button(rb, text="Orange", bg="orange", font=('Arial', 20, 'bold'), bd=1)
                button7 = tk.Button(rb, text="Red", bg="red", font=('Arial', 20, 'bold'), bd=1)

                # Pack the buttons into the window
                button1.place(x=400, y=175)
                button2.place(x=600, y=175)
                button3.place(x=400, y=275)
                button4.place(x=600, y=275)
                button5.place(x=400, y=375)
                button6.place(x=600, y=375)
                button7.place(x=500, y=475)

            rb_btn = Button(gk, text="RAINBOW", font=('Arial', 20, 'bold'), bg='#ffffff', bd=1, command=rainbow)
            rb_btn.place(x=440,y = 170)
            ######################################DAY_OF_WEEK#############################################################
            def day_week():
                Day_week = tk.Toplevel()
                Day_week.geometry('1060x595+250+100')
                Day_week.title('Teachify - For Kids')
                # Load the festival image
                Day_week_image = Image.open("COURSES_BG_ICON.jpg")
                Day_week_image = Day_week_image.resize((1050, 595))
                Day_week_photo = ImageTk.PhotoImage(Day_week_image)

                # Create a label to display the festival image
                Day_week_label = Label(Day_week, image=Day_week_photo)
                Day_week_label.image = Day_week_photo
                Day_week_label.place(x=0, y=0)

                day_label = Label(Day_week, text='DAYS OF WEEK', font=('castellar', 29, 'bold'), fg='red3',
                                  bg='#fffdf0')
                day_label.place(x=360, y=35)

                mon_day = Button(Day_week, text="Monday", font=('Arial', 20, 'bold'), bd=1)
                mon_day.place(x=100, y=200)

                tues_day = Button(Day_week, text="Tuesday", font=('Arial', 20, 'bold'), bd=1)
                tues_day.place(x=450, y=200)

                wednes_day = Button(Day_week, text="Wednesday", font=('Arial', 20, 'bold'), bd=1)
                wednes_day.place(x=800, y=200)

                thurs_day = Button(Day_week, text="Thursday", font=('Arial', 20, 'bold'), bd=1)
                thurs_day.place(x=100, y=300)

                fri_day = Button(Day_week, text="Friday", font=('Arial', 20, 'bold'), bd=1)
                fri_day.place(x=450, y=300)

                satur_day = Button(Day_week, text="Saturday", font=('Arial', 20, 'bold'), bd=1)
                satur_day.place(x=820, y=300)

                sun_day = Button(Day_week, text="Sunday", font=('Arial', 20, 'bold'), bd=1)
                sun_day.place(x=450, y=450)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(Day_week, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=400)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("days of week.mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(Day_week, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=400)

            day_week_btn = Button(gk, text="Days of Week", font=('Arial', 20, 'bold'), bg='#ffffff', bd=1,
                                  command=day_week)
            day_week_btn.place(x=220, y=450)

            ###############################MONTH_OF_YR############################################
            def month_year():
                month_year = tk.Toplevel()
                month_year.geometry('1060x595+250+100')
                month_year.title('Teachify - For Kids')
                # Load the festival image
                month_year_image = Image.open("COURSES_BG_ICON.jpg")
                month_year_image = month_year_image.resize((1050, 595))
                month_year_photo = ImageTk.PhotoImage(month_year_image)

                # Create a label to display the festival image
                month_year_label = Label(month_year, image=month_year_photo)
                month_year_label.image = month_year_photo
                month_year_label.place(x=0, y=0)

                yr_label = Label(month_year, text='MONTH OF YEAR', font=('castellar', 29, 'bold'), fg='red3',
                                 bg='#fffdf0')
                yr_label.place(x=320, y=35)

                Jan_month = Button(month_year, text="January", font=('Arial', 20, 'bold'), bd=1)
                Jan_month.place(x=250, y=160)

                feb_month = Button(month_year, text="February", font=('Arial', 20, 'bold'), bd=1)
                feb_month.place(x=500, y=160)

                mar_month = Button(month_year, text="March", font=('Arial', 20, 'bold'), bd=1)
                mar_month.place(x=750, y=160)

                Apr_month = Button(month_year, text="April", font=('Arial', 20, 'bold'), bd=1)
                Apr_month.place(x=250, y=260)

                may_month = Button(month_year, text="May", font=('Arial', 20, 'bold'), bd=1)
                may_month.place(x=500, y=260)

                june_month = Button(month_year, text="June", font=('Arial', 20, 'bold'), bd=1)
                june_month.place(x=750, y=260)

                July_month = Button(month_year, text="July", font=('Arial', 20, 'bold'), bd=1)
                July_month.place(x=250, y=360)

                aug_month = Button(month_year, text="August", font=('Arial', 20, 'bold'), bd=1)
                aug_month.place(x=500, y=360)

                sept_month = Button(month_year, text="September", font=('Arial', 20, 'bold'), bd=1)
                sept_month.place(x=750, y=360)

                oct_month = Button(month_year, text="October", font=('Arial', 20, 'bold'), bd=1)
                oct_month.place(x=250, y=460)

                nov_month = Button(month_year, text="November", font=('Arial', 20, 'bold'), bd=1)
                nov_month.place(x=500, y=460)

                dec_month = Button(month_year, text="December", font=('Arial', 20, 'bold'), bd=1)
                dec_month.place(x=750, y=460)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(month_year, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("months.mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(month_year, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)

            month_year_btn = Button(gk, text="Months Of Year", font=('Arial', 20, 'bold'), bg='#ffffff', bd=1,
                                    command=month_year)
            month_year_btn.place(x=760, y=450)



        gk_btn = Button(courses, font=('Arial', 20, 'bold'), text="General Knowledge", bg='#ffffff', bd=1, command=gk)
        gk_btn.place(x=275, y=390)

        # -----------------NURSURY POEMS------------------

        # Initialize Pygame mixer
        pygame.mixer.init()
        
        def poems():
            poems = tk.Toplevel()
            poems.geometry('1060x595+250+100')
            poems.title('Teachify - For Kids')

            # Create a frame to hold the image
            image_frame = Frame(poems, bg='white', width=500, height=500)
            image_frame.pack(side=LEFT, padx=0, pady=0)

            # Load the  image
            bg_image = Image.open("COURSES_BG_ICON.png")
            bg_image = bg_image.resize((1050, 595))
            photo = ImageTk.PhotoImage(bg_image)

            # Create a label to display the image
            image_label = Label(image_frame, image=photo, bg='white')
            image_label.image = photo
            image_label.pack()

            poemslabel = Label(poems, text='NURSERY RHYMES', font=('castellar', 29, 'bold'), fg='red3',
                               bg='#fffdf0')
            poemslabel.place(x=320, y=35)

            def poem1():
                poem1 = tk.Toplevel()
                poem1.geometry('1060x595+250+100')
                poem1.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(poem1, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("poem1bg.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()
                text_label = Label(poem1,
                                   text="Twinkle, twinkle, little star,\nHow I wonder what you are.\nUp above the world so high,\nLike a diamond in the sky.",
                                   font=("Bradley Hand", 36), bg='white')
                text_label.place(x=240, y=190)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(poem1, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("Twinkle Twinkle Little star .mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(poem1, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)



            poem1_btn = Button(poems, font=('Arial', 20, 'bold'), text="Twinkle Twinkle Tittle Star", bg='#efd2aa',
                               bd=1,command=poem1)


            poem1_btn.place(x=130, y=190)

            def poem2():
                poem2 = tk.Toplevel()
                poem2.geometry('1060x595+250+100')
                poem2.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(poem2, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("poem2bg.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                text_label = Label(poem2,
                                   text='Jack and Jill went up the hill\nTo fetch a pail of water.\nJack fell down and broke his crow\nAnd Jill came tumbling after.\nThen up got Jack and said to Jill,\nAs in his arms he took her,\n“Brush off that dirt for you’re not hurt,\nLet’s fetch that pail of water.”\nSo Jack and Jill went up the hill\nTo fetch the pail of water,\nAnd took it home to Mother dear,\nWho thanked her son and daughter.',
                                   font=("Bradley Hand", 28), bg='white')
                text_label.place(x=240, y=40)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(poem2, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("Jack And Jill .mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(poem2, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)

            poem2_btn = Button(poems, font=('Arial', 20, 'bold'), text="Jack And Jill", bg='#efd2aa', bd=1,
                               command=poem2)

            poem2_btn.place(x=130, y=260)

            def poem3():
                poem3 = tk.Toplevel()
                poem3.geometry('1060x595+250+100')
                poem3.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(poem3, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("poem3bg.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                text_label = Label(poem3,
                                   text="I'm a little teapot,\nShort and stout,\nHere is my handle\nHere is my spout\nWhen I get all steamed up,\nHear me shout,\nTip me over and pour me out!\nI'm a very special teapot,\nYes, it's true,\nHere's an example of what I can do,\nI can turn my handle into a spout,\nTip me over and pour me out!",
                                   font=("Bradley Hand", 28), bg='white')
                text_label.place(x=240, y=40)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(poem3, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("I'm A Little Teapot .mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(poem3, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)

            poem3_btn = Button(poems, font=('Arial', 20, 'bold'), text="I'm a little teapot", bg='#efd2aa', bd=1,
                               command=poem3)

            poem3_btn.place(x=130, y=330)

            def poem4():
                poem4 = tk.Toplevel()
                poem4.geometry('1060x595+250+100')
                poem4.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(poem4, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("poem4bg.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                text_label = Label(poem4,
                                   text="Humpty Dumpty sat on a wall.\nHumpty Dumpty had a great fall.\nAll the king’s horses and all the king’s men\ncouldn’t put Humpty together again.\nHumpty Dumpty sat on a wall.\nHumpty Dumpty had a great fall.\nAll the king’s horses and all the king’s men\ncouldn’t put Humpty together again.\nHumpty Dumpty sat on a wall.\nHumpty Dumpty had a great fall.\nAll the king’s horses and all the king’s men\ncouldn’t put Humpty together again.",
                                   font=("Bradley Hand", 28), bg='white')
                text_label.place(x=200, y=40)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(poem4, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("Humpty Dumpty .mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(poem4, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)

            poem4_btn = Button(poems, font=('Arial', 20, 'bold'), text="Humpty Dumpty", bg='#efd2aa', bd=1,
                               command=poem4)

            poem4_btn.place(x=130, y=400)

            def poem5():
                poem5 = tk.Toplevel()
                poem5.geometry('1060x595+250+100')
                poem5.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(poem5, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("poem5bg.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                text_label = Label(poem5,
                                   text="Ring-a-ring-a-rosies\nA pocket full of posies\nA tissue, a tissue\nWe all fall down\nThe king has sent his daughter\nTo fetch a pail of water\nA tissue, a tissue\nWe all fall down\nThe robin on the steeple\nIs singing to the people\nA tissue, a tissue\nWe all fall down\nThe wedding bells are ringing\nThe boys and girls are singing\nA tissue, a tissue\nWe all fall down",
                                   font=("Bradley Hand", 24), bg='white')
                text_label.place(x=290, y=7)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(poem5, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("evokids - Ring Around The Rosie.mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(poem5, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)

            poem5_btn = Button(poems, font=('Arial', 20, 'bold'), text="Ring around the roses", bg='#efd2aa', bd=1,
                               command=poem5)

            poem5_btn.place(x=600, y=190)

            def poem6():
                poem6 = tk.Toplevel()
                poem6.geometry('1060x595+250+100')
                poem6.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(poem6, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("poem6bg.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                text_label = Label(poem6,
                                   text="Row, row, row your boat\nGently down the stream\nMerrily merrily, merrily, merrily\nLife is but a dream\nRow, row, row your boat\nGently down the stream\nMerrily merrily, merrily, merrily\nLife is but a dream\nRow, row, row your boat\nGently down the stream\nMerrily merrily, merrily, merrily\nLife is but a dream\nRow, row, row your boat\nGently down the stream\nMerrily merrily, merrily, merrily\nLife is but a dream",
                                   font=("Bradley Hand", 22), bg='white')
                text_label.place(x=290, y=10)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(poem6, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("Row Row Row Your Boat .mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(poem6, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)

            poem6_btn = Button(poems, font=('Arial', 20, 'bold'), text="Row,Row,Row your boat.", bg='#efd2aa', bd=1,
                               command=poem6)

            poem6_btn.place(x=600, y=260)

            def poem8():
                poem8 = tk.Toplevel()
                poem8.geometry('1060x595+250+100')
                poem8.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(poem8, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("poem8bg.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                text_label = Label(poem8,
                                   text="Baa, baa black sheep\nHave you any wool\nYes sir, yes sir\nThree bags full.\n\nOne for my master\nAnd one for my dame\nAnd one for the little boy\nWho lives down the lane",
                                   font=("Bradley Hand", 26), bg='white')
                text_label.place(x=320, y=100)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(poem8, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("BAA BAA BLACK SHEEP .mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(poem8, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)

            poem8_btn = Button(poems, font=('Arial', 20, 'bold'), text="Baa Baa Black Sheep.", bg='#efd2aa', bd=1,
                               command=poem8)

            poem8_btn.place(x=600, y=330)

            def poem7():
                poem7 = tk.Toplevel()
                poem7.geometry('1060x595+250+100')
                poem7.title('Teachify - For Kids')

                # Create a frame to hold the image
                image_frame = Frame(poem7, bg='white', width=500, height=500)
                image_frame.pack(side=LEFT, padx=0, pady=0)

                # Load the  image
                bg_image = Image.open("poem7bg.png")
                bg_image = bg_image.resize((1050, 595))
                photo = ImageTk.PhotoImage(bg_image)

                # Create a label to display the image
                image_label = Label(image_frame, image=photo, bg='white')
                image_label.image = photo
                image_label.pack()

                text_label = Label(poem7,
                                   text="Incy wincy spider\nclimbed up the water spout,\nDown came the rain\nand washed poor Wincy out,\n\nOut came the sun shine\nand dried up all the rain,\nAnd Incy Wincy spider\nclimbed up the spout again.",
                                   font=("Bradley Hand", 26), bg='white')
                text_label.place(x=320, y=100)

                zero_image = Image.open("speak.png")
                zero_image = zero_image.resize((56, 56))
                zero_photo = ImageTk.PhotoImage(zero_image)

                # Create a label to display the zero image
                zero_label = Label(poem7, image=zero_photo)
                zero_label.image = zero_photo
                zero_label.place(x=100, y=200)

                # Define function to play audio on button click
                def play_audio():
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.load("Incy Wincy Spider .mp3")
                        pygame.mixer.music.play()

                # Create a button with the zero image
                zero_button = Button(poem7, image=zero_photo, bg='white', relief=FLAT, bd=0, highlightthickness=0,
                                     command=play_audio)
                zero_button.place(x=100, y=200)

            poem7_btn = Button(poems, font=('Arial', 20, 'bold'), text="Incy Wincy spider.", bg='#efd2aa', bd=1,
                               command=poem7)

            poem7_btn.place(x=600, y=400)
















        poems_btn = Button(courses, font=('Arial', 20, 'bold'), text="POEMS", bg='#ffffff', bd=1,
                           command=poems)
        poems_btn.place(x=345, y=310)

    courses_btn = Button(seven_eleven, text='COURSES', font=('Arial', 20, 'bold'), bd=1, bg='#efd2aa',
                         command=courses_page1)
    courses_btn.place(x=450, y=170)

    #############################---------------------------DICTONARY----------------------------####################################################
    def dict():
        dictionary = tk.Toplevel()
        dictionary.geometry('1060x595+250+100')
        dictionary.title('Teachify - For Kids')
        # Create a frame to hold the image
        image_frame = Frame(dictionary, bg='white', width=500, height=500)
        image_frame.pack(side=LEFT, padx=0, pady=0)

        # Load the image
        bg_image = Image.open("COURSES_BG_ICON.png")
        bg_image = bg_image.resize((1050, 595))
        photo = ImageTk.PhotoImage(bg_image)

        # Create a label to display the image
        image_label = Label(image_frame, image=photo, bg='white')
        image_label.image = photo
        image_label.pack()

        dictlabel = Label(dictionary, text='DICTIONARY', font=('castellar', 29, 'bold'), fg='red3', bg='#fffdf0')
        dictlabel.place(x=395, y=35)

        # ----ENTER WORD-------#
        enterwordLabel = Label(dictionary, text='Enter Word', font=('castellar', 18, 'bold'), fg='red3', bg='#fff7ea')
        enterwordLabel.place(x=430, y=160)

        # -----ENTER WORD TEXTFIELD-----#
        enterwordentry = Entry(dictionary, font=('arial', 18, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
        enterwordentry.place(x=390, y=200)

        def back():
            dictionary.destroy()

        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
        back_button = Button(dictionary, image=back_button_image, bd=0, bg='#fff7ea', command=back,
                             height=74, width=76)
        back_button.image = back_button_image
        back_button.place(x=60, y=460)

        # -------SEARCH BUTTON-------#
        def search():
            data = json.load(open('data.json'))
            word = enterwordentry.get().lower()

            if word in data:
                meaning = data[word]
                textarea.delete(1.0, END)
                for item in meaning:
                    textarea.insert(END, u'\u2022' + item + '\n\n')

            elif len(get_close_matches(word, data.keys())) > 0:
                root.withdraw()
                close_match = get_close_matches(word, data.keys())[0]
                res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')

                if res == True:
                    root.deiconify()
                    enterwordentry.delete(0, END)
                    enterwordentry.insert(END, close_match)
                    meaning = data[close_match]
                    textarea.delete(1.0, END)

                    for item in meaning:
                        textarea.insert(END, u'\u2022' + item + '\n\n')
                        # three_seven.lower()  # bring the root window to front
                        dictionary.focus_force()
                else:
                    textarea.delete(1.0, END)
                    enterwordentry.delete(0, END)
                    messagebox.showerror('Error', 'The word does not exist. Please double-check it.')

            else:
                textarea.delete(1.0, END)
                enterwordentry.delete(0, END)
                messagebox.showerror('Error', 'The word does not exist. Please double-check it.')

        search_button_image = PhotoImage(file='search.gif')
        search_button = Button(dictionary, image=search_button_image, bd=0, command=search, bg='#fff7ea', height=40,
                               width=40)
        search_button.image = search_button_image
        search_button.place(x=450, y=260)

        # ------MIC BUTTON---------#
        def wordaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(enterwordentry.get())
            engine.runAndWait()

        mic_button_image = PhotoImage(file='mic.gif')
        mic_button = Button(dictionary, image=mic_button_image, bd=0, command=wordaudio, bg='#fff7ea', height=40,
                            width=40)
        mic_button.image = mic_button_image
        mic_button.place(x=540, y=260)

        # ----MEANING----#
        meaninglabel = Label(dictionary, text='Meaning', font=('castellar', 18, 'bold'), fg='red3', bg='#fff7ea')
        meaninglabel.place(x=460, y=325)

        # -----ENTER MEANING TEXT FIELD-----#
        textarea = Text(dictionary, font=('arial', 18, 'bold'), height=4, width=50, bd=8, relief=GROOVE, wrap='word')
        textarea.place(x=210, y=355)

        # ---MEANING WALA MIC BUTTON----#
        def meaningaudio():
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(textarea.get(1.0, END))
            engine.runAndWait()

        microphone_button_image = PhotoImage(file='microphone.gif')
        microphone_button = Button(dictionary, image=microphone_button_image, bd=0, command=meaningaudio, bg='#fff7ea',
                                   height=40, width=40)
        microphone_button.image = microphone_button_image
        microphone_button.place(x=370, y=490)

        # ----CLEAR SCREEN BUTTON----#
        def clear():
            textarea.config(state=NORMAL)
            enterwordentry.delete(0, END)
            textarea.delete(1.0, END)

        clear_button_image = PhotoImage(file='clear.gif')
        clear_button = Button(dictionary, image=clear_button_image, bd=0, command=clear, bg='#fff7ea',
                              height=40, width=45)
        clear_button.image = clear_button_image
        clear_button.place(x=500, y=490)

        # -------EXIT BUTTON----------#
        def iexit():
            dictionary.destroy()

        exit_button_image = PhotoImage(file='exit.gif')
        exit_button = Button(dictionary, image=exit_button_image, bd=0, command=iexit, bg='#fff7ea',
                             height=40, width=45)
        exit_button.image = exit_button_image
        exit_button.place(x=610, y=490)

    dict_button = Button(seven_eleven, text='DICTIONARY', font=('Arial', 20, 'bold'), bd=1, command=dict, bg='#efd2aa')
    dict_button.place(x=430, y=240)

    # ###########################################------------------AI---------##################################################################
    # def ai():
    #     ai = Tk()
    #     ai.geometry('500x570+100+30')
    #     ai.title('Teachify')
    #     ai.config(bg='yellow')
    #
    #     data_list = ['What is the capital of India',
    #                  'Delhi is the capital of India',
    #                  'In which language you talk',
    #                  'I mostly talk in english',
    #                  'What you do in free time',
    #                  'I memorize things in my free time',
    #                  'Ok bye',
    #                  'bye take care',
    #                  'what does Devansh love',
    #                  'siuuuu',
    #                  'what lecture is this',
    #                  'python'
    #                  'what does madam say',
    #                  'right'
    #                  ]
    #
    #     bot = ChatBot('Bot')
    #     trainer = ListTrainer(bot)
    #     # for files in os.listdir('data/french/'):
    #     # data=open('data/french/'+files,'r',encoding='utf-8').readlines()
    #
    #     trainer.train(data_list)
    #
    #     def botReply():
    #         question = questionField.get()
    #         question = question.capitalize()
    #         answer = bot.get_response(question)
    #         textarea.insert(END, 'You: ' + question + '\n\n')
    #         textarea.insert(END, 'Bot: ' + str(answer) + '\n\n')
    #         pyttsx3.speak(answer)
    #         questionField.delete(0, END)
    #
    #     def audioToText():
    #         while True:
    #             sr = speech_recognition.Recognizer()
    #             try:
    #                 with speech_recognition.Microphone() as m:
    #                     sr.adjust_for_ambient_noise(m, duration=0.2)
    #                     audio = sr.listen(m)
    #                     query = sr.recognize_google(audio)
    #
    #                     questionField.delete(0, END)
    #                     questionField.insert(0, query)
    #                     botReply()
    #             except Exception as e:
    #                 print(e)
    #
    #     # --------------------------------------ADDING BOT IMAGE-----------------------------------------
    #     # # Load the bot image
    #     # bot_image = Image.open("bot_pic.png")
    #     # bot_image = bot_image.resize((100, 100))
    #     # bot_photo = ImageTk.PhotoImage(bot_image)
    #     #
    #     # # Create a label to display the bot image
    #     # bot_label = Label(ai, image=bot_photo, bg='#fff7ea')
    #     # bot_label.image = bot_photo
    #     # bot_label.pack(pady=5)
    #
    #     # ----------------------------------ADDING SCROLL BAR----------------------------------------------
    #     centerFrame = Frame(ai)
    #     centerFrame.pack(expand=True, fill=BOTH)
    #
    #     scrollbar = Scrollbar(centerFrame)
    #     scrollbar.pack(side=RIGHT)
    #
    #     # -----------------------------------WHITE TEXT AREA------------------------------------------------
    #
    #     textarea = Text(centerFrame, font=('times new roman', 20, 'bold'), height=10, yscrollcommand=scrollbar.set
    #                     , wrap='word')
    #     textarea.pack(side=LEFT)
    #     scrollbar.config(command=textarea.yview)
    #
    #     # ---------------------------------------QUESTION FIELD-------------------------------------------------
    #
    #     questionField = Entry(ai, font=('verdana', 20, 'bold'))
    #     questionField.pack(pady=15, fill=X)
    #
    #     # askPic = PhotoImage(file='ask.png')
    #
    #     # -----------------------------------------------ASK BUTTON------------------------------------------------
    #
    #     askButton = Button(ai, image=askPic, command=botReply)
    #     askButton.pack()
    #
    #     def click(event):
    #         askButton.invoke()
    #
    #     thread = threading.Thread(target=audioToText)
    #     thread.setDaemon(True)
    #     thread.start()
    #
    #     ai.bind('<Return>', click)





    ai_button = Button(seven_eleven, text='AI-BOT', font=('Arial', 20, 'bold'), bd=1, bg='#efd2aa',
                       )
    ai_button.place(x=470, y=315)

    # =======WIKIPEDIA==============================================
    def wik():
        wik = tk.Toplevel()
        wik.geometry('1060x595+250+100')
        wik.title('Teachify - For Kids')
        wik.config(bg='#a8e2fa')

        my_label_frame = LabelFrame(wik, text="Search Wikipedia", font=('arial', 20, 'bold'), bg='#7F7FFF', fg='black')
        my_label_frame.pack(pady=10, padx=10)

        my_entry = Entry(my_label_frame, font=("Helvetica", 18), width=40)
        my_entry.pack(pady=10, padx=20)

        combobox = ttk.Combobox(my_label_frame, font=('times new roman', 18, 'bold'), justify=CENTER, width=15,
                                state='readonly')
        combobox.pack()

        def search():
            question = my_entry.get()
            language = combobox.get()

            for key, value in lang_dict.items():
                if language == value:
                    wikipedia.set_lang(key)

            # wikipedia.set_lang('')
            page = wikipedia.page(question)

            textarea.config(state=NORMAL)
            textarea.insert(END, page.content)
            textarea.config(state=DISABLED)

        lang_dict = googletrans.LANGUAGES
        combobox['values'] = [e for e in lang_dict.values()]
        combobox.set('Select Language')

        search_button = Button(my_label_frame, text="Search", font=("Helvetica", 20, 'bold'), fg="white", bg='red4',
                               command=search)
        search_button.pack(padx=20, pady=10)

        my_frame = Frame(my_label_frame)
        my_frame.pack(pady=2)

        text_scroll = Scrollbar(my_frame)
        text_scroll.pack(side=RIGHT, fill=Y)

        textarea = Text(my_frame, yscrollcommand=text_scroll.set, wrap='word', font=("Helvetica", 20), height=9
                        , bg='#7F7FFF', fg='white', state=DISABLED)
        textarea.pack()

        def clear():
            textarea.config(state=NORMAL)
            textarea.delete(0.0, END)
            textarea.config(state=DISABLED)

            my_entry.delete(0, END)

            combobox.set('Select Language')

        clear_button = Button(wik, text="CLEAR", font=("Helvetica", 20, 'bold'), fg="white", bg='red4'
                              , command=clear)
        clear_button.place(x=490, y=515)

        def back():
            wik.destroy()

        back_button_image = ImageTk.PhotoImage(Image.open("back3.png").resize((50, 50)))
        back_button = Button(wik, image=back_button_image, bd=0, bg='#a8e2fa', command=back,
                             height=74, width=76)
        back_button.image = back_button_image
        back_button.place(x=20, y=510)

    wik_button = Button(seven_eleven, text='WIKIPEDIA', font=('Arial', 20, 'bold'), bd=1, bg='#efd2aa', command=wik)

    wik_button.place(x=440, y=390)


btn7_11y = Button(root, text='7-11 YEARS', font=('Arial', 20, 'bold'), bd=0, relief=GROOVE, fg='white', bg='#1e7922',
                  command=seven_eleven_page)
btn7_11y.place(x=650, y=300)

root.mainloop()
