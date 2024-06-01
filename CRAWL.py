import requests
from bs4  import BeautifulSoup
import json
from tkinter import messagebox as mb

class CRAWL:
    def __init__(self, url):
        self.url = url
        self.ds_crawl = []

    def find_langs(self, lang):
        temp_ds = []
        for job in self.ds_crawl:
            for l in job['langs']:
                if lang == l.lower():
                    temp_ds.append(job)
                    break
        return temp_ds

    def xoa_ds(self):
        self.ds_crawl.clear()
        self.ghiFile()

    def crawl_data(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            s = BeautifulSoup(r.content, 'html.parser')
            jobs = s.findAll('li', class_='mb-4 last:mb-0')

            for job in jobs:
                temp = {}
                p = job.find('a', class_='text-lg font-bold transition-all text-primary')
                if p is None:
                    continue
                temp['title'] = p.text
                temp['company'] = job.find('a', class_='text-gray-600 transition-all hover:text-primary').text
                temp['pois'] = job.find('p', class_='text-gray-500').text
                p = job.findAll('span', class_='whitespace-nowrap rounded border border-solid font-normal transition-all inline-flex items-center justify-center border-blue-light text-blue-dark bg-blue-light hover:border-blue-dark h-[1.625rem] px-2 text-xs md:h-7 md:px-2 md:text-sm')
                l = []
                for t in p:
                    l.append(t.text)
                temp['langs'] = l
                l1 = []
                p = job.findAll('div', class_='flex flex-wrap items-end gap-2 text-gray-500')
                temp['addr'] = p[0].text
                p = job.findAll('ul', class_='ml-6 list-disc text-gray-600')
                for i in p:
                    t = i.findAll('p', class_='line-clamp-1')
                    for z in t:
                        l1.append(z.text)
                temp['benefits'] = l1
                self.ds_crawl.append(temp)
            mb.showinfo('Thành công', 'Bạn đã cào được dữ liệu mới')
            self.ghiFile()
        else:
            print("Khong the ket noi duoc")
            mb.showinfo('Thất bại', 'Cào được dữ liệu mới thất bại')

    def timJobTheoTieuDe(self, ten):
        for job in self.ds_crawl:
            if job['title'] == ten:
                return job

    def docFile(self):
        try:
            with open('./data_json/dsjob.json', 'r') as f:
                temp = json.load(f)
                for i in temp:
                    self.ds_crawl.append(i)
        except FileNotFoundError:
            print('File khong ton tai')
        except ValueError as ve:
            print(f'Loi: {ve}')
        except Exception as e:
            print(f'Loi khong xac dinh: {e}')

    def ghiFile(self):
        try:
            with open('./data_json/dsjob.json','w') as f:
                json.dump(self.ds_crawl,f)
        except FileNotFoundError:
            print('File khong ton tai')
        except ValueError as ve:
            print(f'Loi: {ve}')
        except Exception as e:
            print(f'Loi khong xac dinh: {e}')