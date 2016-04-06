# -*- coding: utf-8 -*-
import time
import requests
import requests_cache
from bs4 import BeautifulSoup
requests_cache.install_cache('hnkeywords', expire_after=180)


keywords = ['python', 'data', 'eff', 'science', 'linux']
response = requests.get('https://news.ycombinator.com/')
print "From cache: {}\n{}".format(response.from_cache,
                                  time.ctime(int(time.time())))

soup = BeautifulSoup(response.text, "lxml")
titles = soup.find_all('td', class_='title')
data = {x.text: x.a['href'] for x in titles if x.a}

for item, url in data.items():
    for keyword in keywords:
        if keyword in item.lower():
            print "[{}] {}: {}".format(keyword, item.encode('utf-8'), url)
