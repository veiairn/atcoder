strList = list(map(str, input().split()))
rev_list=strList[1]+strList[0]
def join_strings(L):
    L = [str(l) for l in L]
    s = ''.join(L)
    return s

result = join_strings(rev_list)
print(result)