from pyquery import PyQuery as pq

for i in range(1,4):
    url = "http://quotes.toscrape.com/page/{0}/"\
        .format(i)

    doc = pq(url)
    divs = doc('div.quote')
    for d in divs:
        author =pq(d)('small').text()
        url = pq(d)('a[class!="tag"]').attr('href')