import urllib
import xml.etree.ElementTree as ET

sum = 0
serviceurl = 'http://python-data.dr-chuck.net/comments_288744.xml'

url = serviceurl
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
    
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print "Count: ",len(counts)
    
for count in counts :
    number = count.text
    sum = sum + int(number)
        
print "Sum: ",sum