import DSnote as ds
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# class GUI(ds.DSNOTE):



def main():
    root = tk.Tk()
    root.title('Note and storage')
    root.geometry('1080x720')
    n1 = ds.DSNOTE()
    n1.nhapNote()
    root.mainloop()

if __name__ == '__main__':
    main()