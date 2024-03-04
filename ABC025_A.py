abc=input()
n=int(input())

l=[]
for i in range(len(abc)):
    for j in range(len(abc)):
        l.append(abc[i]+abc[j])

print(l[n-1],end='\n')
