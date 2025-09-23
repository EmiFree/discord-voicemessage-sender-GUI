from tkinter import messagebox
import ttkbootstrap as tb

def get_token():
    with open("user_token.txt", "r") as f:
        token = f.read().strip()  # Read token, stripping any extra whitespace/newlines
    return token

def save_token(token):
    with open("user_token.txt", "w") as f:
        f.write(token.strip())  # Save token, stripping any extra whitespace/newlines

def login(master):
    popup = tb.Toplevel(master)
    popup.title("Add New Channel")
    popup.geometry("300x200")
    tb.Label(popup, text='Enter Your Discord Token', anchor="center").pack(fill="x", padx=5, pady=5)
    token_box = tb.Entry(popup).pack(fill="x", padx=5, pady=5)
    def get_entry():
        token = token_box.get().strip()
        if token :
            messagebox.showinfo("Success", f"Logged in as: '{token}'")
            save_token(token)
        else:
            messagebox.showwarning("Missing", "Token required.")
    
    tb.Button(popup, text="Submit", command=get_entry).pack(fill="x", padx=5, pady=5)
    
    