from itertools import accumulate
A=[]

for i in range(3):
    n,m=map(int,input().split())
    A.append(int(n*m/10))

B = list(accumulate(A))
print(B[-1])