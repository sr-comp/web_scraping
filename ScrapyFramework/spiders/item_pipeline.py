import scrapy
from ..items import ScrapyframeworkItem

class ItemPipelineSpider(scrapy.Spider):
    name = 'itempipelinespider'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response, **kwargs):
        print('#'*100)
        data = ScrapyframeworkItem()
        for info in response.css('div.quote'):
            data['titel'] = info.css('span.text ::text').get()
            data['author'] = info.css('small.author ::text').get()
            data['tags'] = info.css('div.tags a ::text').getall()
            yield data
