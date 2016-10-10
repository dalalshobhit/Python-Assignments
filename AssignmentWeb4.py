# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
count = raw_input('Enter count: ')
position = raw_input('Enter position: ')
print "Retrieving: " + url
position = int(position)
count = int(count)
i = 0

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")


# Iterate for 'count' time
while (i < count):
    # Retrieve all of the anchor tags
    tags = soup('a')
    # Crawl to link at position -> 'position'
    newURL = tags[position-1]
    URL = newURL.get('href', None)
    html = urllib.urlopen(URL).read()
    soup = BeautifulSoup(html, "html.parser")
    i = i + 1
    print "Retrieving: " + URL