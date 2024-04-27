n=int(input())
div=n//100
mod=n%100
print(div if mod==0 else div+1)