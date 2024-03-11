n,m=map(str,input().split())
match n:
    case 'H':
        n=int(1)
    case 'D':
        n=int(0)
match m:
    case 'H':
        m=int(1)
    case 'D':
        m=int(0)
res=n|m
match res:
    case 1:
        res="H"
    case 0:
        res="D"
print(res,end='\n')