s=input()
t=input()

res="You can win"

def check_atcoder(x, res):
    if x not in 'atcoder':
        res = "You will lose"
    return res

for i in range(len(s)):
    if s[i]!="@" and t[i]!="@" and s[i]!=t[i]:
        res="You will lose"
        break
    elif s[i]!="@" and t[i]=="@":
        res=check_atcoder(s[i],res)
        break
    elif s[i]=="@" and t[i]!="@":
        res=check_atcoder(t[i],res)
        break
print(res,end='\n')