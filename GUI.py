import DSnote as ds
import CRAWL
import note as n
from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import messagebox as mb
import json

class NOTE_GUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1080x700+150+50')
        self.listNote = ds.DSNOTE()
        self.listNote.docFile()

        self.frame_top = ttk.Frame(self.root, bootstyle='dark')
        self.frame_top.pack(side='top', fill='x')
        self.tieude_label = ttk.Label(self.frame_top, text="NOTE", font=("Helvetica",20, "bold"))
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
        self.update_listbox()


        self.frame_right = ttk.Frame(self.root)
        self.frame_right.pack(fill='x')

        self.frame_right_tieude = ttk.Frame(self.frame_right)
        self.frame_right_tieude.pack(fill='x')

        self.tieude_text = ttk.Text(self.frame_right_tieude, height=1, font=('Helvetica', 18, 'italic'))
        self.tieude_text.pack(side='left',padx=50, pady=(30,0))

        self.frame_right_noidung = ttk.Frame(self.frame_right)
        self.frame_right_noidung.pack(fill='x')

        self.noidung_text = ttk.Text(self.frame_right_noidung, width=100, height=20, font=('Helvetica', 12))
        self.noidung_text.pack(side='left', padx=50, pady=(0, 30))

        self.Add_button = ttk.Button(self.frame_right, text="Thêm ghi chú", command=self.them_Note)
        self.Add_button.pack(side='right', padx=(0, 50), pady=(0, 30))

        self.note_listbox.bind("<<TreeviewSelect>>", self.chon_note)

        self.Update_button = ttk.Button(self.frame_right, text="Cập nhật ghi chú", command=self.capNhat_Note)
        self.Update_button.pack(side='right', padx=(0, 20), pady=(0, 30))

        self.Delete_button = ttk.Button(self.frame_right, text="Xoá ghi chú", command=self.xoa_Note)
        self.Delete_button.pack(side='right', padx=(0, 20), pady=(0, 30))

    def chon_note(self, event):
        selected_item = self.note_listbox.selection()
        if selected_item:
            selected_title = self.note_listbox.item(selected_item)['values'][0]
            selected_note = self.listNote.timNoteTheoTieuDe(selected_title)
            if selected_note:
                self.tieude_text.delete("1.0", "end")
                self.tieude_text.insert("1.0", selected_title)
                self.noidung_text.delete("1.0", "end")
                self.noidung_text.insert("1.0", selected_note['Noi dung'])

    def xoaEntry(self):
        self.tieude_text.delete("1.0", "end-1c")
        self.noidung_text.delete("1.0", "end-1c")

    def them_Note(self):
        tieude = self.tieude_text.get("1.0", "end-1c")
        noidung = self.noidung_text.get("1.0", "end-1c")
        self.listNote.taoNote(tieude, noidung)
        self.update_listbox()
        self.listNote.ghiFile()

    def capNhat_Note(self):
        tieude = self.tieude_text.get("1.0", "end-1c")
        noidung = self.noidung_text.get("1.0", "end-1c")
        self.listNote.suaNote(tieude, noidung)
        self.listNote.ghiFile()

    def xoa_Note(self):
        tieude = self.tieude_text.get("1.0", "end-1c")
        self.listNote.xoaNote(tieude)
        self.update_listbox()
        self.listNote.ghiFile()
        

    def update_listbox(self):
        for row in self.note_listbox.get_children():
            self.note_listbox.delete(row)
        for note in reversed(self.listNote.list):
            self.note_listbox.insert("", "end", values=(note['Tieu de'],))


