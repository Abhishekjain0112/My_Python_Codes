import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




url = 'http://py4e-data.dr-chuck.net/comments_702526.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
#print('Retrieved', len(data), 'characters')

#print(data.decode())
tree = ET.fromstring(data)
sum = 0
results = tree.findall('comments/comment')
print(results)
for item in results:
    print("value : ",item.find('count').text)
    sum = sum + int(item.find('count').text)



print(sum)