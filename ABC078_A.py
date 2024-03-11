L = ["A", "B", "C", "D", "E", "F"]
D = {}
for i, name in enumerate(L, 1):
    D[name] = i

n, m = map(str, input().split())
print('>' if D.get(n) > D.get(m) else '<' if D.get(n) < D.get(m) else '=')