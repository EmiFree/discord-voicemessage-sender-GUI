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

def help_popup(master):
    help_text = (
        "1. Login with your Discord user token https://www.youtube.com/watch?v=LnBnm_tZlyU\n\n"
        "2. Add channels using the 'Add Channel' button, providing both a name and numeric ID.\n\n"
        "3. Select a channel from the dropdown on the left.\n\n"
        "4. Select an audio file using the 'Browse' button or choose from recent files.\n\n"
        "5. Click 'Send Voice Message' to send the selected audio as a voice message to the chosen channel."
    )
    messagebox.showinfo("Help", help_text)
master = tb.Window(themename="superhero")
master.title("Discord Voice Message Sender")
master.geometry("800x600")

#> Toolbar
toolbar = tb.Frame(master)
toolbar.pack(side="top", fill="x", pady=5)
tb.Button(toolbar, text="Add Channel",
            command=lambda: new_channel(master, refresh_combo),
            bootstyle="primary").pack(side="left", padx=5)
tb.Button(toolbar, text="Login",
            command=lambda: login(master), 
            bootstyle="primary").pack(side="left", padx=5)
tb.Button(toolbar, text="Help",
            command=lambda: help_popup(master), 
            bootstyle="primary").pack(side="left", padx=5)
tb.Button(toolbar, text="Send Voice Message", 
            command=send_message, 
            bootstyle="success").pack(side="left", padx=5)
app_frame = tb.Frame(master)
app_frame.pack(side="bottom", fill="both", expand=True)
#> Left Frame (Channel Selection)
left_frame = tb.Frame(app_frame)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
tb.Label(left_frame, text="Select a Channel", anchor="n").pack(fill="x", padx=5, pady=5)
# Combobox (dropdown list)
combo = tb.Combobox(left_frame, values=channel_names, bootstyle="info", width=15, height=15)
combo.pack(padx=5, pady=5, anchor="n")

#> Right Frame (File Selection)
right_frame = tb.Frame(app_frame)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")
tb.Label(right_frame, text="Select a New File", anchor="n").grid(row=0, column=0, padx=5, pady=5)
tb.Label(right_frame, text="Select a Recent File", anchor="n").grid(row=0, column=1, padx=5, pady=5)
tb.Button(right_frame, text="Browse", 
            command=lambda: select_file(refresh_file_list), 
            bootstyle="info").grid(row=1, column=0, padx=5)
file_box = tb.Combobox(right_frame, height=15, width=20, bootstyle="info")
file_box.grid(row=1, column=1, padx=5)
refresh_file_list()
file_box.bind("<<ComboboxSelected>>", set_file_path)



master.mainloop()

