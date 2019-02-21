import requests
from bs4 import BeautifulSoup
import time

url = "https://www.kuaidaili.com/free/inha/"
urls = []
filename = "I://ip.txt"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
for i in range(1, 11):
    urls.append(url + str(i))

for url in urls:
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    try:
        trs = soup.tbody.find_all("tr")
        for tr in trs:
            IP = tr.find("td", attrs={"data-title": "IP"}).get_text()
            Port = tr.find("td", attrs={"data-title": "PORT"}).get_text()
            http = IP + ":" + Port
            proxy = {'http': http}
            try:
                requests.get(
                    url="http://www.baidu.com",
                    headers=headers,
                    proxies=proxy,
                    timeout=3
                    )
                with open(filename, "a+") as f:
                    f.write(http)
                    f.write("\n")
            except BaseException as e:
                print(e)
    except BaseException as e:
        print(e)
    time.sleep(1)
