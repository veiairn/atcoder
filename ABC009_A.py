from decimal import Decimal,ROUND_HALF_UP
n=int(input())
a = int(Decimal(str(n/2)).quantize(Decimal('1'),rounding=ROUND_HALF_UP))
print(a,end='\n')