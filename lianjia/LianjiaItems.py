# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    location = scrapy.Field()
    start = scrapy.Field()
    amount = scrapy.Field()
    num_person = scrapy.Field()
    progress = scrapy.Field()



