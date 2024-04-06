def append_str(s,head,end):
    s=head+s+end
    return s

n=int(input())
target=input()

def proc_str(n,target):
    s=""
    for i in range(0,n):
        if i==0:
            s="b"
        elif i%3==1:
            s=append_str(s,"a","c")
        elif i%3==2:
            s=append_str(s,"c","a")
        else:
            s=append_str(s,"b","b")
        if(s==target):
            return i
    return -1

print(proc_str(n,target),end='\n')