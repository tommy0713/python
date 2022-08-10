page='''
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book category="COOKING">
<title lang="en">Everyday Italian</title>
<author>Giada De Laurentiis</author>
<year>2005</year>
<price>30.00</price>
</book>

<book category="CHILDREN">
<title lang="en">Harry Potter</title>
<author>J K. Rowling</author>
<year>2005</year>
<price>29.99</price>
</book>

<book category="WEB">
<title lang="en">XQuery Kick Start</title>
<author>James McGovern</author>
<author>Per Bothner</author>
<author>Kurt Cagle</author>
<author>James Linn</author>
<author>Vaidyanathan Nagarajan</author>
<year>2003</year>
<price>49.99</price>
</book>

<book category="WEB">
<title lang="en">Learning XML</title>
<author>Erik T. Ray</author>
<year>2003</year>
<price>39.95</price>
</book>

</bookstore>
'''
from bs4 import BeautifulSoup
from lxml import etree
soup = etree.HTML(page)

# soup=BeautifulSoup(page,'lxml')
data=soup.xpath('//book')
for i in data:
    print(i)
    print('*'*40)