# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import scrapy

class ModulItem(scrapy.Item):
    model = scrapy.Field()
    model_url = scrapy.Field()
    shops = scrapy.Field()
    start_price = scrapy.Field()
    end_price = scrapy.Field()
    img_url = scrapy.Field()
    image_urls = scrapy.Field()