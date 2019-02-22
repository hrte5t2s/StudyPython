import requests
from bs4 import BeautifulSoup
import sqlite3


def get_webpage():
    url = "https://www.kuaidaili.com/free/inha/1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
    res = requests.get(url=url, headers=headers)
    return res


def soup(res):
    soup = BeautifulSoup(res.text, "html.parser")
    try:
        trs = soup.tbody.find_all("tr")
        for tr in trs:
            IP = tr.find("td", attrs={"data-title": "IP"}).get_text()
            Port = tr.find("td", attrs={"data-title": "PORT"}).get_text()
            save_news_to_db(IP, Port)


def createdb():
    try:
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
  e5t      create_news_table = "CREATE TABLE News(id INTEGER PRIMARY KEY, title TEXT, time TEXT)"
        cursor.execute(create_news_table)
    except BaseException as e:
        print(e)


def save_news_to_db(title, news_time):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    create_news_table = "CREATE TABLE News(id INTEGER PRIMARY KEY, title TEXT, time TEXT)"
    cursor.execute(create_news_table)
    insert_sql = "INSERT INTO News(title, score) VALUES('"+str(title)+"','" + str(news_time)+"')"
    cursor.execute(insert_sql)
    print("save success")
    connect.commit()
    cursor.close()
    connect.close()


def main():
    create_db()
    res = get_webpage()
    print(res.text)
    soup(res)


if __name__ == "__main__":
    main()