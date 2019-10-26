from html.parser import HTMLParser
from lxml import etree
from html.parser import HTMLParser
from html.entities import name2codepoint

class EtreeParser:


    def GetXpathText(self, xpathtext):
        htmlfile = ""  #htmlstr
        tempValList=[]
        info = etree.XML(htmlfile)

        x = info.xpath(xpathtext)
        tempValList.append(x)

def getGrid(htmlstr):
    s2 = htmlstr.split('Daily summary at')[1]
    s2=s2.split('</table>')[0]
    return s2

def getGridData(tablestr):








#<!--nucleo, fin del prologo -->




#1st selector body > table > tbody > tr:nth-child(2) > td:nth-child(2) > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(2) > font
    #xpath selector /html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[1]/td[2]/font
    #/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td[2]/font
    #/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[30]/td[2]/font




#https://www.ogimet.com/cgi-bin/gsynres?lang=en&ord=REV&ndays=30&ano=2015&mes=02&day=01&hora=18&ind=12600
