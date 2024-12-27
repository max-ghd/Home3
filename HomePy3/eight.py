a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))

if a<b and a<c:
    print(f"Число 1 найменше, тому що має значення {a}")
elif b<a and b<c:
    print(f"Число 2 найменше, тому що має значення {b}")
elif c<b and c<a:
    print(f"Число 3 найменше, тому що має значення {c}")
else:
    print("Error")

