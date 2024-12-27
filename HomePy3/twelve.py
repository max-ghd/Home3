number_trolejbus =(input("Введи шестизначний номер квитка тролейбуса: "))
suma_123 = int(number_trolejbus[0]) + int(number_trolejbus[1]) + int(number_trolejbus[2])
suma_456 = int(number_trolejbus[3]) + int(number_trolejbus[4]) + int(number_trolejbus[5])


if suma_123 == suma_456:
    print("Вітаю, це щасливий білет! Очікуй гарних новин)")
else:
    print("Шкода, пощастить наступного разу")

