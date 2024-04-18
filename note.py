class NOTE:
    def __init__(self, tieude, noidung):
        self.tieude = ''
        self.noidung = ''

    def nhapNote(self):
        self.tieude = input('Tieu de: ')
        self.noidung = input('Noi dung: ')

    def xuat(self):
        print(f"Tieu de: {self.tieude}\nNoi dung: {self.noidung}")

    