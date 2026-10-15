pin = input()
if len(pin) != 4:
    print("ERROR")
elif len(set(pin)) != 4:
    print("ERROR")
elif 1900 <= int(pin) <= 2050:
    print("ERROR")
else:
    print("OK")
