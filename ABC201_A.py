intList = list(map(int, input().split()))
intList.sort(key=int)
print("Yes" if intList[2]-intList[1]==intList[1]-intList[0] else "No")