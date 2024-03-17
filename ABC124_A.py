n,m=map(int,input().split())
max=max(n,m)
print(2*n if n==m else 2*max-1)