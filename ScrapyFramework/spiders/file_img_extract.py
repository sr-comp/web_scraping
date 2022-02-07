import scrapy
from ..items import ScrapyframeworkItem

class FileImgExtractSpider(scrapy.Spider):
    name = 'fileimgextractspider'
    start_urls = ['https://books.toscrape.com/', 'https://music-fa.com/download-songs/']

    def parse(self, response, **kwargs):
        print('#'*100)
        data = ScrapyframeworkItem()

        picture = []
        for img in response.css('article.product_pod'):
            image = img.css('a img ::attr(src)').get()
            download = response.urljoin(image)
            picture.append(download)

        data['image_urls'] = picture
        yield data

        song = []
        for info in response.css('article.pstfa'):
            film = info.css('audio ::attr(src)').get()
            download = response.urljoin(film)
            song.append(download)

        data['file_urls'] = song
        yield data
