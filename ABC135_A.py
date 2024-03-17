n,m=map(int,input().split())
sum=n+m
print(int((sum)//2) if sum%2==0 else "IMPOSSIBLE")