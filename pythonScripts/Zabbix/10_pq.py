from pyquery import PyQuery as pq

doc = pq('http://172.40.50.127:8000/blog/list')
trs = doc('tr[id]')
for tr in trs:
    title = pq(tr)('td:eq(0)').text()
    desc = pq(tr)('td:eq(1)').text()
    print(title,desc)
