n=int(input())
h=n//3600
m=(n-h*3600)//60
s=n-(h*3600+m*60)
print('{:0>2}:{:0>2}:{:0>2}'.format(h, m, s))