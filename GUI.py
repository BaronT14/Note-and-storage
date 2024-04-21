import DSnote as ds
import note as n
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from ttkbootstrap.constants import *

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NOTE AND STORAGE")
        self.style = Style("minty")
        self.listNote = ds.DSNOTE()

        self.tieude_entry = tk.Entry(root, width=50, font=('Times New Roman', 18, 'italic'))
        self.tieude_entry.grid(row=0, column=2, padx=5, pady=5)
        self.tieude_label = tk.Label(root, text="Tiêu đề:")
        self.tieude_label.grid(row=0, column=1, padx=50, pady=50)

        self.noidung_entry = tk.Entry(root, width=75, font=('Times New Roman', 12))
        self.noidung_entry.grid(row=1, column=2, padx=5, pady=5)
        self.noidung_label = tk.Label(root, text="Nội dung:")
        self.noidung_label.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Thêm ghi chú", command=self.themNote)
        self.add_button.grid(row=5, column=0, columnspan=2, sticky=W ,padx=5, pady=5)

        self.note_listbox = tk.Listbox(root)
        self.note_listbox.grid(row=5, column=2, rowspan=5, sticky=W,padx=50, pady=(50, 50))

    def themNote(self):
        tieude = self.tieude_entry.get()
        noidung = self.noidung_entry.get()
        self.listNote.taoNote(tieude, noidung)
        self.update_listbox()

    def update_listbox(self):
        self.note_listbox.delete(0, tk.END)
        for note in self.listNote.list:
            note_str = f"{note['Tieu de']}"
            self.note_listbox.insert(tk.END, note_str)

    
def main():
    root = tk.Tk()
    root.geometry('1080x600')
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()