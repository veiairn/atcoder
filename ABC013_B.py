l1=(0,1,2,3,4,5,6,7,8,9)
l2=(5,6,7,8,9,0,1,2,3,4)
n=int(input())
m=int(input())
dist1=abs(l1[n]-l1[m])
if dist1>5:
    dist1=abs(l2[n]-l2[m])

print(dist1,end='\n')