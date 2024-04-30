from tkinter import *
from tkinter import messagebox
import json

# gui
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

def add():
    if len(website_entry.get()) == 0 or len(password_entry.get())== 0:
        messagebox.showinfo(title="", message="Please enter the info")
    else:
        #is_ok = messagebox.askokcancel(title="", message=f"Email: {email_entry.get()} \nPassword: {password_entry.get()} \n Is it good to save?")
        #if is_ok: 
            #f = open("data.txt", "a")
            #f.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()} \n")
            #website_entry.delete(0,END)
            #password_entry.delete(0,END)
        new_data = {
            website_entry.get():
            {
                "email": email_entry.get(),
                "password": password_entry.get()
            }
        }
        with open("data.json", "r") as data_file:
            # reading old data
            data = json.load(data_file)
            # updating old data with new data
            data.update(new_data)

        with open("data.json", "w") as data_file:
            # saving updated
            json.dump(data, data_file, indent=4)
            
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image = img)
canvas.grid(column=1, row=0)

label_1 = Label(text="Website")
label_1.grid(column=0, row=1)

label_2 = Label(text="Email/Username")
label_2.grid(column=0, row=2)

label_3 = Label(text="Password")
label_3.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2)
email_entry.insert(END, "@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", highlightthickness=0)
generate_button.grid(column=3, row=3)

add_button = Button(text="Add", highlightthickness=0, width=30, command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

