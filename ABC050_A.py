a,op,b=map(str,input().split())
a=int(a)
b=int(b)
match op:
    case '+':
        print(a+b,end='\n')
    case '-':
        print(a-b,end='\n')