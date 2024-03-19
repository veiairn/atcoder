s=input()
cnt=0
for i in range(2):
    if s[i]==s[i+1]=="R":
        cnt+=1

if cnt>0:
    print(cnt+1,end='\n')
elif cnt==0 and s.find("R")>=0:
    print(1,end='\n')
else:
    print(0,end='\n')