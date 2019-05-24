from pyquery import PyQuery as pq

doc = pq("<html><a>abc</a></html>")

print(doc.html())
print(doc.text())