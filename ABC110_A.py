intList = list(map(int, input().split()))
intList.sort(key=int,reverse=True)
res=intList[0]*10+intList[1]+intList[2]
print(res,end='\n')