n = int(input())
if n == 1:
    print(0)
else:
    n -= 1
    length = 1
    count = 9
    while n > count * length:
        n -= count * length
        length += 1
        count *= 10
    number = 10 ** (length - 1) + (n - 1) // length #само число
    position = (n - 1) % length
    print((number // 10 ** (length - 1 - position)) % 10)