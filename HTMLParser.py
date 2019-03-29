from html.parser import HTMLParser
from bs4 import BeautifulSoup
import lxml.html

import urllib


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

#<!--nucleo, fin del prologo -->


class SoupParser:
    def get_tag_data(self, tagname, htmlfile):
        soup = BeautifulSoup(htmlfile, 'html.parser')
        doc = lxml.html.fromstring(htmlfile)
        for element in doc.xpath('//label[contains(text(), "PRICE:")]/ancestor::div[@class="price_class"]'):
            print('Found %s: %s' % (element.tag, element.text_content().strip()))



    def get_page_data(self):
        page = urllib.urlopen('http://www.google.com/')
        htmlstring = page.read()
        return  htmlstring

