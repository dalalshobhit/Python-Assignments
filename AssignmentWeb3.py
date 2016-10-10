# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import BeautifulSoup
num = list()

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
# Parse HTML page using BeautifulSoup library
soup = BeautifulSoup(html)

# Retrieve all of the span tags
tags = soup('span')
# Read the value for all span tags and convert it to int
for tag in tags:
    num.append(int(tag.contents[0]))
    
# Print sum of all values
print sum(num)