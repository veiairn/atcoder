s=input()
sum=0
for i in range(len(s)):
    match s[i]:
        case '+': 
            sum+=1
        case '-': 
            sum-=1
print(sum,end='\n')