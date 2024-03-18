strList = list(map(str, input().split()))
set_s=list(set(strList))
print("No" if len(set_s)==1 else "Yes")