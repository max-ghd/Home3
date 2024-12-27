suma =float(input("Write suma in grivnes: "))
m=int(input("Введіть термін вкладу в місяцях: "))
stav=float(input("Введіть процентну ставку за рік: "))

stav1= stav/100
suma_m = suma*stav1*m/12
print(f"{suma_m} сума процентового доходу через {m} місяців")