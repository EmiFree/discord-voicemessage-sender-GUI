import csv
import os
from tkinter import messagebox
from voicemessages import VoiceMessageSender
import ttkbootstrap as tb

def get_channel_names():
    channel_names = []
    with open("channel_id.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)  # reads using headers
        for row in reader:
            channel_names.append(row["Channel Name"])
    return channel_names

def new_channel_to_csv(channel_name, channel_id):
    file_exists = os.path.isfile("channel_id.csv")
    with open("channel_id.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:   # only write header if new file
            writer.writerow(["Channel Name", "Channel ID"])
        writer.writerow([channel_name, channel_id])

def new_channel(master, refresh_callback):
    popup = tb.Toplevel(master)
    popup.title("Add New Channel")
    popup.geometry("300x200")
    tb.Label(popup, text='Channel Name').grid(row=0)
    tb.Label(popup, text='Channel ID').grid(row=1)
    ch_name = tb.Entry(popup)
    ch_id = tb.Entry(popup)
    ch_name.grid(row=0, column=1)
    ch_id.grid(row=1, column=1)
    def get_entry():
        channel_name = ch_name.get().strip()
        channel_id = ch_id.get().strip()
        if channel_name and channel_id and channel_id.isdigit():
            new_channel_to_csv(channel_name, channel_id)
            messagebox.showinfo("Success", f"Channel '{channel_name}' with ID {channel_id} added.")
            refresh_callback()  # Refresh the combo box in main window
        elif channel_id and not channel_id.isdigit():
            messagebox.showerror("Invalid ID", "Channel ID must be a number.")
        else:
            messagebox.showwarning("Missing", "Both fields required.")
    
    tb.Button(popup, text="Submit", command=get_entry).grid(row=2, columnspan=2, pady=5)
