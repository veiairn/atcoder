def join_strings(L):
    L = [str(l) for l in L]
    s = ''.join(L)
    return s

L = [input(), "s"]
result = join_strings(L)
print(result)