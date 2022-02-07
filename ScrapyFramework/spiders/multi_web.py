import scrapy

class MultiWebSpider(scrapy.Spider):
    name = 'multiwebspider'
    start_urls = ['https://4nightmovie.click/','https://hexdownload.co/']
    def parse(self, response, **kwargs):
        print('#'*10)
        for night in response.css('article.introMovie'):
            yield {
                'titel': night.css('a.moviename ::text').get(),
                'story': night.css('div.shortStory ::text').get(),
                'dir': night.css('li.col65 a ::text').getall()[-1]
            }

        for data in response.css('div.post-right'):
            yield{
                'film_name': data.css('p.film-name ::text').get(),
                'genre': data.css('p.film-genre a ::text').get()

            }

        links = response.css('footer.footerp a::attr(href)').getall()
        for link in links:
            link = response.urljoin(link)
            yield scrapy.Request(url=link, callback=self.movie)

    def movie(self,response):
        yield {
            'download': response.css('ul.l1nk a ::attr(href)').getall()
        }