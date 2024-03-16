from tkinter import *
import tkinter as tk

from tkinter import Frame
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import threading
import speech_recognition


def ai():
    data_list = ['What is the capital of India',
                 'Delhi is the capital of India',
                 'In which language you talk',
                 'I mostly talk in english',
                 'What you do in free time',
                 'I memorize things in my free time',
                 'Ok bye',
                 'bye take care',
                 'what does Devansh love',
                 'siuuuu'
                 ]

    bot = ChatBot('Bot')
    trainer = ListTrainer(bot)
    # for files in os.listdir('data/french/'):
    # data=open('data/french/'+files,'r',encoding='utf-8').readlines()

    trainer.train(data_list)

    def botReply():
        question = questionField.get()
        question = question.capitalize()
        answer = bot.get_response(question)
        textarea.insert(END, 'You: ' + question + '\n\n')
        textarea.insert(END, 'Bot: ' + str(answer) + '\n\n')
        pyttsx3.speak(answer)
        questionField.delete(0, END)

    def audioToText():
        while True:
            sr = speech_recognition.Recognizer()
            try:
                with speech_recognition.Microphone() as m:
                    sr.adjust_for_ambient_noise(m, duration=0.2)
                    audio = sr.listen(m)
                    query = sr.recognize_google(audio)

                    questionField.delete(0, END)
                    questionField.insert(0, query)
                    botReply()
            except Exception as e:
                print(e)

    root = Tk()

    root.geometry('500x570+100+30')
    root.title('Teachify')
    root.config(bg='yellow')

    # --------------------------------------ADDING BOT IMAGE-----------------------------------------



    centerFrame = Frame(root)
    centerFrame.pack()

    # ----------------------------------ADDING SCROLL BAR----------------------------------------------

    scrollbar = Scrollbar(centerFrame)
    scrollbar.pack(side=RIGHT)

    # -----------------------------------WHITE TEXT AREA------------------------------------------------

    textarea = Text(centerFrame, font=('times new roman', 20, 'bold'), height=10, yscrollcommand=scrollbar.set
                    , wrap='word')
    textarea.pack(side=LEFT)
    scrollbar.config(command=textarea.yview)

    # ---------------------------------------QUESTION FIELD-------------------------------------------------

    questionField = Entry(root, font=('verdana', 20, 'bold'))
    questionField.pack(pady=15, fill=X)

    askPic = PhotoImage(file='ask.png')

    # -----------------------------------------------ASK BUTTON------------------------------------------------

    askButton = Button(root, image=askPic, command=botReply)
    askButton.pack()

    def click(event):
        askButton.invoke()

    thread = threading.Thread(target=audioToText)
    thread.setDaemon(True)
    thread.start()

    root.bind('<Return>', click)
    root.mainloop()


root = tk.Tk()
root.geometry('1000x626+250+100')
root.title('Teachify - For Kids')

bot=ChatBot('Bot')
trainer=ListTrainer(bot)
for files in os.listdir('data/english/'):
   data=open('data/english/'+files,'r',encoding='utf-8').readlines()
trainer.train(data)





def search():
    root1=Toplevel()

def hide_indicators():
    dashboard_indicate.config(bg='black')
    courses_indicate.config(bg='black')
    dict_indicate.config(bg='black')
    ai_indicate.config(bg='black')


def indicate(lb):
    hide_indicators()
    lb.config(bg='#158aff')

def add_close_button(window):
    close_btn = tk.Button(window, text='X', bg='red', fg='white',
                          font=('Arial', 20), command=window.destroy)
    close_btn.place(x=660, y=0, width=40, height=40)

def open_dashboard_window():
    dashboard_window = tk.Toplevel(root)
    dashboard_window.geometry('700x626+250+100')
    dashboard_window.title('Teachify - For Kids')
    add_close_button(dashboard_window)


def open_courses_window():
        courses_window = tk.Toplevel(root)
        courses_window.geometry('700x626+250+100')
        courses_window.title('Teachify - For Kids')
        add_close_button(courses_window)

def open_dict_window():
       dict_window = tk.Toplevel(root)
       dict_window.geometry('700x626+250+100')
       dict_window.title('Teachify - For Kids')
       add_close_button(dict_window)






def open_ai_window():
    ai_window = tk.Toplevel(root)
    ai_window.geometry('700x626+250+100')
    ai_window.title('Teachify - For Kids')
    add_close_button(ai_window)







def on_enter(button):
    button.config(bg='#262626')


def on_leave(button):
    button.config(bg='black')


options_frame = tk.Frame(root, bg='black')

dashboard_btn = tk.Button(options_frame, text='Dashboard', font=('Bold', 20), fg='#158aff', bd=0, bg='black',
                          command=lambda: (indicate(dashboard_indicate), open_dashboard_window()))
dashboard_btn.bind("<Enter>", lambda event, b=dashboard_btn: on_enter(b))
dashboard_btn.bind("<Leave>", lambda event, b=dashboard_btn: on_leave(b))
dashboard_btn.place(x=65, y=200)

dashboard_indicate = tk.Label(options_frame, text='', bg='black')
dashboard_indicate.place(x=65, y=200, width=5, height=52)

# ------------------------------------------------------------------------------------------------------------------------
courses_btn = tk.Button(options_frame, text='Courses', font=('Bold', 20), fg='#158aff', bd=0, bg='black',
                        command=lambda: (indicate(courses_indicate),open_courses_window()))
courses_btn.bind("<Enter>", lambda event, b=courses_btn: on_enter(b))

courses_btn.bind("<Leave>", lambda event, b=courses_btn: on_leave(b))
courses_btn.place(x=65, y=300)

courses_indicate = tk.Label(options_frame, text='', bg='black')
courses_indicate.place(x=65, y=300, width=5, height=52)

# ------------------------------------------------------------------------------------------------------------------------

dict_btn = tk.Button(options_frame, text='Dictionary', font=('Bold', 20), fg='#158aff', bd=0, bg='black',
                     command=lambda: open_dict_window())
dict_btn.bind("<Enter>", lambda event, b=dict_btn: on_enter(b))
dict_btn.bind("<Leave>", lambda event, b=dict_btn: on_leave(b))
dict_btn.place(x=65, y=400)

dict_indicate = tk.Label(options_frame, text='', bg='black')
dict_indicate.place(x=65, y=400, width=5, height=52)

# ------------------------------------------------------------------------------------------------------------------------

ai_btn = tk.Button(options_frame, text='AI-ChatBot', font=('Arial', 20), fg='#158aff', bd=0, bg='black',
                   command=ai)

ai_btn.place(x=65, y=500)

ai_indicate = tk.Label(options_frame, text='', bg='black')
ai_indicate.place(x=65, y=500, width=5, height=52)





options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=300, height=800)



root.tk_setPalette('#ccccff')
main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)

#create frames
frame1=Frame(root,height=80,width=1550,bg='#6666ff')
frame1.place(x=0,y=0)


root.mainloop()