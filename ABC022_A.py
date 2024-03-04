from itertools import accumulate
A=[]

N,S,T=map(int,input().split())

for i in range(N):
    A.append(int(input()))

cnt=0
for i in range(N):
    val=list(accumulate(A))[i]
    if val >= S and val <= T:
        cnt+=1

print(cnt,end='\n')