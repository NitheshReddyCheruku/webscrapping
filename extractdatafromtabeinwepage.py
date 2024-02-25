import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.worldometers.info/world-population/'
page=requests.get(url)
print(page.text)
soup=BeautifulSoup(page.text,'lxml')
print(soup)
t=soup.find_all('div',class_='navbar-collapse collapse')
a=[]
for i in t:
    x=i.text
    a.append(x)
print(a)
table=soup.find('table',class_='table table-striped table-bordered table-hover table-condensed table-list')
print(table)
x1=table.find_all('th')
print(x1)
x3=[]
for i in x1:
    e=i.text
    x3.append(e)
print(x3)
y=pd.DataFrame(columns=x3)
print(y)
for i in  table.find_all('tr')[1:]:
    rowdata=i.find_all('td')
    row=[tr.text for  tr in rowdata]
    length=len(y)
    y.loc[length]=row
print(y)
y.to_csv('C:\webscarpper\collect.csv')
