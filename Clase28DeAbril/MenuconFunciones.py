def tablas(a,vez):
    print("Tablas de multiplicar")
    for x in range (0,vez):
        print(a,"*",x+1,"=",a*(x+1))
    return
def compara(num1,num2,num3):
    if num1 == num2 and num2 == num3:
        print("Los numeros son iguales.")
    elif num1 <= num2 and num1 <= num3:
        print(num1," Es menor que",num2,"y",num3)
    elif num1 >= num2 and num1 >= num3:
        print(num1," Es mayor que",num2,"y",num3)
    elif num2 <= num1 and num2 <= num3:
        print(num3," Es menor")
    elif num2 >= num1 and num2 >= num3:
        print(num3," Es mayor")
    else:
        print("Como le hiciste para cagarla tanto?")
    return
def suma(num1,num2):
    print("Suma")
    resultado=num1+num2
    print("El resultado es:",resultado)
    return
def iva():
    print("\n Calculadora de Iva")
    iva=float(input("Dame el iva: "));
    cantidad=float(input("Digita la cantidad: "));
    print("la cantidad es:",cantidad,"y el iva es:",iva*cantidad);


print("Seleccione una operacion: \n1: Suma \n2: Resta\n3: multiplicacion\n4: Division \n5: Comparacion de 3 numeros \n6: IVA \n7: Tablas de multiplicar \n8: Salir")
x=1
while x<9 and x>0:
    bandera = True
    while bandera:
        x=int(input("Elige una opcion: "))
        if x>0 and x<9:
            bandera = False
        else:
            print("Opcion equivocada")
    if x == 1:#suma
        a=int(input("Dame un numero: "))
        b=int(input("Dame otro numero"))
        suma(a,b)
    elif x==2:
        print("resta")
        a=int(input("Dame un numero: "))
        b=int(input("Dame otro numero"))
        resul=a-b
        print("El resultado es:",resul)
    elif x==3:
        print("Multiplicacion")
        a=int(input("Dame un numero: "))
        b=int(input("Dame otro numero"))
        resul=a*b
        print("El resultado es:",resul)
    elif x==4:
        print("Division")
        a=int(input("Dame un numero: "))
        b=int(input("Dame otro numero"))
        resul=a/b
        print("El resultado es:",resul)
    elif x==5:
        print("Comparando 3 numeros")
        num1=float(input("Dame un numero: "))
        num2=float(input("Dame otro numero: "))
        num3=float(input("Dame otro numero: "))
        compara(num1,num2,num3)
    elif x==6:
        print("IVA")
        iva()
    elif x==7:
        print("Tablas de multiplicar")
        a=int(input("De que numero: "))
        b=int(input("Limite: "))
        tablas(a,b)
    elif x==8:
        print("Saliendo...")
        x=9
input("Adios........")
