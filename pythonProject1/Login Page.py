from tkinter import *
import sqlite3


root = Tk()
root.title("Database Login")
root.geometry("600x400")
root.configure(bg="black")

user_label = Label(root, text="Username:", bg="black", fg="white")
user_label.pack()
user_entry = Entry(root)
user_entry.pack()


pass_label = Label(root, text="Password:", bg="black", fg="white")
pass_label.pack()
pass_entry = Entry(root, show="*")
pass_entry.pack()


def check_login():

    conn = sqlite3.connect("example.db")
    c = conn.cursor()


    c.execute("SELECT * FROM users WHERE username=? AND password=?", (user_entry.get(), pass_entry.get()))
    result = c.fetchone()


    if result:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    # Close the database connection
    conn.close()


login_button = Button(root, text="Login", command=check_login)
login_button.pack()


root.mainloop()
