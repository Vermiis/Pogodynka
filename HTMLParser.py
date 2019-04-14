from html.parser import HTMLParser
from bs4 import BeautifulSoup
import lxml.html
import urllib
from lxml import etree

class EtreeParser:


    def GetXpathText(self, xpathtext):
        htmlfile = ""  #htmlstr
        tempValList=[]
        info = etree.XML(htmlfile)

        x = info.xpath(xpathtext)
        tempValList.append(x)





#<!--nucleo, fin del prologo -->




#1st selector body > table > tbody > tr:nth-child(2) > td:nth-child(2) > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(2) > font
    #xpath selector /html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[1]/td[2]/font
    #/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td[2]/font
    #/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[30]/td[2]/font


    def get_page_data(self, days, day, month, year):
        addrstr = "https://www.ogimet.com/cgi-bin/gsynres?lang=en&ord=REV&ndays=" + days + "&ano=" + year + "&mes=" + month + "&day=" + day + "&hora=18&ind=12600"
        page = urllib.urlopen(addrstr)
        htmlstring = page.read()
        return  htmlstring



#https://www.ogimet.com/cgi-bin/gsynres?lang=en&ord=REV&ndays=30&ano=2015&mes=02&day=01&hora=18&ind=12600
