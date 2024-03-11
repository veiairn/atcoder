D = {
    1: "A", 3: "A", 5: "A", 7: "A", 8: "A", 10: "A", 12: "A",
    4: "B", 6: "B", 9: "B", 11: "B",
    2: "C"
}
n,m=map(int,input().split())
print("Yes" if D.get(n)==D.get(m) else 'No')