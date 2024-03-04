n=int(input())
half=n//2
if(n%2==0):
    print(int(half**2),end='\n')
else:
    print(int(half*(half+1)),end='\n')
