n=int(input())
mod=n%1000
is_mod=mod==0
print(0 if is_mod else 1000-mod)