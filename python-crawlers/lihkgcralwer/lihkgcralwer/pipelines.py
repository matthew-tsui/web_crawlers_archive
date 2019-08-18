# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem
from datetime import datetime

class LihkgcralwerPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if re.search('^(http|https):',item['href']):
            if(item['href'] not in self.ids_seen):

                return item
            else:
                raise DropItem
        else:
            raise DropItem
