from bs4 import BeautifulSoup
import requests

url1 = "https://top.chinaz.com/all/index_br6_"
for i in range(2, 78):
    url2 = "https://top.chinaz.com/all/index_br6_"+str(i)+".html"
    print(url2)
    res = requests.get(url=url2)
    soup = BeautifulSoup(res.text, 'html.parser')
    div = soup.find(name='div', attrs={"class": "TopListCent-listWrap"})
    h3_list = div.find_all(name='h3')
    for h3 in h3_list:
        span = h3.find('span')
        print(span.get_text())
        

    