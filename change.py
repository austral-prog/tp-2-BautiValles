def change():
    expense = 23.75
    money = 100
    Vuelto = money - expense
    Pesos = int(Vuelto)
    Centavos = round((Vuelto - Pesos) * 100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(Pesos)
    print("Centavos:")
    print( Centavos)
