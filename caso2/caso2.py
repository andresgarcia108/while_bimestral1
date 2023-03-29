c = int(input("Digite el capital: "))

interes = 0
mes = 0
c2 = c + c

while c < c2:
    interes = c*0.05
    c = c+interes
    mes = mes + 1
print("El capital se duplica en " +str(mes)+ " meses")
