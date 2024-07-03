import random
import string
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Password Generator")
root.configure(background='lightblue')  

def generate_password(length):
    characters = string.ascii_letters + string.digits
    valid_punctuation = "#$^&*@_!"
    allowed_characters = characters + valid_punctuation
    password = ''.join(random.choices(allowed_characters, k=length))
    return password

def password_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return
        password = generate_password(length)
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

title_label = tk.Label(root, text="Password Generator", bg='lightblue', fg='navy', font=("Helvetica", 16,'bold'))
title_label.pack(pady=(10, 0))

length_label = tk.Label(root, text="Password Length:", bg='lightblue', fg='Black')
length_label.pack(pady=(10, 0))

length_entry = tk.Entry(root, width=20)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=password_button_click, bg='navy', fg='white')
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, text="Generated Password:", bg='lightblue', fg='black')
password_label.pack(pady=(10, 0))

password_entry = tk.Entry(root, textvariable=password_var, width=30, state='readonly')
password_entry.pack()
root.mainloop()
