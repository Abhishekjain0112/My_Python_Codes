R = 7
p = 40/100
n = int(input("Average number of planet that can support life :"))
f = 13/100


i = float(input("% of those who can develop intelligent life :"))/100
c = float(input("% of those who are will contact :"))/100
L = int(input("Expected life for civilisation :"))

N = R*p*n*f*i*c*L

print(" the Estimated number : ", N)
