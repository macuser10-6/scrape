from requests_html import HTMLSession

urls = [
    ''
    ''
    ''
]


def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="priceblocck_ourprice"]', first=True).text
    }
    print(product)
    return product


tvprices = [getPrice(url) for url in urls]
print(len(tvprices))
