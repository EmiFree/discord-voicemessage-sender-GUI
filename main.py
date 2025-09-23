from voicemessages import VoiceMessageSender
import tkinter as tk
from tkinter import *

TOKEN = "your_token_here" # Replace with your token
CHANNEL_ID = 123  # Replace with your channel ID

master = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
Label(master, text='Channel Name').grid(row=0)
Label(master, text='Channel ID').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
master.mainloop()
# voicemessage = VoiceMessageSender(TOKEN, CHANNEL_ID)
# voicemessage.SendVoiceMessage("D:\path\to\your\audio\file.mp3")