# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoldItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    amount = scrapy.Field()
    time = scrapy.Field()
    benefit = scrapy.Field()
    percentage = scrapy.Field()
    minium = scrapy.Field()



