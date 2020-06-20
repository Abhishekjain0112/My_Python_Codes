print("abhi")
ii = ord('a')-1
print((chr(ii+1)))

n = int(input("Enter Value : "))
ch = ord('a')+n-1
for i in range(n):
    for j in range(n-i-1):
        print("--", end="")

    ch = ord('a') + n - 1
    for j in range(i+1):
        print(chr(ch), end="")
        if j != i:
            print("-",end="")
        ch = ch - 1
    ch = ch + 1
    for j in range(i):
        print("-", end="")
        print(chr(ch+1), end="")
        ch = ch + 1
    for j in range(n-i-1):
        print("--", end="")
    print()

for i in range(n-1):

    for j in range(i+1):
        print("--", end="")
    ch = ord('a') + n - 1
    for j in range(n-i-1):
        print(chr(ch), end="")
        ch = ch - 1
        if j != (n-i-2):
            print("-",end="")
    ch = ch + 1
    for j in range(n-2-i):
        print("-", end="")
        print(chr(ch+1), end="")
        ch = ch + 1
    for j in range(i+1):
        print("--", end="")

    print()


