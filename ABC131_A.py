s=input()
set_s=list(set(s))
if len(set_s)==1:
    print("Bad",end='\n')
elif len(set_s)==4:
    print("Good",end='\n')
elif len(set_s)==4:
    print("Good",end='\n')
else:
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            print("Bad",end='\n')
            break
        if i==len(s)-2:
            print("Good",end='\n')