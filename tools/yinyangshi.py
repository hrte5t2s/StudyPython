import requests
from bs4 import BeautifulSoup
import time


filename='/home/zhens/Desktop/yys.csv'
url = 'https://www.jiaoyimao.com/g4307/n'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

with open(filename, "w+") as f:
    for i in range(1,5001):
        target_url = url+str(i)+'.html'
        res = requests.get(url=target_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        soup_ul = soup.find('ul',attrs={"class":"list-con specialList"})
        soup_ul_li = soup_ul.find_all('li',attrs={"name":"goodsItem"})
        for li in soup_ul_li:
            name = li.find('a').get_text().replace("\n", "").strip()
            money = li.find('span',attrs={"class":"price"}).get_text().replace("\n", "").strip()
            number = li.find('span',attrs={"class":"count"}).get_text().replace("\n", "").strip()
            href = str(li.a['href'])
            print(name+'  '+money+'  '+number+'  '+href)
            f.write(str(name))
            f.write(",")
            f.write(str(money))
            f.write(",")
            f.write(str(number))
            f.write(",")
            f.write(str(href))
            f.write('\n')
        time.sleep(1)