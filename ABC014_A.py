n=int(input())
m=int(input())
res=m-(n%m)
if res!=m:
    print(res,end='\n')
else:
    print(0,end='\n')