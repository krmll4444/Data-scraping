from bs4 import BeautifulSoup
from khnu.items import InstituteItem
import scrapy
# '/root/page.aspx?l=0&r=3&p=3'



class FacultSpider(scrapy.Spider):
    name = "khnu"
    BASE_URL = "https://www.khnu.km.ua"
    start_urls = ["https://www.khnu.km.ua"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        institutes_array = soup.find(id="site-content").find('div').find('div').find_all('a')
        for inst in institutes_array:
            yield InstituteItem(
                name=inst.getText(),
                link=self.BASE_URL + '/root/page.aspx?l=0&r=3&p=3' + inst.get('href')
            )
