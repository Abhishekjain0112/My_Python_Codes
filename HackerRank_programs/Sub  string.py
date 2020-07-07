name = input("Enter the String:")

x, y = 0, 0

l = len(name)
mylist=list()
tup =('A', 'E', 'I', 'O','U')

for i in range(l):
    for j in range(i+1, l+1):
        s=name[i]
        #print(s)
        mylist.append(s)
        if s[0] in tup:
            x = x + 1
        else:
            y = y + 1
if x > y:
    print("Vowel", x)
elif x == y:
    print("draw")
else:
    print("Consonent", y)  # your code goes here
#print(mylist)
