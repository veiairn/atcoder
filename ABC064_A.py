strList = list(map(str, input().split()))
def join_strings(L):
    L = [str(l) for l in L]
    s = ''.join(L)
    return s

num = int(join_strings(strList))
print('YES' if num%4==0 else 'NO')