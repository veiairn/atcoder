n,m=map(int,input().split())
print(m if n>12 else m//2 if 5<n<=12 else 0)