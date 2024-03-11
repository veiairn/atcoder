n,m=map(int,input().split())
n=14 if n==1 else n
m=14 if m==1 else m
if n==m:
    print("Draw",end='\n')
elif n>m:
    print("Alice",end='\n')
else:
    print("Bob",end='\n')