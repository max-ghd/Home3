corner_up=int(input("Введи координат верхнього лівого кута прямокутника: "))
corner_down=int(input("Введи координат нижнього правого кута прямокутника: "))
x = 7 
y = 5

if corner_up == y and corner_down == x:
    print("Точка належить цьому прямокутнику")
elif corner_up < y and corner_down < x:
    print("Точка не належить цьому прямокутнику")
elif corner_up > y and corner_down > x:
    print("Точка  належить  прямокутнику")
else:
    print("Error")
