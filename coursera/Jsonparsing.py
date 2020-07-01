import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_702527.json'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()


info = json.loads(data)
sum= 0
#print(info)
for js in info['comments']:
    #print(js['count'])
    sum = sum + int(js['count'])

print(sum)