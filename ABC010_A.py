def join_strings(L):
    L = [str(l) for l in L]
    s = ''.join(L)
    return s

s=input()
L = [s, "pp"]
result = join_strings(L)
print(result)