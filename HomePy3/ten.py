a = input("Ціле число ")

if 4 == len(a):
    print("Число має 4 розряда")
elif len(a)==3:
    print("Число маж 3 розряда")
elif len(a)==2:
    print("Число має 2 розряда")
elif len(a)==1:
    print("Число має 1 розряд")
else:
    print("Помилка, більше 4 розрядів")
