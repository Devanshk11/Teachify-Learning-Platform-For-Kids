from tkinter import *
from tkinter import ttk
import googletrans
import wikipedia
import pyperclip

def search():
    question=my_entry.get()
    language= combobox.get()

    for key, value in lang_dict.items():
        if language == value:
            wikipedia.set_lang(key)

    #wikipedia.set_lang('')
    page=wikipedia.page(question)

    textarea.config(state=NORMAL)
    textarea.insert(END, page.content)
    textarea.config(state=DISABLED)

def edit():
    textarea.config(state=NORMAL)

def copy():
    content = textarea.get(0.0, END)
    pyperclip.copy(content)

def clear():
    textarea.config(state=NORMAL)
    textarea.delete(0.0, END)
    textarea.config(state=DISABLED)


    my_entry.delete(0, END)

    combobox.set('Select Language')


lang_dict = googletrans.LANGUAGES


root=Tk()
root.geometry('700x670+200+10')
#setting title
root.title('My Wikipedia')
#set color
root.config(bg='#7F7FFF')
 #bgimage = PhotoImage(file='icon_7.gif')
 #bgLabel = Label(root, image=bgimage)
 #bgLabel.place(x=0, y=0)


my_label_frame= LabelFrame(root,text="Search Wikipedia", font=('arial',20,'bold'), bg='brown3', fg='white')
my_label_frame.pack(pady=10, padx=10)

my_entry = Entry(my_label_frame, font=("Helvetica",18), width=40)
my_entry.pack(pady=10, padx=20)

combobox = ttk.Combobox(my_label_frame, font=('times new roman', 18, 'bold'), justify=CENTER, width=15,
                        state='readonly')
combobox.pack()

combobox['values']=[e for e in lang_dict.values()]
combobox.set('Select Language')

search_button = Button(my_label_frame, text="Search", font=("Helvetica", 20, 'bold'), fg="white", bg='red4',
                       command=search)
search_button.pack(padx=20, pady=10)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

textarea= Text(my_frame, yscrollcommand=text_scroll.set, wrap='word', font=("Helvetica", 20), height=12
               , bg='red4', fg='white', state=DISABLED)
textarea.pack()

buttonFrame = Frame(my_label_frame, bg='brown3')
buttonFrame.pack()

edit_button = Button(buttonFrame, text="EDIT", font=("Helvetica", 20, 'bold'), fg="white", bg='red4'
                     ,command=edit)
edit_button.grid(row=0, column=0, padx=20)

copy_button = Button(buttonFrame, text="COPY", font=("Helvetica", 20, 'bold'), fg="white", bg='red4'
                     ,command=copy)
copy_button.grid(row=0, column=1, padx=20)

clear_button = Button(buttonFrame, text="CLEAR", font=("Helvetica", 20, 'bold'), fg="white", bg='red4'
                      ,command=clear)
clear_button.grid(row=0, column=2, padx=20)





root.mainloop()