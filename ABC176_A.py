n,m,p=map(int,input().split())
x=int(n//m)
y=int(n//m+1)
print(x*p if n%m==0 else y*p)