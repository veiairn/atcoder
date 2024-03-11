intList = list(map(int, input().split()))
set_l=list(set(intList))
print(set_l[0] if intList.count(set_l[0])==1 else set_l[1])
