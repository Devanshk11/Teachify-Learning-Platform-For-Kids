from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition
import threading









data_list=[ 'What is the capital of India',
            'Delhi is the capital of India',
            'In which language you talk',
            'I mostly talk in english',
            'What you do in free time',
            'I memorize things in my free time',
            'Ok bye',
            'bye take care',
            'what does Devansh love',
            'siuuuu',
            'what lecture is this',
            'python'
            'what does madam say',
            'right'
            ]


bot=ChatBot('Bot')
trainer=ListTrainer(bot)
#for files in os.listdir('data/french/'):
     #data=open('data/french/'+files,'r',encoding='utf-8').readlines()

trainer.train(data_list)

def botReply():
    question=questionField.get()
    question = question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END, 'You: ' + question+'\n\n')
    textarea.insert(END, 'Bot: ' + str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0, END)

def audioToText():
    while True:
        sr=speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone()as m:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio=sr.listen(m)
                query=sr.recognize_google(audio)


                questionField.delete(0,END)
                questionField.insert(0,query)
                botReply()
        except Exception as e:
            print(e)




root=Tk()

root.geometry('500x570+100+30')
root.title('Teachify')
root.config(bg='yellow')



#--------------------------------------ADDING BOT IMAGE-----------------------------------------

logoPic=PhotoImage(file='bot_pic.png')
logoPicLabel=Label(root,image=logoPic,bg='yellow')
logoPicLabel.pack(pady=5)

centerFrame=Frame(root)
centerFrame.pack()

#----------------------------------ADDING SCROLL BAR----------------------------------------------

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

#-----------------------------------WHITE TEXT AREA------------------------------------------------

textarea=Text(centerFrame,font=('times new roman',20,'bold'),height=10,yscrollcommand=scrollbar.set
              ,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

#---------------------------------------QUESTION FIELD-------------------------------------------------

questionField=Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=15,fill=X)

askPic=PhotoImage(file='ask.png')

#-----------------------------------------------ASK BUTTON------------------------------------------------

askButton=Button(root,image=askPic,command=botReply)
askButton.pack()
def click(event):
    askButton.invoke()

thread=threading.Thread(target=audioToText)
thread.setDaemon(True)
thread.start()

root.bind('<Return>',click)
root.mainloop()
