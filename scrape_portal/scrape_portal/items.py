# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuardianItem(scrapy.Item):
    # define the fields for your news relevant information
    category     = scrapy.Field()
    section      = scrapy.Field()
    headline     = scrapy.Field()
    url          = scrapy.Field()
    summary      = scrapy.Field()
    media        = scrapy.Field()
    datescrapped = scrapy.Field()
