import note
import json

class DSNOTE: 
    def __init__(self):
        self.list = []

    def taoNote(self, tieude, noidung):
        new_note = note.NOTE(tieude, noidung)
        self.xuLyTrung(new_note.info)
        self.ghiFile()

    def suaNote(self, tieude, noidung):
        for i in self.list: 
            if i['Tieu de'] == tieude:
                i['Noi dung'] = noidung
                break

    def xoaNote(self, tieude):
        for i in self.list:
            if i['Tieu de'] == tieude:
                self.list.remove(i)

    def inDS(self):
        for x in self.list:
            print(x)

    def docFile(self):
        try:
            with open('./data_json/note.json', 'r') as f:
                temp = json.load(f)
                for i in temp:
                    self.list.append(i)
        except FileNotFoundError:
            print('File khong ton tai')
        except ValueError as ve:
            print(f'Loi: {ve}')
        except Exception as e:
            print(f'Loi khong xac dinh: {e}')

    def ghiFile(self):
        try:
            with open('./data_json/note.json','w') as f:
                json.dump(self.list,f)
        except FileNotFoundError:
            print('File khong ton tai')
        except ValueError as ve:
            print(f'Loi: {ve}')
        except Exception as e:
            print(f'Loi khong xac dinh: {e}')

    def timNoteTheoTieuDe(self, tieude):
        for note in self.list:
            if note['Tieu de'] == tieude:
                return note
        return None
    
    def xuLyTrung(self, note):
        tmp = note['Tieu de']
        for i in self.list:
            if i['Tieu de'] == note['Tieu de']:
                count = 1
                note['Tieu de'] = f"{tmp}_{count}"
                for j in self.list:
                    if j['Tieu de'] == note["Tieu de"]:
                        count += 1
                        note['Tieu de'] = f"{tmp}_{count}"
        self.list.append(note)