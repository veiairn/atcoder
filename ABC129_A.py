intList = list(map(int, input().split()))
intList.sort(key=int)
print(intList[0]+intList[1],end='\n')