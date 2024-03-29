# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LinkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post_id = scrapy.Field
    href = scrapy.Field()
    timestamp = scrapy.Field()
    page_num = scrapy.Field()
    img_type = scrapy.Field()
    pass
