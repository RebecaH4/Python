acu = 0
while True: #se ejecutara al menos una vez
    n1 = (input("teclea un numero: o presione x para salir del programa "))
    if(n1=="x"):
        break #rompe el ciclo
    else:
        acu = acu+int(n1) #toma n1 como entero
#fuera del ciclo
if (acu>0):
    print("El resultado final del acumulador es-----> ", acu)
else:
    print("Se pulso x para salir del bucle")