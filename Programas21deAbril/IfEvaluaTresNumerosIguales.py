#Hay que rervisarlo
print("¿Son los numeros iguales?")
num1=float(input("Dame un numero: "))
num2=float(input("Dame otro numero: "))
num3=float(input("Dame otro numero: "))
if num1 == num2 and num2 == num3:
    print("Los numeros son iguales.")
elif num1 <= num2 and num1 <= num3:
    print(num1," Es menor")
elif num1 >= num2 and num1 >= num3:
    print(num1," Es mayor")
elif num2 <= num1 and num2 <= num3:
    print(num3," Es menor")
elif num2 >= num1 and num2 >= num3:
        print(num3," Es mayor")
else:
    print("Como le hiciste para cagarla tanto?")
input("..........")
