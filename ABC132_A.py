s=input()
set_s=list(set(s))
print("Yes" if len(set_s)==2 and s.count(set_s[0])==2  else "No")