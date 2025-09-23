from voicemessages import VoiceMessageSender
import ttkbootstrap as tb
from channel_manager import get_channel_id_by_name, new_channel, get_channel_names
from ttkbootstrap.constants import *
from tkinter import messagebox
from token_manager import get_token, login
from tkinter import filedialog
from file_manager import select_file
channel_names = get_channel_names()
TOKEN = get_token()
file_path = None  # Placeholder for selected file path

def refresh_combo():
    combo['values'] = get_channel_names()

def send_message():
    if not TOKEN:
        messagebox.showerror("Error", "Please login with your Discord token.")
        return
    selected_channel = combo.get()
    if not selected_channel:
        messagebox.showerror("Error", "Please select a channel.")
        return
    if not file_path:
        messagebox.showerror("Error", "Please select an audio file.")
        return
    # Retrieve channel ID from CSV based on selected channel name
    channel_id = get_channel_id_by_name(selected_channel)
    if not channel_id:
        messagebox.showerror("Error", "Selected channel not found.")
        return
    voicemessage = VoiceMessageSender(TOKEN, channel_id)
    voicemessage.SendVoiceMessage(file_path)
    messagebox.showinfo("Success", f"Voice message sent to '{selected_channel}'.")

master = tb.Window(themename="superhero")
master.title("Discord Voice Message Sender")
master.geometry("800x600")

#> Toolbar
toolbar = tb.Frame(master)
toolbar.pack(side="top", fill="x", pady=5)
tb.Button(toolbar, text="Add Channel",
            command=lambda: new_channel(master, refresh_combo),
            bootstyle="success").pack(side="left", padx=5)
tb.Button(toolbar, text="Login",
            command=lambda: login(master), 
            bootstyle="primary").pack(side="left", padx=5)

#> Left Frame (Channel Selection)
left_frame = tb.Frame(master)
left_frame.pack(side="left", padx=10, pady=10, fill="y")
tb.Label(left_frame, text="Select a Channel", anchor="n").pack(fill="x", padx=5, pady=5)
# Combobox (dropdown list)
combo = tb.Combobox(left_frame, values=channel_names, bootstyle="info", width=15)
combo.pack(padx=5, pady=5, anchor="n")

#> Right Frame (File Selection)
right_frame = tb.Frame(master)
right_frame.pack(side="right", padx=10, pady=10, fill="y")
tb.Label(right_frame, text="Select a File", anchor="n").pack(fill="x", padx=5, pady=5)
tb.Button(right_frame, text="Browse", 
            command=select_file, 
            bootstyle="info").pack(padx=5, pady=5, anchor="n")

tb.Button(master, text="Send Voice Message", 
            command=send_message, 
            bootstyle="success").pack(pady=20)
master.mainloop()
# voicemessage = VoiceMessageSender(TOKEN, CHANNEL_ID)
# voicemessage.SendVoiceMessage("D:\path\to\your\audio\file.mp3")

