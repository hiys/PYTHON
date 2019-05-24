import urllib.request
response = urllib.request.urlopen('http://python.org/')
html = response.read()
print(html)


for i in range(39):
    # https: // s.taobao.com / search?q = % E6 % 89 % 8
    # B % E6 % 9
    # C % BA & imgfile = & commend = all & ssid = s5 - e & search_type = item & sourceId = tb.index & spm = a21bo
    # .2017
    # .201856 - taobao - item
    # .1 & ie = utf8 & initiative_id = tbindexz_20170306 & cps = yes & ppath = 20000 % 3
    # A30111 % 3
    # B12304035 % 3
    # A11835346 % 3
    # B10004 % 3
    # A827902415 & bcoffset = 3 & p4ppushleft = % 2
    # C48 & s = 0 & ntoffset = 39
    s = i * 44