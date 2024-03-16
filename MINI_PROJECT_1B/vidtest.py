import tkinter as tk
import tkinter.ttk as ttk

import vlc

def play_video():
    # Create instance of VLC player
    player = vlc.MediaPlayer("C:\\Users\\sumee\\Downloads\\dsk.mp4")

    # Play the video
    player.play()

# Create a window
root = tk.Tk()

# Create a button
play_button = ttk.Button(root, text="Play Video", command=play_video)
play_button.pack()

# Run the window
root.mainloop()

