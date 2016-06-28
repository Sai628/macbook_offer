# -*- coding: UTF-8 -*-

import cStringIO
import urllib2

import requests
from PIL import Image
import BeautifulSoup as bs


index_url = "http://appled.cc"


def get_soup(url):
    html = requests.get(url).content
    return bs.BeautifulSoup(html)


def get_offer_picture():
    soup = get_soup(index_url)
    urlSuffix = soup.findAll("h4", {"class": "title"})[0].a["href"]
    target_url = index_url + str(urlSuffix)

    soup = get_soup(target_url)
    div = soup.findAll("div", {"class": "entry typo"})[0]

    for img in div.findAll("img"):
        src = img["src"]
        file = urllib2.urlopen(src)
        tmp_image = cStringIO.StringIO(file.read())
        im = Image.open(tmp_image)
        im.show()


get_offer_picture()
