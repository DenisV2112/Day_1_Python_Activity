# Actividad 8
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
if (imc < 18.5):{print ("Bajo peso")}
elif 18.5 <= imc <= 24.9:{ print ("Peso normal")}
elif 25 <= imc <= 29.9:{ print ("Sobrepeso")}
else :{ print ("Obesidad")}