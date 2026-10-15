a, b = map(float, input().split('x'))
r_arena = 6.5
diag = (a ** 2 + b ** 2) ** 0.5
if diag <= r_arena*2:
    print("да")
else:
    print("нет")
