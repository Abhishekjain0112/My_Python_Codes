# Enter your code here. Read input from STDIN. Print output to STDOUT

l = input().split(" ")
N = int(l[0])
M = int(l[1])
f = int(N/2)
k=1
for i in range(f):
    for j in range(f-i):
        print("---",end="")
    for j in range(k):
        print(".|.",end="")
    k +=2
    for j in range(f-i):
        print("---",end="")
    print("")
print("-"*int((M-7)/2),end="WELCOME")
print("-"*int((M-7)/2))
k -=2
for i in range(f):
    for j in range(i+1):
        print("---",end="")
    for j in range(k):
        print(".|.",end="")
    k -=2
    for j in range(i+1):
        print("---",end="")
    print("")

'''
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

'''