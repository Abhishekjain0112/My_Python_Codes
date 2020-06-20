n = int(input('Enter Number  of rows :'))

for i in range(0, n):
    for j in range(n, i, -1):
        print(' ', end='')
    for k in range(0,i+1):
        print('* ', end='')
    print()
