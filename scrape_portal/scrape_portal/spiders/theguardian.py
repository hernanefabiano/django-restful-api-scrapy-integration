import scrapy
import re
import time
import json
from datetime import datetime as dt
from scrape_portal.items import GuardianItem

class GuardianSpider(scrapy.Spider):
    name = "theguardian"
    allowed_domains = ['theguardian.com']
    news_urls = ['international', 'uk-news', 'world', 'uk/sport']

    def __init__(self, scrape_date=None, *args, **kwargs):
        super(GuardianSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.theguardian.com/%s' % (path) for path in self.news_urls]

    def parse(self, response):
        # parse thru each of the element
        for element in response.css('div.fc-item__container'):
            item = GuardianItem()
            item['category']     = response.url.split('/')[-1]
            item['section']      = element.css('span.fc-item__kicker::text').extract_first()
            item['headline']     = element.css('span.js-headline-text::text').extract_first()
            item['url']          = element.css('a.fc-item__link::attr(href)').extract_first()
            item['summary']      = element.css('div.fc-item__standfirst::text').extract_first()
            item['media']        = element.css('source::attr(srcset)').extract_first()
            item['datescrapped'] = dt.today().strftime('%Y-%m-%d')
            yield item
