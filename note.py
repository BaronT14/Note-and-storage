class NOTE:
    def __init__(self):
        self.info = {
            'Tieu de' : '',
            'Noi dung' : ''
        }

    def nhapNote(self):
        self.info['Tieu de'] = input('Tieu de: ')
        self.info['Noi dung'] = input('Noi dung: ')

    def xuat(self):
        print(f"Tieu de: {self.info['Tieu de']}\nNoi dung: {self.info['Noi dung']}")

    