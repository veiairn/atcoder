from decimal import Decimal,ROUND_CEILING
n,m=map(int,input().split())
a = Decimal(str((n+m)/2)).quantize(Decimal('1'),rounding=ROUND_CEILING)
print(int(a))