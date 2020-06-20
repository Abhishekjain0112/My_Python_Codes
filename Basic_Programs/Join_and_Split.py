def split_and_join(line):
    # write your code here
    list1 = line.split(" ")
    line = "-".join(list1)
    return line


line = input("Enter The Value Here : ")
result = split_and_join(line)
print(result)
'''
Enter The Value Here : hello i am abhishek  jain 
hello-i-am-abhishek--jain-
'''