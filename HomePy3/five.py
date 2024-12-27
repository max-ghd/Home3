film=float(input("Розмір фільму в гігабайтах: "))
inet=float(input("Швидкість Інтернет-з'єднання в секунду: "))
print(film)
print(inet)
# 1gb - 1000mb
#8.5mb sec
gb_v_mb = film * 1000
print(gb_v_mb)
time = round(gb_v_mb/inet, 2)
print(f"{time} секунд треба, щоб завантажити собі фільм")

