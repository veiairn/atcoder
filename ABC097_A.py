a,b,c,d=map(int,input().split())
if (abs(a-b)<=d and abs(b-c)<=d) or abs(c-a)<=d:
    print("Yes",end='\n')
else:
    print("No",end='\n')