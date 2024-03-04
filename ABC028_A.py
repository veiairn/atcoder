n=int(input())
if n <= 59:
    print("Bad",end='\n')
elif n >= 60 and n <= 89:
    print("Good",end='\n')
elif n >= 90 and n <= 99:
    print("Great",end='\n')
else:
    print("Perfect",end='\n')