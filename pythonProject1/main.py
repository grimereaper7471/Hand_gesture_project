import tkinter as tk


# Create a new Tkinter window
window = tk.Tk()


window.title("Hand Gesture GUI")


window.geometry("500x350")

window.configure(background="black")

label = tk.Label(window, text="Welcome to hand gesture recognition !", fg="white", bg="black", font=("Arial", 20))
label.pack()

my_button = tk.Button(window, text="Start!",font=("Arial", 20), width=10, height=2)
my_button.pack()

window.mainloop()
