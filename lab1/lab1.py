from bs4 import BeautifulSoup
from requests import get
from json import dump
from sqlite3 import connect

BASE_URL = 'https://www.khnu.km.ua'
url = BASE_URL + '/root/page.aspx?l=0&r=3&p=3'
print(url)

page = get(url)
soup = BeautifulSoup(page.content, 'html.parser')
faculties = []
facult=''

i= 0

connections = connect("lab2.db")
cursor = connections.cursor()

for el in soup.find(id="site-content").find('div').find_all('div'):
    el_h3 = el.find('a').find('h3')
    el_a=el.find('a')
    if el_h3 != None: 
        facult=el_h3.getText()
        for el in faculties:
            facult.append(el.getText())
            cursor.execute(
                "INSERT INTO faculties (name, faculty) VALUES (?, ?)",
                [el.getText(), i]
            )
    else:
        if el_a.getText() != "":
            faculties.append(el_a.getText())
            cursor.execute(
                "INSERT INTO faculties (name, faculty) VALUES (?, ?)",
                [el.getText(), i]
            )

        faculty = {
            "name": el_h3.getText(),
        }
        cursor.execute(
            "INSERT INTO faculties (name, url) VALUES (?, ?)",
            [faculty['name']]
        )
        faculties.append(faculty)
        i+=1
    connections.commit()

connections.close()

