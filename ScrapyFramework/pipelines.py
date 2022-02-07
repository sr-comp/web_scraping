# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ScrapyframeworkPipeline:
    def process_item(self, item, spider):
        if str(item['author']) == 'Albert Einstein':
            return item
        else:
            raise DropItem('sorry')
