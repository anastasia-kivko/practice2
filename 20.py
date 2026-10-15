s = input()
x = ord(s[0]) - ord('a') + 1
y = int(s[1])
if (x + y) % 2 == 0:
    print("черный")
else:
    print("белый")