intList = list(map(int, input().split()))
intList.sort(key=int)
res=int((intList[0]*intList[1])//2)
print(res,end='\n')