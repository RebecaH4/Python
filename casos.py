a = int(input("Ingresa el primer numero "))
b = int(input("Ingresa el segundo numero "))
print("{+} suma a+b")
print("{-} resta a-b")
print("{*} multi a+*b")
print("{/} division a/b")
simbolo = input("ingresa la operacion insertando el simbolo ")
match simbolo:
    case "+":
        print("el resultado ", (a+b))
    case "-":
        print("el resultado ", (a-b))
    case "*":
        print("el resultado ", (a*b))
    case "/":
        if b != 0:
            print("el resultado ", (a/b))
        else:
            print("No se puede dividir entre cero")
    case _:
        print("Operacion invalida")