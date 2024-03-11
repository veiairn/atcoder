def join_strings(L):
    L = [str(l) for l in L]
    s = ''.join(L)
    return s

s=input()
t=input()
u=input()

L=[s[0],t[1],u[2]]

result = join_strings(L)
print(result)
    