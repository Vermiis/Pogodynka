from HTMLParser import *
from CRUDMSSQL import *
from Webrowser import *


x = prepareURL("30", "01", "08", "2017")
y = getSiteData(x)
z = getGrid(y)
print(z)
