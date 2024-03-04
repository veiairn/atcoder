n,m=map(int,input().split())
div=m//n
print(div if m%n==0 else div+1)