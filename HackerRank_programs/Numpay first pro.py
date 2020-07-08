import numpy
arr=input().split()
N=int(arr[0])
M=int(arr[1])
#print(N,M)
lis=list()
for i in range(N):
    l = list()
    arr = input().split()
    for j in range(M):
        l.append(int(arr[j]))
    lis.append(l)

my_array = numpy.array(lis)
print(numpy.transpose(my_array))
print(my_array.flatten())