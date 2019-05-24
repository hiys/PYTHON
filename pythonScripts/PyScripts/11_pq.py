from pyquery import PyQuery as pq

doc = pq('http://172.40.50.127:8000/blog/list')

trs = doc('table > tr')

for tr in trs[1:]:
    print(pq(tr)('td:eq(0)').text())
