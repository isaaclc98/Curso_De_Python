print("Seleccione una operacion: \na: Area cuadrado \nb: Area Triangulo")
x=input("Opcion: ")
if x == 'a' :
    print("Calculadora area cuadrado")
    baseC=int(input("Dame la base: "))
    alturaC=int(input("Dame la altura: "))
    area=baseC*alturaC
    print("El area es:",area)
    input("........"),
elif x == 'b' :
    print("Calculadora area triangulo")
    baseT=float(input("Dame la base: "))
    alturaT=float(input("Dame la altura: "))
    areaT=(baseT*alturaT)/2
    print("El area del triangulo es:",areaT)
    input("........"),
else :
    print(x,"No es una operacion valida")
    input(".............")

# or = || and= && not= !
