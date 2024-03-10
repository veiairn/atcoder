intList = list(map(int, input().split()))
intList.sort(key=int)
if intList[0]+intList[1]==intList[2]:
    print("Yes",end='\n')
else:
    print("No",end='\n')