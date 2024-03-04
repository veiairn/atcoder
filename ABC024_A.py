A,B,C,K=map(int,input().split())
S,T=map(int,input().split())
sum=A*S+B*T
cnt=S+T
if cnt>=K:
    sum-=C*cnt
print(sum,end='\n')