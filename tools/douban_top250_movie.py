import requests
from bs4 import BeautifulSoup

urls = []
filename = "I://movie.txt"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
for i in range(0, 226, 25):
    url = "https://movie.douban.com/top250?start="+str(i)+"&filter="
    urls.append(url)

for url in urls:
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    div = soup.find_all("div", attrs={"class": "info"})
    for spans in div:
        name = spans.a.span.get_text()
        quteo = spans.find("span", attrs={"class": "rating_num"}).get_text()
        with open(filename, "a+") as f:
            f.write(name+",")
            f.write(quteo+"\n")