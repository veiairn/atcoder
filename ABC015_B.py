from decimal import Decimal,ROUND_CEILING
n=int(input())
intList = list(map(int, input().split()))
sum=0
cnt=0
for i in range(n):
    if intList[i]!=0:
        sum+=intList[i]
        cnt+=1
res=sum/cnt
a = Decimal(str(res)).quantize(Decimal('1'),rounding=ROUND_CEILING)
print(a,end='\n')
