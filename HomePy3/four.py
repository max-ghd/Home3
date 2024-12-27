time= int(input("Time in second: "))
day = time //  86400
day1 = int(day)
print(day1)
hours = time // 3600
time = time % 3600
print(hours)
min = time // 60
print(min)
sec = time % 60
print(sec)

