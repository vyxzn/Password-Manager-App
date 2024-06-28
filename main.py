from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

EMAIL = "exampleemail@email.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)

    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    saved = f"Website: {website} \nUser/Email: {user} \nPassword: {password} \n\n"
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n Email: {user}'
                                                              f'\nPassword: {password} \nIs it ok to save?')
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(saved)
            web_entry_var.set("")
            user_entry_var.set(EMAIL)
            pass_entry_var.set("")
# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND = "#A0937D"
ENTRY_BG = "#FFE9D0"
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND)
window.minsize(500,350)

canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=BACKGROUND, padx=10, pady=10)
website_label.grid(column=0, row=1)

web_entry_var = StringVar()
website_entry = Entry(width=55, textvariable=web_entry_var, bg=ENTRY_BG)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_label = Label(text="Email/Username:", bg=BACKGROUND, padx=10, pady=10)
user_label.grid(column=0, row=2)

user_entry_var = StringVar()
user_entry = Entry(width=55, textvariable=user_entry_var, bg=ENTRY_BG)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, EMAIL)

password_label = Label(text="Password:", bg=BACKGROUND, padx=10, pady=10)
password_label.grid(column=0, row=3)

pass_entry_var = StringVar()
password_entry = Entry(width=36, textvariable=pass_entry_var, bg=ENTRY_BG)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_password, bg=BACKGROUND)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_to_file, bg=BACKGROUND)
add_button.grid(column=1, row=4, columnspan=2)










window.mainloop()