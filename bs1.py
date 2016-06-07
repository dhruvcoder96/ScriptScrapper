#beautiful soup program

import urllib
from BeautifulSoup import *
site=raw_input("Enter the site: ")
handle=urllib.urlopen('http://'+site).read()
#handle for beautiful soup
handle1= BeautifulSoup(handle)
lst=handle1('script')

for tags in lst:
	print tags.get('src',None)

