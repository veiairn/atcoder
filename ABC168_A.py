s = input()
match s[-1]:
    case '2' | '4' | '5' | '7' | '9':
        print("hon",end='\n')
    case '0' | '1' | '6' | '8': 
        print("pon",end='\n')
    case '0' | '3':
        print("bon",end='\n')