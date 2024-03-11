n,m,p=map(int,input().split())
print('A' if abs(n-m)<abs(n-p) else 'B')