from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
class PasswordGenerator(Tk):
    def __init__(self):
        super().__init__()
        self.config(padx=45, pady=10)
        self.geometry("500x300")
        self.title("password Generator")
        self.value()

    def value(self):

        head = Label(text="PASSWORD GENERATOR", font=("Times new roman", 24, "bold"), background="black", fg="white")
        head.grid(row=0, columnspan=3, column = 0)

        length_label = Label(text="Length:", pady=30, font=("Times new roman", 15, "bold"))
        length_label.grid(row=1)

        self.length_entry = Entry(width=50)
        self.length_entry.grid(row=1, column=1, columnspan=2)
        self.length_entry.focus()

        self.button = Button(text="Generate Password", height=2, command=self.generate_password)
        self.button.grid(row=3, column=1)

        password_label = Label(text="Password:", pady=30,font=("Times new roman", 15, "bold"))
        password_label.grid(row=2)

        self.password_entry = Entry(width=50)
        self.password_entry.grid(row=2, column=1, columnspan=2)


#Password Generator Project
    def generate_password(self):
        get_length = self.length_entry.get()

        if len(get_length) == 0:
            messagebox.showerror(title="error", message="password length should not be empty")
            
        else:
            
            get_length = int(self.length_entry.get())
            password_length = self.password_entry.get()

            if len(password_length) > 0:
                self.password_entry.delete(0, END)

            if get_length < 8:
                messagebox.showwarning(title="warning", message="length of the password should be atleast 8 characters")

            elif get_length > 20:
                messagebox.showwarning(title="warning", message="length of the password should be less than 20")

            else:
                if get_length < 14:
                    letter_len = get_length-4
                    symbol_len = 2
                    number_len = 2
                
                else:
                    letter_len = get_length-8
                    symbol_len = 4
                    number_len = 4

            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','?']

            password_letters = [choice(letters) for _ in range(letter_len)]
            password_symbols = [choice(symbols) for _ in range(symbol_len)]
            password_numbers = [choice(numbers) for _ in range(number_len)]

            password_list = password_letters + password_symbols + password_numbers
            shuffle(password_list)

            password = "".join(password_list)

            self.password_entry.insert(0, password)
            pyperclip.copy(password)

obj = PasswordGenerator()
obj.mainloop()
