nivel_agua = float(input("¿Cuál es el nivel del agua? : "))


# evaluando multiple condiciones

if nivel_agua > 0 and nivel_agua <= 200 :
    print(f"El nivel del agua es {nivel_agua} y está muy bajo")
elif(nivel_agua > 200 and nivel_agua <= 400):
    print(f"El nivel del agua es {nivel_agua}, estamos operando con normalidad")
elif nivel_agua > 400:
    print(f"El nivel del agua es {nivel_agua} inicie evacuación")
else:
    print(f"Por favor revise el sensor de agua")