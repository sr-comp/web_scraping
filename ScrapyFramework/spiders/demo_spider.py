import scrapy

class DemoSpider(scrapy.Spider):
    name = 'demospider'
    # start_urls = ['https://quotes.toscrape.com/','https://www.python.org/','https://www.skysports.com/']
    start_urls = ['https://quotes.toscrape.com/']
    def parse(self, response, **kwargs):
        print('#'*100)
        # print(response)
        # print(response.xpath('//title/text()').get())
        # 'tags': response.css('div.tags a ::attr(href)').getall(),
        for data in response.css('div.quote'):
            yield {
                'titel': data.css('span.text ::text').get(),
                'author': data.css('small.author ::text').get(),
                'tags': data.css('div.tags a ::text').getall()
            }
        next_page = response.css('li.next a::attr(href)').get()
        # #urljoin
        # if next_page:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(url=next_page, callback=self.parse)
        #follow method
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)