# -*- coding: utf-8 -*-
'''
Created on June 1, 2013

@author: Canh Duong
'''

from scrapy import log
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders.crawl import Rule
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from honeybay.items import DealItem
from datetime import datetime

class GrouponSpider(CrawlSpider):
    name = "honeybay.com"
    start_urls = [
        'http://www.honeybay.com/',
    ]
    rules = (
        # nav
        Rule(SgmlLinkExtractor(allow=(r'/c/[a-z]+',)),
            follow=True,),
        # follow deals
        Rule(SgmlLinkExtractor(allow=(r'/deals/.+',)),
            callback='parse'
        ),
    )

    def parse(self, response):
        log.msg('[CRAWLED] - %s' % response.url, level=log.INFO)

        hxs = HtmlXPathSelector(response)
        item = DealItem()
        item['offer'] = hxs.select('//div[@class="deal-name"]/h1/text()').extract()[0].strip()
        item['company'] = 'honeybay.com'
        item['start_date'] = datetime.now().strftime('%d/%m/%Y')
        item['end_date'] = ""
        item['s_price'] = hxs.select('//div[@class="deal-discount-price number"]/text()').extract()[0].strip()
        item['us_price'] = item['s_price']  
        item['discount'] = 0.00
        item['category'] = ""
        item['main_deal'] = 'No'
        item['sold'] = hxs.select('//div[@class="deal-num-of-bought  number "]/span/text()').extract()[0].strip()
        item['total_sales'] = float(item['s_price'])*int(item['sold'])
        item['merchant'] = 0
        item['merchant_contact'] = hxs.select('//div[@class="location-address"]/b[1]/text()').extract()[0].strip()
        item['deal_in_DayWatch'] = ""
        item['offer_id'] = ""
        item['link'] = response.url

        print item



