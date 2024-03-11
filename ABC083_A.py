n,m,p,o=map(int,input().split())
L=n+m
R=p+o
print("Balanced" if L==R else "Left" if L>R else "Right")