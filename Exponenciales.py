#Rebe HC
x = int(input("Ingresa un numero "))
i = 0
m = 0
d = 0
for i in range(1, x+1):
    m = (i**i)*i
    print(f"{i}  ^   {i+1}  =  {m}")
    d+=m

print(f"{d} / {x} = {d/x}")
    
    
