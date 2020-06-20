def print_formatted(number):
    # your code goes here
    #w= len("{0:b}".format(number))
    w = len("{0:b}".format(number))
    for i in range(1,number+1,1):
        #s = " {0:{w}d} {0:{w}0}{0:{w}X}{0:{w}b}"
        #print(s.format(i,w=w))
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b} i".format(i, w=w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)