intList = list(map(int, input().split()))
set_s=list(set(intList))
cnt=len(set_s)
print("No" if cnt==1 or cnt==3 else "Yes")