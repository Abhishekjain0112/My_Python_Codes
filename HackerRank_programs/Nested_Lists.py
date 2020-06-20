list1=[]
scores= set()
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l=[name,score]
        list1.append(l)
        scores.add(score)

print(list1)
list1.sort()
print(list1)

sorted(scores)
shotest_score=sorted(scores)[1]
print(sorted(scores))

name_list= []
for name, score in list1:
    if(score==shotest_score):
        name_list.append(name)

for name in sorted(name_list) :
    print(name)

