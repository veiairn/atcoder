n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

l.sort(key=int)
print(l[0],end='\n')