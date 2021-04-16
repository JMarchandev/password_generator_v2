import tkinter as tk

from model.password import Password
from model.window import Window

if __name__ == "__main__":
    root = tk.Tk()
    password = Password()
    app = Window(root, password)
    root.mainloop()
