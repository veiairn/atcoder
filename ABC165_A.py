K=int(input())
n,m=map(int,input().split())
flg=False
for i in range(n,m+1):
    if i%K==0:
        flg=True
        break
print("OK" if flg else "NG")