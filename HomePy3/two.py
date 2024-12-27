grivna =float(input("Введи суму в гривнях: "))

num1 = int(grivna)
num2 = round((grivna - num1) * 100)

print(f"Your suma: {num1} гривень {num2}  кпійок")