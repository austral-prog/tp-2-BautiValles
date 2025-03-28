def change():
    expense = 23.75
    money = 100
    Vuelto = money - expense
    Pesos = int(Vuelto)
    Centavos = round((Vuelto - Pesos) * 100)
    print("ingresar el gasto: ")
    print(expense)
    print("dinero recibido: ")
    print(money)
    print("\n")
    print("Vuelto: ")
    print("\n")
    print("Pesos: ")
    print(Pesos)
    print("Centavos: ")
    print( Centavos)
