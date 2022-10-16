from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()

url = 'https://www.amazon.com/deals?ref_=nav_cs_gb'


def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    return BeautifulSoup(r.html.html, 'html.parser')
