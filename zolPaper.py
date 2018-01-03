import requests
import urllib.request
import uuid
from bs4 import BeautifulSoup
import os


if os.path.exists('D:\image') == True:  # 如果目录不存在则创建
    print("image dir is exsit")
else:
    os.mkdir('image')
i = 0
for page in range(1,50):
    url = 'http://desk.zol.com.cn/1920x1080/'+str(page)+'.html'
    #print(url)
    r = requests.get(url)
    contents = r.text

    soup = BeautifulSoup(contents,'html.parser')
    uls = soup.find_all('ul','pic-list2')

    for ul in uls:
        hrefs = ul.find_all('a')
        for href in hrefs:
            newurl = 'http://desk.zol.com.cn'+href['href']
            newr = requests.get(newurl)
            newcontents = newr.text

            newsoup = BeautifulSoup(newcontents,'html.parser')
            newuls = newsoup.find_all('li','show1')
            for newul in newuls:
                newhrefs = newul.find_all('img')
                for newhref in newhrefs:
                    print(newhref['src'])
                    urllib.request.urlretrieve(newhref['src'].replace('144x90','1920x1080'),'D:\image\%s.jpg'%i)
                    i += 1
                    print('成功抓取第%s张图片'%i)
print('共抓取'+str(i)+'张图片')
