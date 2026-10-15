s = input()
a, b = s.split(":")
a = int(a)
b = int(b)
if a > b:
    print(1)
elif b > a:
    print(2)
else:
    print(0)