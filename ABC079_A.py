s=input()
a=list(set(s[1:]))
b=list(set(s[:-1]))
print("Yes" if len(a)==1 or len(b)==1 else "No")