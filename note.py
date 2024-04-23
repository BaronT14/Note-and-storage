class NOTE:
    def __init__(self, tieude, noidung):
        self.info = {
            'Tieu de' : tieude,
            'Noi dung' : noidung
        }

    def xuat(self):
        print(f'Tieu de: {self.info["Tieu de"]}\nNoi dung: {self.info["Noi dung"]}')
