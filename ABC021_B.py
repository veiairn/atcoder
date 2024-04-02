n=int(input())
a,b=map(int,input().split())
m=int(input())
intList = list(map(int, input().split()))

seen=[a,b]
flg=True

for i in range(len(intList)):
    if intList[i] in seen:
        flg=False
    else:
        seen.append(intList[i])

print("YES" if flg else "NO")