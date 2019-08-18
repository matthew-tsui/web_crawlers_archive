# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import simplejson as json
from datetime import datetime
import re
from ..items import LinkItem

#excute crawler
# scrapy crawl lihkg_1 -o link.json -a ip='637947' where ip=post_id

class Lihkg1Spider(scrapy.Spider):
    name = 'lihkg_1'
    #allowed_domains = ['https://lihkg.com']
    #start_urls = ['https://lihkg.com/api_v2/thread/637947/page/1?order=reply_time']

    def __init__(self, post_id='', **kwargs):
        super(Lihkg1Spider, self).__init__(**kwargs)
        self.request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "http://thewebsite.com",
        "Connection": "keep-alive" 
    }
        self.post_id = post_id


    def start_requests(self):
        yield scrapy.Request(url='https://lihkg.com/api_v2/thread/'+str(self.post_id)+'/page/1?order=reply_time', callback=self.parse, headers=self.request_headers)

    def parse(self, response):
    	content = json.loads(response.body_as_unicode())
        total_pages = content['response']['total_page']
        for i in range(1,total_pages+1):
            yield scrapy.Request(url='https://lihkg.com/api_v2/thread/'+str(self.post_id)+'/page/'+str(i)+'?order=reply_time', callback=self.parse_page, headers=self.request_headers, meta={'page_num' : i})

    def parse_page(self, response):
        content = json.loads(response.body_as_unicode())
        comment_count = len(content['response']['item_data']) #get the number of comments on that page

        item = LinkItem()
        page_num = response.meta.get('page_num')
        for comment_num in range(comment_count): #loop over every comment
            comment = content['response']['item_data'][comment_num]['msg']
            imgs = Selector(text=comment).xpath('//img/@src').extract()
            
            img_list = list()
            for img in imgs: #loop over all the img links in a comment
                item['post_id'] = self.post_id
                item['page_num'] = page_num
                item['href'] = img
                yield item
        
        



