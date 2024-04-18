import note
import json

class DSNOTE(note.NOTE): 
    def __init__(self):
        self.list = []

    def taoNote(self):
        self.list.append(self.nhapNote())

    def inDS(self):
        for x in self.list:
            self.xuat()
