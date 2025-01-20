import requests
from bs4 import BeautifulSoup
import sqlite3
import re

con = sqlite3.connect('posts.db')
cur = con.cursor()
create_table_statements = """CREATE TABLE IF NOT EXISTS iranjib(
                                id,
                                url,
                                title,
                                summary,
                                content,
                                date)"""
cur.execute(create_table_statements)

keywords = ['ارز', 'طلا', 'سکه']
links = []

for page_num in range(0, 300):
    archive_url = f'https://www.iranjib.ir/showarchive/{page_num}/0/'
    res = requests.get(archive_url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    news = soup.find_all(name='tr')

    for item in news[1:-1]:
        news_date = item.find_all(name='td')[2].getText()
        yearReg = re.findall('۱۴۰۳', news_date)
        views = int(item.find_all(name='td')[1].getText().split()[0])
        title = item.find_all(name='td')[0].getText().split()

        if yearReg:
            if (views >= 1000)  and any(keyword in title for keyword in keywords):
                news_link = '/'.join(item.find_all(name='a')[0]['href'].split('/')[0:5]) + '/'
                links.append(news_link)
        else:
            break
    for id, url in enumerate(links):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find('h1').getText()
        summary = soup.find('div',attrs={'class':'newssummary'}).getText()
        content_list = soup.find_all('p')
        content = ''
        for p in content_list:
            content += p.getText() + '\n'
        date_table = soup.find_all('table', attrs= {'class':'cellspacing0'})[0]
        date = date_table.find_all('td')[4].getText()
        insert_statements = """INSERT INTO iranjib
                                (id,url,title,summary,content,date)
                                VALUES
                                (?,?,?,?,?,?)"""
        cur.execute(insert_statements,(id,url,title,summary,content,date))
        con.commit()

con.close()
