from tkinter import messagebox
from voicemessages import VoiceMessageSender
import ttkbootstrap as tb
from tkinter import Menu
from channel_manager import new_channel, get_channel_names

TOKEN = "your_token_here" # Replace with your token
CHANNEL_ID = 123  # Replace with your channel ID

def refresh_combo():
    combo['values'] = get_channel_names()

master = tb.Window(themename="superhero")
master.title("Discord Voice Message Sender")
master.geometry("800x600")

menu_bar = Menu(master)
master.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Channel", command=lambda: new_channel(master, refresh_combo))

channel_names = get_channel_names()

tb.Label(master, text="Select a Channel").pack(pady=10)
# Combobox (dropdown list)
combo = tb.Combobox(master, values=channel_names, bootstyle="info")
combo.pack(pady=5)

master.mainloop()
# voicemessage = VoiceMessageSender(TOKEN, CHANNEL_ID)
# voicemessage.SendVoiceMessage("D:\path\to\your\audio\file.mp3")