class JOBS_GUI(CRAWL.CRAWL):
    def __init__(self, root, quyen, url):
        self.root = root
        self.root.geometry('1080x700+150+50')
        self.dsc = CRAWL.CRAWL(url)
        self.quyen = quyen
        self.dsc.docFile()

        self.frame_top = ttk.Frame(self.root, bootstyle='dark')
        self.frame_top.pack(side='top', fill='x')
        self.label1 = ttk.Label(self.frame_top, text="JOBS", font=("Helvetica",20, "bold"))
        self.label1.pack(pady=10, padx=(10,0) , side='left')
        self.newCrawl_button = ttk.Button(self.frame_top, text="Cào dữ liệu mới", command=self.crawl_data)
        self.newCrawl_button.pack(side='right', padx=(0, 30))
        if self.quyen == 'admin':
            self.xoads = ttk.Button(self.frame_top, text="Xoá danh sách công việc", command=self.xoa_ds)
            self.xoads.pack(side='right', padx=(0, 30))
            # self.xoads.config(state="disabled")
        self.find_theo_langs = ttk.Button(self.frame_top, text="Tìm kiếm việc theo yêu cầu", command=self.pop_up_o_tim_kiem)
        self.find_theo_langs.pack(side='right', padx=(0, 30))

        self.frame_left = ttk.Frame(self.root)
        self.frame_left.pack(side='left', fill='y')
        self.scrollbar = ttk.Scrollbar(self.frame_left)
        self.job_listbox = ttk.Treeview(self.frame_left, columns=("Title"), show="headings", yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.configure(command=self.job_listbox.yview)
        self.job_listbox.pack(side="left", fill="both", expand=True)
        self.job_listbox.heading("Title", text="Danh sách công việc")
        self.update_listbox(self.dsc.ds_crawl)
        self.job_listbox.bind("<<TreeviewSelect>>", self.chon_job)

        self.frame_right = ttk.Frame(self.root)
        self.frame_right.pack(fill='x')
    
    def pop_up_o_tim_kiem(self):
        self.find_theo_langs.destroy()
        self.find_theo_langs = ttk.Button(self.frame_top, text="Tìm kiếm", command=self.find_nn)
        self.find_theo_langs.pack(side='right', padx=(0, 30))
        self.find = ttk.Entry(self.frame_top, width = 40)
        self.find.pack(side='right', padx=(0, 30))

        
    def find_nn(self):
        x = self.find.get().lower()
        self.find.destroy()
        self.find_theo_langs.destroy()
        self.find_theo_langs = ttk.Button(self.frame_top, text="Huỷ tìm kiếm", command=self.huy_find)
        self.find_theo_langs.pack(side='right', padx=(0, 30))
        l = self.dsc.find_langs(x)
        self.update_listbox(l)

    def huy_find(self):
        self.find_theo_langs.destroy()
        self.update_listbox(self.dsc.ds_crawl)
        self.find_theo_langs = ttk.Button(self.frame_top, text="Tìm kiếm việc theo yêu cầu", command=self.pop_up_o_tim_kiem)
        self.find_theo_langs.pack(side='right', padx=(0, 30))

    def chon_job(self, event):
        self.frame_right.destroy()
        selected_item = self.job_listbox.selection()
        if selected_item:
            selected_title = self.job_listbox.item(selected_item)['values'][0]
            job = self.dsc.timJobTheoTieuDe(selected_title)
            if job:
                self.frame_right = ttk.Frame(self.root)
                self.frame_right.pack(fill='x')

                title = ttk.Label(self.frame_right, text=job['title'], font=('Times New Roman', 25), wraplength=800)
                title.grid(padx=20, pady=20, row=0, column=0, sticky='w')
                company = ttk.Label(self.frame_right, text='Tên công ty: ' + job['company'], font=('Times New Roman', 15))
                company.grid(padx=20, pady=10, row=1, column=0, sticky='w')
                pois = ttk.Label(self.frame_right, text='Vị trí: ' + job['pois'], font=('Times New Roman', 13))
                pois.grid(padx=20, pady=10, row=3, sticky='w')
                addr = ttk.Label(self.frame_right, text='Địa chỉ: ' + job['addr'], font=('Times New Roman',13))
                addr.grid(padx=20, pady=10,row=4, sticky='w')
                benefits_label = ttk.Label(self.frame_right, text='* Lợi ích công ty', font=('Times New Roman',13))
                benefits_label.grid(padx=20, pady=10,row=5, sticky='w')
                row=6
                for i in job['benefits']:
                    benefits = ttk.Label(self.frame_right, text='-- ' + i, font=('Times New Roman',13), wraplength=750)
                    benefits.grid(padx=20, pady=10,row=row, sticky='w')
                    row+=1
                langs_label = ttk.Label(self.frame_right, text='* Yêu cầu', font=('Times New Roman',13))
                langs_label.grid(padx=20, pady=10,row=row, sticky='w')
                row+=1
                l = ' : '.join(job['langs'])
                langs = ttk.Label(self.frame_right, text='+ ' + l, font=('Times New Roman',13))
                langs.grid(padx=20, pady=10,row=row, sticky='w')
                row+=1
                btn = ttk.Button(self.frame_right, text='Xoá Job', command=self.xoa_job)
                btn.grid(row=row, sticky='sw', padx=20, pady=20)
                if self.quyen == 'user':
                    btn.config(state="disabled")

    def them_note(self):
        selected_item = self.job_listbox.selection()
        if selected_item:
            selected_title = self.job_listbox.item(selected_item)['values'][0]
            job = self.dsc.timJobTheoTieuDe(selected_title)
            

    def xoa_job(self):
        selected_item = self.job_listbox.selection()
        if selected_item:
            selected_title = self.job_listbox.item(selected_item)['values'][0]
            job = self.dsc.timJobTheoTieuDe(selected_title)
            self.dsc.ds_crawl.remove(job)
            self.dsc.ghiFile()
            self.update_listbox(self.dsc.ds_crawl)

    def crawl_data(self):
        self.dsc.crawl_data()
        self.update_listbox(self.dsc.ds_crawl)

    def xoa_ds(self):
        self.dsc.xoa_ds()
        self.update_listbox(self.dsc.ds_crawl)

    def update_listbox(self, list_data):
        for row in self.job_listbox.get_children():
            self.job_listbox.delete(row)
        for job in reversed(list_data):
            self.job_listbox.insert("", "end", values=(job['title'],))


class USER:
    def __init__(self):
        self.quyen = 'user'
        self.dsuser = []
        self.dsadmin = []
        self.dangnhap = 0
        self.root = tk.Tk()
        self.root.title('Login')
        self.root.geometry('400x500+500+50')
        self.docFile('./data_json/dsadmin.json')
        self.docFile('./data_json/dsuser.json')

        self.chon_user_admin()

        self.root.mainloop()

    def chon_user_admin(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        chon_label = tk.Label(self.frame, text = "Bạn là ADMIN hay USER", font=('Helvetica', 12))
        chon_label.pack(pady = 20, padx=30)

        user_login = tk.Button(self.frame, text = 'User', font=('Helvetica', 12), width=36, command=self.entry_login_user)
        user_login.pack(pady=20)
        admin_login = tk.Button(self.frame, text = 'Admin', font=('Helvetica', 12), width=36, command=self.entry_login_admin)
        admin_login.pack(pady=20)

    def entry_login_admin(self):
        self.frame.destroy()
        self.quyen = 'admin'
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        username_label = tk.Label(self.frame, text = "username", font=('Helvetica', 12))
        username_label.pack(pady = (20,1), anchor='w')
        self.username_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 14))
        self.username_entry.pack()
        password_label = tk.Label(self.frame, text = "password", font=('Helvetica', 12))
        password_label.pack(pady = (20,1), anchor='w')
        self.password_entry = tk.Entry(self.frame, width=30, show = '*', font=('Helvetica', 14))
        self.password_entry.pack()
        login_button = tk.Button(self.frame, text = 'Đăng nhập', font=('Helvetica', 12), width=36, command=self.login)
        login_button.pack(pady=20)
        back = tk.Button(self.frame, text = 'Back', font=('Helvetica', 12), command=self.back_chon)
        back.pack(anchor='w', pady=20)


    def entry_login_user(self):
        self.frame.destroy()
        self.quyen = 'user'
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        username_label = tk.Label(self.frame, text = "username", font=('Helvetica', 12))
        username_label.pack(pady = (20,1), anchor='w')
        self.username_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 14))
        self.username_entry.pack()

        password_label = tk.Label(self.frame, text = "password", font=('Helvetica', 12))
        password_label.pack(pady = (20,1), anchor='w')
        self.password_entry = tk.Entry(self.frame, width=30, show = '*', font=('Helvetica', 14))
        self.password_entry.pack()

        login_button = tk.Button(self.frame, text = 'Đăng nhập', font=('Helvetica', 12), width=36, command=self.login)
        login_button.pack(pady=20)
        logup_button = tk.Button(self.frame, text = 'Đăng ký', font=('Helvetica', 12), width=36, command=self.logup)
        logup_button.pack()

        back = tk.Button(self.frame, text = 'Back', font=('Helvetica', 12), command=self.back_chon)
        back.pack(anchor='w', pady=20)

    def back_chon(self):
        self.frame.destroy()
        self.chon_user_admin()

    def login(self):
        name = self.username_entry.get()
        password = self.password_entry.get()
        if self.quyen == 'admin':
            for i in self.dsadmin:
                if i['name'] == name and i['password'] == password:
                    mb.showinfo('Thông báo', 'Đăng nhập thành công')
                    self.dangnhap = 1
                    self.root.destroy()
                    return True
            mb.showerror('Thông báo', 'Đăng nhập thất bại')
        else:
            for i in self.dsuser:
                if i['name'] == name and i['password'] == password:
                    mb.showinfo('Thông báo', 'Đăng nhập thành công')
                    self.dangnhap = 1
                    self.root.destroy()
                    return True
            mb.showerror('Thông báo', 'Đăng nhập thất bại')
        return False

    def logup(self):
        info = {}
        info['name'] = self.username_entry.get()
        info['password'] = self.password_entry.get()
        if len(info['name']) == 0 or len(info['password']) == 0:
            mb.showerror('Đăng kí thất bại', 'Chưa nhập đủ thông tin')
        else:
            self.dsuser.append(info)
            self.ghiFile()
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            mb.showinfo('Thông báo', 'Đăng ký thành công')


    def docFile(self, filename):
        try:
            with open(filename, 'r') as f:
                temp = json.load(f)
                if filename == './data_json/dsadmin.json':
                    for i in temp:
                        self.dsadmin.append(i)
                else:
                    for i in temp:
                        self.dsuser.append(i)
        except FileNotFoundError:
            print('File khong ton tai')
        except ValueError as ve:
            print(f'Loi: {ve}')
        except Exception as e:
            print(f'Loi khong xac dinh: {e}')

    def ghiFile(self):
        try:    
            with open('./data_json/dsuser.json','w') as f:
                json.dump(self.dsuser,f)
        except FileNotFoundError:
            print('File khong ton tai')
        except ValueError as ve:
            print(f'Loi: {ve}')
        except Exception as e:
            print(f'Loi khong xac dinh: {e}')

class main:
    def __init__(self):
        self.h = USER()
        self.quyen = self.h.quyen
        if self.h.dangnhap == 1:
            self.root = Tk()
            self.root.geometry('500x200+500+50')
            self.root.title("NOTE AND JOBS")
            self.style = Style("minty")
            self.frame_main = tk.Frame(self.root)
            self.frame_main.pack()
            self.chon_app()
            self.root.mainloop()

    def chon_app(self):
        btn_note_app = tk.Button(self.frame_main, text='Ứng dụng note', font=('Helvetica', 25), width=36, command=self.appNote)
        btn_note_app.pack(padx=20, pady=10)
        btn_jobs_app = tk.Button(self.frame_main, text='Ứng dụng jobs', font=('Helvetica', 25), width=36,command=self.appJobs)
        btn_jobs_app.pack(padx=20, pady=10)

    def appNote(self):
        self.frame_main.destroy()
        app = NOTE_GUI(self.root)

    def appJobs(self):
        self.frame_main.destroy()
        app = JOBS_GUI(self.root, self.quyen, 'https://topdev.vn/viec-lam-it/ho-chi-minh-kl79?src=topdev.vn&medium=mainmenu')
            


m = main()
    
    