s=input()
end=s[-1]

l=[]
l.append(s)

def join_strings(L):
    L = [str(l) for l in L]
    s = ''.join(L)
    return s

if end=="s":
    l.append("es")
else:
    l.append("s")

result = join_strings(l)
print(result)