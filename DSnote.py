import note
import json

class DSNOTE: 
    def __init__(self):
        self.list = []

    def taoNote(self, tieude, noidung):
        new_note = note.NOTE(tieude, noidung)
        self.list.append(new_note.info)

    # def suaNote(self):


    def inDS(self):
        for x in self.list:
            print(x)

    def docFile(self):
        with open('note.json', 'r') as f:
            self.list = json.load(f)

    def ghiFile(self):
        with open('note.json','w') as f:
            json.dump(self.list,f)