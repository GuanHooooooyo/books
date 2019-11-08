from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json

def chrome():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path='D:/test lab/chromedriver.exe')
        #driver.get('https://www.books.com.tw/web/sys_tdrntb/books/')
        r = requests.get('https://www.books.com.tw/web/sys_tdrntb/books/')
        soup = BeautifulSoup(r.text,'lxml')
        #soup = BeautifulSoup(driver.page_source, 'lxml')
        count = 0
        datum = []
        matrix = []
        key = {}
        # for div in soup.select('div.type02_m035 ul li.item'):
        #     # print(div.text)
        #     # count += 1
        #     if count > 9:
        #         break
        #     else:
        #         datum.append(div.text.split('\n'))
        #         # print(div.text)
        #         count += 1
        # datum.remove('')
        '''抓取 top100 資料'''
        for div2 in soup.select('div.type02_bd-a h4 a'):
            matrix.append(div2.get('href'))
            print('title',div2.text)
            print('href',div2['href'])
        print(matrix)
        for a in matrix:
            r = requests.get(a)
            test = soup.select('div.title h3 a')
            for b in test:
                print('分類',b.text)

            #for classfy in soup.select('div.grid_10 li'):
                #print('細項',classfy.text)



        # for data in datum:
        #     while '' in data:
        #         data.remove('')
        # if data =='TOP1':
        # dict = {}
        # dict['key'] = {"'" + data[0] +"'": data}
        # json1 = json.dumps(dict['key'], ensure_ascii=False).encode('utf8')
        # print(json1.decode())
        # print(datum)
        # key = {'fp':234,'a':True,'b':False,'c':None,'d':123}
        # testkey = {'aa':datum}
        # json1 = json.dumps(key)
        # print(json1)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    chrome()