A,B,C=map(int,input().split())
min=min(A,B)
max=max(A,B)
div=int(C//min)
if C%min < max:
    print(div,end='\n')
else:
    print(div+1,end='\n')