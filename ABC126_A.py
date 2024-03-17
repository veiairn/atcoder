n,m=map(int,input().split())
s=input()

def join_strings(L):
    L = [str(l) for l in L]
    s = ''.join(L)
    return s

L = []
for i in range(n):
    if i==m-1:
        low=s.lower()
        L.append(low[i])
    else:
        L.append(s[i])

result = join_strings(L)
print(result)