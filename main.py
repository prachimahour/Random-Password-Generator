import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate a random password
def generate_password():
    length = int(password_length.get())
    level = complexity_var.get()

    if level == 0:
        characters = string.ascii_letters
    elif level == 1:
        characters = string.ascii_letters + string.digits
    elif level == 2:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    generated_password.set(password)

# Function to copy the generated password to the clipboard
def copy_password():
    password_to_copy = generated_password.get()
    if password_to_copy:
        pyperclip.copy(password_to_copy)
        messagebox.showinfo("Copied", "Password copied to clipboard!\n\n" + password_to_copy)
    else:
        messagebox.showwarning("Empty Password", "No password to copy.")


# Create the main app window
app = ctk.CTk()
app.title("Random Password Generator")
app.geometry("400x400")

# Create and place widgets in the window
frame = ctk.CTkFrame(app)
frame.pack(expand=True, fill='both')

length_label = ctk.CTkLabel(frame, text="Password Length:")
length_label.pack()

password_length = ctk.CTkEntry(frame)
password_length.pack()

complexity_label = ctk.CTkLabel(frame, text="Select Complexity:")
complexity_label.pack()

# Use IntVar for complexity level selection
complexity_var = tk.IntVar()
complexity_slider = ctk.CTkSlider(frame, from_=0, to=2, variable=complexity_var)
complexity_slider.pack()

generate_button = ctk.CTkButton(frame, text="Generate Password", command=generate_password)
generate_button.pack()

# Use tk.StringVar for generated password
generated_password = tk.StringVar()

password_label = ctk.CTkLabel(frame, textvariable=generated_password)
password_label.pack()

copy_button = ctk.CTkButton(frame, text="Copy Password", command=copy_password)
copy_button.pack()

# Disable resizing of the window
app.resizable(False, False)

# Start the CustomTkinter main loop
app.mainloop()
