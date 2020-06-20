if __name__ == '__main__':
    s = input()

first = False
second = False
three = False
four = False
five = False

for a in s:
    if a.isalnum():
        first = True
    if a.isalpha():
        second = True
    if a.isdigit():
        three = True
    if a.islower():
        four = True
    if a.isupper():
        five = True

print(first)
print(second)
print(three)
print(four)
print(five)