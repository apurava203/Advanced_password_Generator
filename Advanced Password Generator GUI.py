import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_var = tk.IntVar()
        self.length_entry = ttk.Entry(root, textvariable=self.length_var)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.lower_var = tk.IntVar()
        self.lower_check = ttk.Checkbutton(root, text="Include Lowercase", variable=self.lower_var)
        self.lower_check.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W)

        self.upper_var = tk.IntVar()
        self.upper_check = ttk.Checkbutton(root, text="Include Uppercase", variable=self.upper_var)
        self.upper_check.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W)

        self.digits_var = tk.IntVar()
        self.digits_check = ttk.Checkbutton(root, text="Include Digits", variable=self.digits_var)
        self.digits_check.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W)

        self.symbols_var = tk.IntVar()
        self.symbols_check = ttk.Checkbutton(root, text="Include Symbols", variable=self.symbols_var)
        self.symbols_check.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()

        if length <= 0:
            self.result_label.config(text="Please enter a valid password length.")
            return

        characters = ""
        if self.lower_var.get():
            characters += string.ascii_lowercase
        if self.upper_var.get():
            characters += string.ascii_uppercase
        if self.digits_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += string.punctuation

        if not characters:
            self.result_label.config(text="Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_label.config(text="Generated Password: " + password)

        # Copy to clipboard
        pyperclip.copy(password)
        self.result_label.config(text=self.result_label.cget("text") + " (Copied to clipboard)")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
