import csv
from tkinter import filedialog


def select_file():
    global file_path
    new_file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Audio files", "*.mp3 *.ogg *.m4a"), ("All files", "*.*"))
    )
    if new_file_path:
        print("Selected file:", new_file_path)
        file_path = new_file_path

def add_recent_file(file_path):
    recent_files = []
    try:
        with open("recent_files.txt", "r") as f:
            recent_files = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        pass  # No recent files yet

    if file_path not in recent_files:
        recent_files.insert(0, file_path)  # Add to the top
        recent_files = recent_files[:5]  # Keep only the last 5

        with open("recent_files.txt", "w") as f:
            for path in recent_files:
                f.write(path + "\n")
