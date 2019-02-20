import requests
from bs4 import BeautifulSoup
import csv

a=0
filename = "I://ip.csv"
url = "https://www.xicidaili.com/wt/"
urls = []
ips = []
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
for i in range(1, 10):
    url1 = url+str(i)
    urls.append(url1)
for i in urls:
    res = requests.get(url=i, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    table = soup.find("table", attrs={"id": "ip_list"})

    odd = table.find_all("tr", attrs={"class": "odd"})
    for i in odd:
        ip = i.find_all("td")[1].get_text()
        port = i.find_all("td")[2].get_text()
        
        http = ip+":"+port
        try:
            proxy={
                'http': http
                
            }
            res_test = requests.get(
                url="http://www.cipuc.edu.cn",
                headers=headers,
                proxies=proxy,
                timeout=3
                )
            ips.append(http)
            with open(filename, "w+") as f:
                con = http +','+ res.elapsed.total_seconds()
                f.write(con)
        except BaseException as e:
            a=a+1
            print(a)
    print(i)
