#!/usr/bin/env python3

import requests as req
class A(object):
    def __init__(self, URL):
        self.x = 'Hello'


def prepareURL(days, day, month, year):
    addrstr = "https://www.ogimet.com/cgi-bin/gsynres?lang=en&ord=REV&ndays=" + days + "&ano=" + year + "&mes=" + month + "&day=" + day + "&hora=18&ind=12600"
    return addrstr

def getSiteData(URL):
    resp = req.get(URL)
    data = resp.text
    return data



