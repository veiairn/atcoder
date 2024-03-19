n,m=map(int,input().split())
min=min(n,m)
max=max(n,m)
print("Yes" if min+3>max else "No")