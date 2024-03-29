s=input()
if s=="":
    print("YES",end='\n')
else:
    if "choku" in s:
        if s.endswith("ch") or s.endswith("o") or s.endswith("k") or s.endswith("u"):
            print("YES",end='\n')
        else:
            print("No",end='\n')
    else:
        print("No",end='\n')