from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    #----------- Used to copy password without Ctrl+C after generating ------------ #
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def adding():
    website = web_entry.get()
    user_name = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website:{
            "email":user_name,
            "password":password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any fields empty!")
    else:
        try:
            with open("data.json", "r") as datas:
                #reading old data
                data=json.load(datas)
        except FileNotFoundError:
            with open("data.json", "r") as datas:
                json.dump(new_data,datas,indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as datas:
                #saving updated data
                json.dump(data,datas,indent=4 )
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

def get_info():
    website = web_entry.get()
    try:
        with open("data.json","r") as datas:
            data=json.load(datas)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            user_name = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{user_name}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No Details for {website} found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(130,100,image = pass_img)
canvas.grid(column=1,row=0)

web_label = Label(text="Website:")
web_label.grid(column = 0,row =1)

user_label =Label(text = "Email/Username:")
user_label.grid(column = 0,row =2)

pass_label =Label(text = "Password:")
pass_label.grid(column = 0,row =3)

web_entry = Entry(width=34)
web_entry.grid(column = 1,row = 1)
web_entry.focus()

user_entry = Entry(width=52)
user_entry.grid(column = 1,row = 2 ,columnspan =2)
user_entry.insert(0,"pycharm@gmail.com")

pass_entry = Entry(width = 34)
pass_entry.grid(row = 3 ,column = 1,columnspan =1)

generate_button = Button(text="Generate Password",bg="white",command=generate_password)
generate_button.grid(column=2,row = 3)

add_button = Button(text="Add",width=44,bg="white",command=adding)
add_button.grid(column = 1,row = 4,columnspan =2)

search_button = Button(text="Search",width=15,bg="white",command=get_info)
search_button.grid(column=2,row=1)

window.mainloop()