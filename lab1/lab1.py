from bs4 import BeautifulSoup
from requests import get
from json import dump
from re import fullmatch,match
import json

BASE_URL = 'https://www.khnu.km.ua'
url = BASE_URL + '/root/page.aspx?l=0&r=3&p=3'
print(url)

page = get(url)
soup = BeautifulSoup(page.content, 'html.parser')
faculties = []
facult=''
res={}

for el in soup.find(id="site-content").find('div').find_all('div'):
    el_h3 = el.find('a').find('h3')
    el_a=el.find('a')
    if el_h3 != None: 
        facult=el_h3.getText()
        res[el_h3.getText()]=[]
    else:
        if el_a.getText() != "":
            res[facult].append(el_a.getText())

print(res)

with open("lab.json", "w", encoding="utf-8") as json_file:
    dump(res, json_file, ensure_ascii=False, indent=4)
# with open("lab1.json", "w", encoding="utf-8") as json_file:
#     dump(res, json_file, ensure_ascii=False, indent=4)
#     href_facult = fullmatch(r'/[a-z]+/[a-z]+/[a-z]+', el_a['href'])
#     if href_facult is not None:
#         departments = []
#         try:
#             chair = el.find(class_="disp_none").find(class_="disp_none").find_all('a')
#         except Exception:
#             departments = None
#         else:
#             departments = [el.getText() for el in chair]        

#         faculty = {
#             "name": el_a.getText(),
#             "url": href_facult.group(0),
#             "departments": departments,
#         }
#         faculties.append(faculty)