# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
import time
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f/index/forumpark?cn=&ci=0&pcn=小说&pci=161&ct=&st=new&p=1']
    url_h = "http://tieba.baidu.com/f/index/forumpark?cn=&ci=0&pcn=小说&pci=161&ct=&st=new&pn="
    flag = 1
    def parse(self, response):
        quotes = response.css('.ba_content')
        for quote in quotes:
            item = TutorialItem()
            item['name'] = quote.css('.ba_name::text').extract_first()
            item['people'] = quote.css('.ba_num .ba_m_num::text').extract_first()
            item['commit'] = quote.css('.ba_num .ba_p_num::text').extract_first()
            item['text'] = quote.css('.ba_desc::text').extract_first()
            yield item
        self.flag = self.flag+1
        url = self.url_h + str(self.flag)
        if self.flag <= 30:
            yield scrapy.Request(url=url, callback=self.parse)


