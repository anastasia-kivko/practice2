s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
best = a
if b > best:
    best = b
if c > best:
    best = c
print(best)