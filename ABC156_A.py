n,m=map(int,input().split())
print(m+(100*(10-n)) if n<10 else m)