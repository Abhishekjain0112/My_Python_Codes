import re

head = open('data.txt')
su= 0
for line in head:
    lis = re.findall('[0-9]+',line)
    for n in lis:
        su = su + int(n)

print(su)
