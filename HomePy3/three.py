masa = float(input("Введи масу в тоннах: "))

ton = int(masa)
kg = (masa - ton) * 1000
kilog = int(kg)
gram = round((kg - kilog)*1000) 
print(f"{ton}ton {kilog} kg {gram} gram")
