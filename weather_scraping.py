import requests
from bs4 import BeautifulSoup as bs

place='jaipur'
url='https://www.google.com/search?q=weather'+place
response=requests.get(url)

soup=bs(response.content,"lxml")

temp=soup.find("div",class_='BNeawe iBp4i AP7Wnd').text+'\n'
more=soup.find('div',class_='BNeawe tAd8D AP7Wnd').text

i=more.find('\n')
print(i+1)
cond=more[i+1:]

l=[]
place=place+'\n'
l.append(more)
l.append(cond)
print(l)
print(place+temp+more)

# txt='\weather pauri'
# if txt[0:8]=='\weather':
#     print(txt[9:])