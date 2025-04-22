#Actividad 9
year = input("insert a year")
if (int(year) % 4 == 0 and int(year)% 100 != 0): print(f"{year} es un año bisiesto.")
elif  int(year) % 400 == 0:  print(f"{year} es un año bisiesto.")
else :  print(f"{year} es un año bisiesto.")