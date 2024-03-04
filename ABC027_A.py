import collections

s = input().split(" ")
L = [int(x) for x in s[:3]]

c = collections.Counter(L)

for length, count in c.items():
    if count == 1 or count == 3:
        print(length)
        break