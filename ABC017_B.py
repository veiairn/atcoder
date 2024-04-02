s=input()
uniq_s=set(sorted(s))
msg="NO"
if 'ch' and 'o' and 'k' and 'u' in uniq_s:
    idx_c=s.index('c')
    idx_h=s.index('h')
    idx_o=s.index('o')
    idx_k=s.index('k')
    idx_u=s.index('u')
    if idx_c<idx_h<idx_o<idx_k<idx_u and idx_c==idx_h+1:
        msg="YES"

print(msg,end='\n')