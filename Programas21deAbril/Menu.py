print("Seleccione una operacion: \na: Suma \nb: Resta\nc: Division \nd: multiplicacion\ne: Datos \nf: multiplicacion de la clase \ng: salir \n0:Comapar dos numeros")

x=input("Opcion: ")
if x == 'a' :
    print("Suma")
    num1=int(input("Dame un numero: "))
    num2=int(input("Dame otro numero: "))
    resultado=num1+num2
    print("El resultado es:",resultado)
    input("........"),
elif x == 'b' :
    print("Resta")
    num1=int(input("Dame un numero: "))
    num2=int(input("Dame otro numero: "))
    resultado=num1-num2
    print("El resultado es:",resultado)
    input("........"),
elif x == 'c' :
    print("Division")
    num1=int(input("Dame un numero: "))
    num2=int(input("Dame otro numero: "))
    resultado=num1/num2
    print("El resultado es:",resultado)
    input("........"),
elif x == 'd' :
    print("Multiplicacion")
    num1=int(input("Dame un numero: "))
    num2=int(input("Dame otro numero: "))
    resultado=num1+num2
    print("El resultado es:",resultado)
    input("........"),
elif x == 'e' :
    print("Datos del Usuario")
    nom=input("Nombre: ")
    edad=int(input("Edad: "))
    peso=int(input("Peso: "))
    print(nom,edad,peso)
    input("........"),
elif x == 'f' :
    print("Tablas de multiplicar")
    numero=int(input("De que tabla sera?:"))
    vecez=int(input("Cuantas tablas?:"))
    for x in range (0,vecez):
        print(numero,"*",x+1,"=",numero*(x+1))

    input("....")
elif x == 'g' :
    print("Saliendo")
    input("........"),
elif x == '0' :
    print("Son los numeros iguales?")
    num1=float(input("Dame un numero: "))
    num2=float(input("Dame otro numero: "))
    if num1 == num2:
        print("Los numeros son iguales.")
    elif num1 < num2:
        print(num1," Es menor")
    elif num1 > num2:
        print(num1," Es mayor")
    else:
        print("Como le hiciste para cagarla tanto?")
    input("........"),
else:
    print("Opcion invalida")
    input("...........")
