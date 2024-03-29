n = int(input(""))
D = dict()

for _ in range(n):
    s=input()
    D[s]=D.get(s,0)+1

max_value=max(D.values())

for k,v in D.items():
    if v==max_value:
        print(k,end='\n')
        break;