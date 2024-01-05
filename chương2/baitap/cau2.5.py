import xml.dom.minidom

with open('"E:\chương2\baitap\sample.xml"', 'r') as file:
    NoiDung = file.read()

dom = xml.dom.minidom.parseString(NoiDung)

PhanTu = dom.getElementsByTagName('*')

for i in PhanTu:
    print(i.tagName)