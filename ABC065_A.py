n,m,p=map(int,input().split())
sum=n+m
if p <= m:
    print("delicious",end='\n')
elif sum >= p:
    print("safe",end='\n')
else:
    print("dangerous",end='\n')