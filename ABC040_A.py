len,idx=map(int,input().split())
l=[]

for i in range(len):
    if i != idx:
        l.append(0)
    else:
        l.append(1)

