from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json
from selenium.webdriver.common.keys import Keys

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
        for div in soup.select('div.type02_m035 ul li.item'):
            # print(div.text)
            # count += 1
            # if count > 9:
            #     break
            # else:
            datum.append(div.text.split('\n'))
                #print(div.text)
                #count += 1

        '''發生error-('Connection aborted.', OSError("(10054, 'WSAECONNRESET')"))'''

        for div2 in soup.select('div.type02_bd-a h4 a'):
            matrix.append(div2.get('href'))
            print('title',div2.text)
            print('href',div2['href'])
        #print(matrix)
        headers = {
            "Host": "www.books.com.tw",
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
        for a in matrix:
            #print(a)
            r = requests.get(a,headers = headers)
            #print(r.request.headers)
            #print(r.text)
            for b in soup.select('div.cnt_prod002.clearfix ul.price'):
                print('分類',b.text)

            ###error - ('Connection aborted.', OSError("(10054, 'WSAECONNRESET')"))

        ####json格式輸出
        for data in datum:
            while '' in data:
                data.remove('')

            dict = {}
            dict['key'] = {"'" + data[0] +"'": data}
            json1 = json.dumps(dict['key'], ensure_ascii=False).encode('utf8')
            print(json1.decode())

    except Exception as e:
        print(e)


if __name__ == '__main__':
    chrome()