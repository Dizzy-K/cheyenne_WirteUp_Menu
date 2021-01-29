import re, requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import unquote

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

ques = input("请输入想查找的题目：")

html = requests.get('https://davidcheyenneone.github.io/Misc/CTFshow/CTFshow.html')
soup = BeautifulSoup(html.text,"lxml")
a = soup.body.find_all('a')
chlid = []
for i in a:
    ff = re.search('\">', str(i))
    f = str(i)[9:ff.span()[0]]
    chlid.append(f)

for j in tqdm(chlid):
    htmlj = requests.get('https://davidcheyenneone.github.io/Misc/CTFshow/{0}'.format(j), headers = headers)
    if ques in str(BeautifulSoup(htmlj.text,"lxml")):
        print(ques, "is in ", unquote(j))
        print('https://davidcheyenneone.github.io/Misc/CTFshow/{0}'.format(j))
        break
    else:
        htmlj.keep_alive = False
    print('Sorry, Question unfind')

