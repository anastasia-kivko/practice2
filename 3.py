print("Вы поедете на бал?")
answer = input("Ответ: ").lower()
if not (answer == "да" or answer == "нет"):
    print("Верно")
else:
    print("Неверно")