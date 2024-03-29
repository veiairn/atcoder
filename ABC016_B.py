a,b,c=map(int,input().split())
flg=0
if c==a+b:
    flg+=1;
if c==a-b:
    flg+=2;

match flg:
    case 0:
        print('!')
    case 1:
        print('+')
    case 2:
        print('-')
    case 3:
        print('?')