import tkinter as tk
from tkinter import *

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe helper program")
        # self.master.wm_iconbitmap('icon.ico')
        
        # --- This is the code you need --- #
        screen_width = str(self.master.winfo_screenwidth())
        screen_height = str(self.master.winfo_screenheight())
        self.master.geometry(screen_width + "x" + screen_height + "+0+0")

        self.listButton = tk.Button(self.master, text='Show recipe list', command='clicked')
        self.listButton.grid(row=0, column=1, padx=4, pady=4)

        self.enterButton = tk.Button(self.master, text='Add new recipe')
        self.enterButton.grid(row=0, column=2, padx=4, pady=4)
        
        self.enterButton = tk.Button(self.master, text='Clear the list')
        self.enterButton.grid(row=0, column=3, padx=4, pady=4)
        
        self.enterButton = tk.Button(self.master, text='Close this program')
        self.enterButton.grid(row=0, column=4, padx=4, pady=4)

        lbl = Label(self.master, text="This program can help you to choose a recipe or fill your list of recipes!", font=("Arial Bold", 20))  
        lbl.grid(row=1, column=0)
        # ---  --- #
        
def clicked():
    # lbl.configure(text="Вот они")
    lbl = Label(text="HERE IT IS!", font=("Arial Bold", 20))


def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
if __name__ == '__main__':
    main()