n,m=map(int,input().split())
print('16:9' if n%16==0 and m%9==0 else '4:3')