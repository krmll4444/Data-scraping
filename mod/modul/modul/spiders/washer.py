import scrapy
from bs4 import BeautifulSoup
from modul.SeleniumRequest import SeleniumRequest
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
from modul.items import ModulItem

class PhonesSpider(scrapy.Spider):
    name = 'washer'
    allowed_domains = ['ek.ua']
    BASE_URL = 'https://ek.ua/ua'
    start_urls = ['https://ek.ua/ua/list/65/']

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=expected_conditions.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     ".model-shop-name .sn-div")
                ),
            )


    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        last_page = int(soup.find(class_="list-pager").find(class_="ib page-num").find_all('a')[-1].getText())
        for i in range(0, 10):
            yield SeleniumRequest(
                url=f"{self.start_urls[0]}/{i}/",
                callback=self.parse_fridge,
                wait_time=10,
                wait_until=expected_conditions.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     ".model-shop-name .sn-div")
                ),
            )
    def parse_fridge(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        washer_list = soup.find(id="list_form1").find_all('div')
        for washer in washer_list:
            try:
                img_url = washer.find(class_="list-img").find('img').get('src')
                model_wrapper = washer.find(class_="model-short-info").find(class_="model-short-title no-u")
                model = model_wrapper.find('span').getText()
                model_url = model_wrapper.get('href')
                price = washer.find(class_="model-hot-prices-td").find(class_="model-price-range").find('a').find_all(
                    'span')
                start_price = int(price[0].getText().replace('\xa0', ''))
                end_price = int(price[1].getText().replace('\xa0', ''))
                shops = []
                shops_html = washer.find(class_="model-hot-prices").find_all('tr')
                for shop in shops_html:
                    shops.append(shop.find('u').getText())
            except AttributeError:
                continue
            yield ModulItem(
                model=model,
                model_url=f"{self.BASE_URL}{model_url}",
                start_price=start_price,
                end_price=end_price,
                img_url=img_url,
                image_urls=[img_url],
                shops=shops
            )