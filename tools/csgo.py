import requests
from bs4 import BeautifulSoup


filename='/home/zhens/Desktop/csgo.csv'
url1 = 'https://www.c5game.com'
url = 'https://www.c5game.com/csgo/default/result.html?locale=zh&page='
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

with open(filename, "w+") as f:
    for i in range(1,101):
        target_url = url+str(i)
        res = requests.get(url=target_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        soup_ul = soup.find('ul',attrs={"class":"list-item4 clearfix"})
        soup_ul_li = soup_ul.find_all('li', attrs={"class":"selling"})
        for li in soup_ul_li:
            name = li.find('span',attrs={'class':'text-unique'}).get_text().replace("\n", "").strip()
            money = li.find('span',attrs={'class':'price'}).get_text().replace("\n", "").strip()
            number = li.find('span',attrs={'class':'num'}).get_text().replace("\n", "").strip()
            href = url1+str(li.a['href'])
            f.write(str(name))
            f.write(",")
            f.write(str(money))
            f.write(",")
            f.write(str(number))
            f.write(",")
            f.write(str(href))
            f.write('\n')
        