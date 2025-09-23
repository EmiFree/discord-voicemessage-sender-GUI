from voicemessages import VoiceMessageSender
import ttkbootstrap as tb
from channel_manager import get_channel_id_by_name, new_channel, get_channel_names
from ttkbootstrap.constants import *
from tkinter import messagebox
from token_manager import get_token, login
from tkinter import filedialog
from file_manager import select_file, get_recent_files
channel_names = get_channel_names()
TOKEN = get_token()
file_path = None  # Placeholder for selected file path

def refresh_combo():
    combo['values'] = get_channel_names()
def refresh_file_list():
    recent_files = get_recent_files()
    file_box['values'] = recent_files
        
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

def set_file_path(event):
    global file_path
    file_path = file_box.get()

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
            command=lambda: select_file(refresh_file_list), 
            bootstyle="info").pack(padx=5, pady=5, anchor="n")
file_box = tb.Combobox(right_frame, height=15, width=20, bootstyle="info")
file_box.pack(padx=5, pady=5)
refresh_file_list()
file_box.bind("<<ComboboxSelected>>", set_file_path)

#> Send Button
tb.Button(master, text="Send Voice Message", 
            command=send_message, 
            bootstyle="success").pack(pady=20)


master.mainloop()
# voicemessage = VoiceMessageSender(TOKEN, CHANNEL_ID)
# voicemessage.SendVoiceMessage("D:\path\to\your\audio\file.mp3")

