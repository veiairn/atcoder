HW=[]
for i in range(4):
    strList = list(map(str, input().split()))
    HW.append(strList)

for i in range(3,-1,-1):
    print(" ".join(HW[i][::-1]),end='\n')
