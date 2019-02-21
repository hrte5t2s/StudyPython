import requests
from bs4 import BeautifulSoup


filename = "I://ip.txt"
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
            proxy = {
                'http': http
                
            }
            res_test = requests.get(
                url="http://www.cipuc.edu.cn",
                headers=headers,
                proxies=proxy,
                timeout=3
                )
            ips.append(http)
            with open(filename, "a+") as f:
                con = http + ',' + str(res.elapsed.total_seconds())
                f.write(str(http)+'\n')
                print(con)
        except BaseException as e:
            print(e)
    
