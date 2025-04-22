print("Hola mundo")
# Actividad 1
age = input ("Insert your age: ")
if ( int(age) <= 18): {print("eres menor de edad")} 
elif ( int(age) >= 18): {print("eres mayor de edad")}
#Actividad 2
positive_negative_number = input("Insert a number")
if(int(positive_negative_number) < 0) : {print("the number is negative")}
elif(int(positive_negative_number) > 0) : {print("the number is Positive")}
else : {print("the number is 0")}
#Actividad 3
par_impar_number = input("Insert a Number")
if(int(par_impar_number)% 2 == int(par_impar_number) - int(par_impar_number)): print("es par")
else : print("es impar")
#Actividad 4
password = input("Insert your pastword")
acess_password = "python123"
if(password == acess_password): {print("Correct")}
else : {print("incorrect")}
#Actividad 5 
tips = input("Inserta valor de la cuenta")
porcent = input("Que porcentaje quieres dar? ")
print(f"{int(tips) * int(porcent) / 100}")
#Actividad 6
secret_number = 7
your_numebr = int (input("Adivina un numero del 1 al 10"))
if(secret_number == your_numebr ) :{ print("Adivinaste")}
elif(secret_number < your_numebr):{print("Es mayor")}
elif(secret_number > your_numebr) : {print("Es menor")}
#Actividad 7
number1 = input("Ingresa un numero")
number2 = input("ingresa otro numero")
if number1 < number2 : print(f"{number2} es mayor a {number1}")
elif number1 > number2 : print(f"{number2} es menor a {number1}")
else : print('los numeros son iguales')
# Actividad 8
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
if (imc < 18.5):{print ("Bajo peso")}
elif 18.5 <= imc <= 24.9:{ print ("Peso normal")}
elif 25 <= imc <= 29.9:{ print ("Sobrepeso")}
else :{ print ("Obesidad")}
#Actividad 9
year = input("insert a year")
if (int(year) % 4 == 0 and int(year)% 100 != 0): print(f"{year} es un año bisiesto.")
elif  int(year) % 400 == 0:  print(f"{year} es un año bisiesto.")
else :  print(f"{year} es un año bisiesto.")
#Actividad 10
range_number = input("Inserta un numero")
if 1 <= int(range_number)  : print("Esta en el rango del 1 al 10")
elif int(range_number)  <= 10  : print("Esta en el rango del 1 al 10")
else :  print("No esta")
