l=[]
for i in range(5):
    l.append(int(input()))
d=int(input())
l.sort(key=int)
print(":(" if l[-1]-l[0]>d else "Yay!")