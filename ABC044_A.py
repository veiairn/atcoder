N=int(input())
K=int(input())
X=int(input())
Y=int(input())

if N <= K:
	sum=N*X
else:
	sum = K*X + (N-K)*Y

print(sum,end='\n')