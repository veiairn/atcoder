import collections

input_list = list(map(int, input().split()))

if input_list.count(5)==2 and input_list.count(7)==1:
    print("YES")
else:
    print("NO")