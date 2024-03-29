n=int(input())
l=[]
for _ in range(n):
    l.append(int(input()))
l.sort(key=int,reverse=True)
max=l[0]
for i in range(n):
    if l[i]!=max:
        print(l[i],end='\n')
        break