s=input()
p=int(input())

def join_strings(L):
    L = [str(l) for l in L]
    s = ''.join(L)
    return s

def reverse_str(s,n,m):
    head=s[:n-1]
    res=s[n-1:m]
    rev=res[::-1]
    end=s[m:]

    L = head,rev,end
    result = join_strings(L)
    return result

for i in range(p):
    n,m=map(int,input().split())
    s=reverse_str(s,n,m)

print(s,end='\n')