from tkinter import *
from tkinter import messagebox as mbox, messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    website = website_entry.get().capitalize()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = { website:{
        "user": user,
        "password": password,
        }
    }

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

                website_entry.delete(0, END)
                pass_entry.delete(0, END)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)



# ---------------------------- READ PASSWORD ------------------------------- #
def get_password():
    website = website_entry.get().capitalize()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
             messagebox.showinfo(f"{website} details",
                    f"Username: {data[website]['user']}\n Password: {data[website]['password']}")
            elif website == "":
                messagebox.showerror("Error", "Please Enter A Website To Search For")
            else:
                messagebox.showerror("Error", "Sorry, You Don't Have Any Passwords Saved For That Website")
    except FileNotFoundError:
        messagebox.showerror("Error", "No File Found. please save a password first!")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager for the Mentally Overworked")
window.config(padx=40, pady=40)
window.minsize(200, 200)

canvas = Canvas(window, width=200, height=200, highlightthickness=0)
LOGO = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=LOGO)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)
user_label = Label(window, text="Email/Username:")
user_label.grid(row=2, column=0)
pass_label = Label(window, text="Password:")
pass_label.grid(row=3, column=0)

# Entries
website_entry = Entry(window, width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
user_entry = Entry(window, width=54)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(END, "jlh3ndr@gmail.com")
pass_entry = Entry(window, width=35)
pass_entry.grid(row=3, column=1)

# Buttons
search_btn = Button(window, text="Search",width=14, command=get_password)
search_btn.grid(row=1, column=2)
pass_btn = Button(window, text="Generate Password", command=generate_random_password)
pass_btn.grid(row=3, column=2, columnspan=2)
add_btn = Button(window, text="Add", width=46, command=save_pass)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()