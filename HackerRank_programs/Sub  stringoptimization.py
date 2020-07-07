#name = input("Enter the String:")
name = 'BANANA'

x, y = 0, 0

l = len(name)
mylist=list()
tup =('A', 'E', 'I', 'O','U')

for i in range(l):
    s=name[i]
    sum1=l-i
    #print(s)
    if s in tup:
        #print( " i :",i,"if : ",s ,"Sum = ",sum1 )
        x = x + sum1
        sum1=0
    else:
        #print(" i :", i, "else: ",s,"Sum = ",sum1)
        y = y + sum1
        sum1=0
if x > y:
    print("Vowel", x)
elif x == y:
    print("draw")
else:
    print("Consonent", y)  # your code goes here
#print(mylist)
print("Vowel", x)
print("Consonent", y)
