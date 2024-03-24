n=int(input())
V=n/100
if n<100:
    V=0
elif 100<=n<=5000:
    V=V
elif 6000<=n<=30000:
    V/=10
    V+=50
elif 35000<=n<=70000:
    V=(V/10-30)/5+80
elif 70000<n:
    V=89

print('{:0>2}'.format(int(V)))