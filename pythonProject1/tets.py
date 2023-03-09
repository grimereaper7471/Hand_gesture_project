import tkinter as tk

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hand Gesture GUI")

        self.label = tk.Label(master, text="Login!")
        self.label.pack()

        self.quit_button = tk.Button(master, text="Stop", command=master.quit, )
        self.quit_button.pack()
        root.configure(bg="black")


class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hand Gesture GUI")

        self.label = tk.Label(master, text="Welcome to hand gesture recognition!", bg="black", fg="white")
        self.label.pack()

        self.my_button = tk.Button(master, text="Start", command=self.open_my_gui, bg="black", fg="white")
        self.my_button.pack()
        root.configure(bg="black")


    def open_my_gui(self):
        my_gui_window = tk.Toplevel(self.master)
        my_gui = MyGUI(my_gui_window)

root = tk.Tk()
main_gui = MainGUI(root)
root.mainloop()

