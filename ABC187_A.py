n,m=map(str,input().split())
sorted_n=sorted(n,reverse=True,key=int)
sorted_m=sorted(m,reverse=True,key=int)
join_n=''.join(sorted_n)
join_m=''.join(sorted_m)
max=max(join_n,join_m)
sum=0
for i in range(3):
    sum+=int(max[i])

print(sum,end='\n')
