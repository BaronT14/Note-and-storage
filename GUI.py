import DSnote as ds
import note as n
from tkinter import *
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap import Style

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
        self.newNote_button = ttk.Button(self.frame_top, text="Tạo ghi chú mới", command=self.xoaEntry)
        self.newNote_button.pack(side='right', padx=(0, 30))




        self.frame_left = ttk.Frame(self.root)
        self.frame_left.pack(side='left', fill='y')
        self.scrollbar = ttk.Scrollbar(self.frame_left)
        self.note_listbox = ttk.Treeview(self.frame_left, columns=("Title"), show="headings", yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.configure(command=self.note_listbox.yview)
        self.note_listbox.pack(side="left", fill="both", expand=True)
        self.note_listbox.heading("Title", text="Danh sách ghi chú")


        self.frame_right = ttk.Frame(self.root)
        self.frame_right.pack(fill='x')

        self.frame_right_tieude = ttk.Frame(self.frame_right)
        self.frame_right_tieude.pack(fill='x')
        # self.tieude_label = ttk.Label(self.frame_right_tieude, text="Tiêu đề:")
        # self.tieude_label.pack(side='left', padx=20, pady=30)
        self.tieude_text = ttk.Text(self.frame_right_tieude, height=1, font=('Helvetica', 18, 'italic'))
        self.tieude_text.pack(side='left',padx=50, pady=(30,0))

        self.frame_right_noidung = ttk.Frame(self.frame_right)
        self.frame_right_noidung.pack(fill='x')
        # self.noidung_label = ttk.Label(self.frame_right_noidung, text="Nội dung:")
        # self.noidung_label.pack(side='left', padx=20, pady=30)
        self.noidung_text = ttk.Text(self.frame_right_noidung, width=100, height=20, font=('Helvetica', 12))
        self.noidung_text.pack(side='left', padx=50, pady=(0, 30))

        self.Add_button = ttk.Button(self.frame_right, text="Thêm ghi chú", command=self.themNote)
        self.Add_button.pack(side='right', padx=(0, 50), pady=(0, 30))
        
        self.delete_Button = ttk.Button(self.frame_right, text="Mở File", command=self.openfile)
        self.delete_Button.pack(side='right', padx=(0, 50), pady=(0, 30))



    def xoaEntry(self):
        self.tieude_text.delete("1.0", "end-1c")
        self.noidung_text.delete("1.0", "end-1c")

    def themNote(self):
        tieude = self.tieude_text.get("1.0", "end-1c")
        noidung = self.noidung_text.get("1.0", "end-1c")
        self.listNote.taoNote(tieude, noidung)
        self.update_listbox()

    def update_listbox(self):
        for row in self.note_listbox.get_children():
            self.note_listbox.delete(row)
        for note in self.listNote.list:
            self.note_listbox.insert("", "end", values=(note['Tieu de'],))
    #Ham mo file - file explorer
    def openfile(self):
        filepath=filedialog.askopenfilename()
        file=open(filepath, 'r')
        print(file.read())
        file.close()

    
def main():
    root = Tk()
    root.geometry('1080x600')
    app = GUI(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()