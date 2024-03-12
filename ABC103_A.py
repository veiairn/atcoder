intList = list(map(int, input().split()))
intList.sort(key=int,reverse=True)
sum=0
for i in range(1,len(intList)):
    sum+=intList[i-1]-intList[i]
print(sum,end='\n')