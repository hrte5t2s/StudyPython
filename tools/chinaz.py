from bs4 import BeautifulSoup
import requests

filename = "I:/url.txt"
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
url1 = "https://top.chinaz.com/all/index_br6_"
with open(filename, "w+") as f:
    for i in range(2, 78):
        url2 = "https://top.chinaz.com/all/index_br6_"+str(i)+".html"
    
        res = requests.get(url=url2, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        div = soup.find(name='div', attrs={"class": "TopListCent-listWrap"})
        h3_list = div.find_all(name='h3')
        for h3 in h3_list:
            span = h3.find('span')
            f.write(span.get_text())
            f.write('\n')

        

    