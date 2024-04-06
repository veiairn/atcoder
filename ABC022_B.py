n=int(input())
D = dict()

cnt=0
for i in range(n):
    k=int(input())
    if k in D.keys():
        cnt+=1
    else:
        D[k]=D.get(k,0)+1 
print(cnt,end='\n')