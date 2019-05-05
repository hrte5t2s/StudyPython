import requests
from bs4 import BeautifulSoup
import time

filename='/home/zhens/Desktop/tlbb.csv'
url = 'http://tl.cyg.changyou.com/goods/selling?world_id=0&have_chosen=&page_num='
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

with open(filename, "w+") as f:
    for i in range(1,933):
        target_url = url+str(i)
        res = requests.get(url=target_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        soup_ul = soup.find('ul',attrs={"class":"pg-goods-list"})
        soup_ul_li = soup_ul.find_all('li')
        for li in soup_ul_li:
            name = li.find('span',attrs={"class":"name"}).get_text().replace("\n", "").strip()
            money = li.find('p',attrs={"class":"price"}).get_text().replace("\n", "").strip()
            href = li.find('a')['href'].replace("\n", "").strip()
            
            print(name+'  '+money+'  '+href)
            f.write(str(name))
            f.write(",")
            f.write(str(money))
            f.write(",")

            f.write(str(href))
            f.write('\n')
        time.sleep(1)
        