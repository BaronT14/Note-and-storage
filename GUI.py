import DSnote as ds
import note as n
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap import Style
from PIL import ImageTk,Image
class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NOTE AND STORAGE")
        self.style = Style("minty")
        self.listNote = ds.DSNOTE()

        self.frame_top = ttk.Frame(self.root, bootstyle='dark')
        self.frame_top.pack(side='top', fill='x')
        self.tieude_label = ttk.Label(self.frame_top, text="NOTE AND STORAGE", font=("Helvetica",20, "bold"))
        self.tieude_label.pack(pady=10, padx=(10,0) , side='left')
        self.add_button = ttk.Button(self.frame_top, text="Thêm ghi chú", command=self.themNote)
        self.add_button.pack(side='right', padx=(0, 30))
        #background 
        # self.bg=Image.open("hello.png")

        # self.resized=self.bg.resize((800,500), Image.LANCZOS)

        # self.new_pic = ImageTk.PhotoImage(self.resized)
        # # my_bg = Label(root, image=bg)
        # # my_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # self.my_canvas=Canvas(root)
        # self.my_canvas.pack(fill="both",expand=True)
        # self.my_canvas.create_image(0,0,image=self.new_pic)



        self.frame_left = ttk.Frame(self.root,bootstyle='secondary')
        self.frame_left.pack(side='left', fill='y')
        self.scrollbar = ttk.Scrollbar(self.frame_left)
        self.note_listbox = ttk.Treeview(self.frame_left, columns=("Title"), show="headings", yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.configure(command=self.note_listbox.yview)
        self.note_listbox.pack(side="left", fill="both", expand=True)
        self.note_listbox.heading("Title", text="Tiêu đề")


        self.frame_right = ttk.Frame(self.root)
        self.frame_right.pack(fill='x')

        self.frame_right_tieude = ttk.Frame(self.frame_right,bootstyle='info')
        self.frame_right_tieude.pack(fill='x')
        #self.tieude_label = ttk.Label(self.frame_right_tieude, text="Tiêu đề:")
        #self.tieude_label.pack(side='left', padx=20, pady=30)
        self.tieude_entry = ttk.Entry(self.frame_right_tieude, font=('Helvetica', 18, 'italic'))
        self.tieude_entry.pack(side='left',padx=(20,0), pady=(30,0))

        self.frame_right_noidung = ttk.Frame(self.frame_right,bootstyle='info')
        self.frame_right_noidung.pack(fill='x')
        # self.noidung_label = ttk.Label(self.frame_right_noidung, text="Nội dung:")
        # self.noidung_label.pack(side='left', padx=20, pady=30)
        self.noidung_entry = ttk.Entry(self.frame_right_noidung, font=('Helvetica', 12))
        self.noidung_entry.pack(side='left', padx=(10,0))

    def themNote(self):
        tieude = self.tieude_entry.get()
        noidung = self.noidung_entry.get()
        self.listNote.taoNote(tieude, noidung)
        self.update_listbox()

    def update_listbox(self):
        for row in self.note_listbox.get_children():
            self.note_listbox.delete(row)
        for note in self.listNote.list:
            self.note_listbox.insert("", "end", values=(note['Tieu de'],))

    
def main():
    root = Tk()
    root.geometry('1080x600')
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()