A,B,C,D=map(int,input().split())

if B*C == A*D:
    print("DRAW",end='\n')
elif B*C < A*D:
    print("AOKI",end='\n')
else:
    print("TAKAHASHI",end='\n')