#Rebe HC
#Llamar la fecha de la computadora
import datetime
import os
fecha = datetime.datetime.now()
año = datetime.datetime.strftime(fecha, "%Y")
d1 = {"Ing Indistrial", "Tic's", "Ing Sistemas", "Ing Quimica", "Ing Civil", "Ing Mecatronica", "Ing Electrica", "Ing Logistica", "Lic Administracion"}
p="error"
while p=="error":
    print("Selecciona una opcion ")
    print("1. Provienes de otra escuela")
    print("2. Hiciste examen de admision en el tec o pase por promedio")
    x = int(input(""))
    match x:
        case 1:
            print("Selecciona tu carrera")
            c=1
            for i in d1:
                print(c, ".", i)
                c+=1    
            y = int(input(""))
            if y<1 or y>9:
                    print("Error")
            else:
                g = int(input("Ingresa tu numero de alumno "))
                no = (str(año)+str(x)+str(y)+str(g))
                r = len(no)
                t=1
                if g>999 or g<1:
                    print("El numero es incorrecto")
                else:    
                    for d in range(1,t+1):
                        if r==9:
                            print("Tu numero de control es ")
                            print(str(año)+str(x)+str(y)+str(g))

                        if r==8:
                            print("Tu numero de control es ")
                            print(str(año)+str(x)+str(y)+ "0"+ str(g)) 

                        if r==7:
                            print("Tu numero de control es ")
                            print(str(año)+str(x)+str(y)+ "00"+ str(g)) 
        case 2:
            print("Selecciona tu carrera")
            w=1
            for i in d1:
                print(w, ".", i)
                w+=1
            s = int(input(""))
            if s<1 or s>9:
                print("Error")
            else:
                h = int(input("Ingresa tu numero de alumno "))
                nu = (str(año)+str(x)+str(s)+str(h))
                u = len(nu)
                j=1
                if h>999 or h<1:
                    print("El numero es incorrecto")
                else:
                    for d in range(1,j+1):
                        if u==9:
                            print("Tu numero de control es ")
                            print(str(año)+str(x)+str(s)+ str(h)) 

                        if u==8:
                            print("Tu numero de control es ")
                            print(str(año)+str(x)+str(s)+ "0"+ str(h)) 

                        if u==7:
                            print("Tu numero de control es ")
                            print(str(año)+str(x)+str(s)+ "00"+ str(h))
        case _:
            os.system("cls")
            print("Operacion invalida")
            p="error"

