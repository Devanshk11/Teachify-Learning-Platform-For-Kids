from tkinter import *
from tkvideo import tkvideo

w=Tk()
w.title=("Title")
w.geometry('700x670+200+10')
lblVideo= Label(w)
lblVideo.pack()

player= tkvideo("dsk.mp4",
                lblVideo,
                loop=1,
                size=(1000,1000))

player.play()
w.mainloop()

