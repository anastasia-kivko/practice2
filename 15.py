n, k, m = map(int, input().split())
d1 = abs(k - m)
d2 = n - d1
print(min(d1, d2))
