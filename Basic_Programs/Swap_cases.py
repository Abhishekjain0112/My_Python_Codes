#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2
#
def swap_case(s):
    s1=""
    for a in s:
        if a.isupper():
            s1+=a.lower()
        elif a.islower():
            s1 += a.upper()
        else :
            s1 +=a

    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
