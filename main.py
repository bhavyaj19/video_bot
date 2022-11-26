from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from pytube import YouTube
import time

urls=[
    # "/c/MrwhosethebossShorts1/shorts",
    "/c/SlickStevie/shorts",
    "/channel/UCIBQ5aZ0m1RfzSqqbkQ_eAw/shorts",
    "channel/UCK1hLFdqOsnfWuDuVx4PwTg/shorts",
    "c/Gaming217_/shorts"
]
def get_browser_ready():
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
    driver.get('https://www.youtube.com{}'.format(urls[1]))

    # scroll to bottom of page
    # driver.execute_script("window.scrollTo(0,{})".format(height)) #to scroll the page 
    for i in range(100):
        height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.find_element('tag name','body').send_keys(Keys.END)
        time.sleep(5)
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        if last_height == height:
            break
    time.sleep(6)
    get_browser_ready.content = driver.page_source.encode('utf-8').strip()
    get_url()


def get_url():
    # get url of channel 
    soup=BeautifulSoup(get_browser_ready.content,'lxml')
    video_url= soup.find_all('a',{"class":"yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-slim-media"})
    j=0
    get_url.all_urls = []
    for i in video_url:
        # print('https://www.youtube.com{}'.format(video_url[j].get('href')))
        get_url.all_urls.append(video_url[j].get('href'))
        j+=1

        # storing urls to a file
    with open('urls','w+') as f:
        for items in get_url.all_urls:
            f.write('%s\n' %items)
        print('All Urls Stored to file')

    time.sleep(3)
    # get_audio()


def get_audio():
    PATH="audio_files"
    j=0
    f = open('urls','r')

    for i in f.readlines():
        yt = YouTube('https://www.youtube.com{}'.format(i, end=''))
        
        yt.streams.filter(only_audio=True).first().download(
            output_path=PATH,
            filename='audio{}.mp3'.format(j)
        )
        j+=1
    

# get_browser_ready()
get_audio()
