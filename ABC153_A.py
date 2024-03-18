n,m=map(int,input().split())
res=int(n//m)
print(res if n%m==0 else res+1)