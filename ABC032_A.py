n=int(input())
m=int(input())
p=int(input())

min=min(n,m)
max=max(n,m)

if(p%min==0):
    start=p
else:
    start=((p//min)+1)*min

for i in range(start,start+(n*m),min):
    if(i%max==0):
        print(i)
        break