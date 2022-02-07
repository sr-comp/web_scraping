import requests
from bs4 import BeautifulSoup
import re
import random

def download(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # video
    #link = soup.findAll('a', href=re.compile('.mp4'))
    # image
    link = soup.findAll('img', src=re.compile('.jpg'))
    # print(link)
    #download_link=[]

    for info in link:
        #download_link.append(info.get('href'))
        # image
        link = info.get('src')
        print(link)
        with requests.get(link, stream=True) as r:
            name = random.randrange(1, 1000)
            with open(str(name) + '.jpg', 'wb') as f:
                for img in r.iter_content(chunk_size=1024):
                    f.write(img)

    #print(download_link)
    # with requests.get(download_link[0], stream=True) as r:
    # with requests.get(link, stream=True) as r:
    #     # with open('video_1.mp4', 'wb') as f:
    #     with open(str(name)+'jpg', 'wb') as f:
    #         for video in r.iter_content(chunk_size=1024):
    #             f.write(video)

# download('https://video.varzesh3.com/video/243637/%D8%B4%D8%A8%DB%8C%D9%87-%D8%B3%D8%A7%D8%B2%DB%8C-%D8%AF%DB%8C%D8%AF%D8%A7%D8%B1-%D8%B3%D9%88%DB%8C%D8%A7-%D8%A8%D8%A7%D8%B1%D8%B3%D9%84%D9%88%D9%86%D8%A7-%D8%A8%D8%A7-%D9%84%DA%AF%D9%88')
download('https://www.digikala.com/search/category-stationery/')