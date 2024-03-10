from itertools import accumulate
A=[]
n=int(input())
for i in range(1,n+1):
    A.append(i)

B = list(accumulate(A))
print(B[-1],end='\n')