number=int(input("Welcome To Program of Checking Prime Number or Not \n Enter The Number ="))
for i in range(2,number,1):
    if number%i==0:
        print(" This Number is Not A Prime ")
        break
else:
    print("The Number  is Prime ")