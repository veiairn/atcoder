n,m=map(int,input().split())
p=n+m
if 15<=p and 8<=m:
    print(1,end='\n')
elif 10<=p and 3<=m:
    print(2,end='\n')
elif 3<=p:
    print(3,end='\n')
else:
    print(4,end='\n')