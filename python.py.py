#Georgina Alessabdra Corona Velázquez
#A01702762
#Calculadora de Indice de Masa Corporal(peso, edad, altura y genero)
edad=int(input("¿Cuantos años tienes?"))
estaturacm=float(input("¿Cual es tu estatura en cm?"))
peso=float(input("¿Cual es tu peso en kg?"))
genero=str(input("¿Eres hombre o mujer?"))

def estaturaenm(a):
    return a/100
estaturam = estaturaenm(estaturacm)

def imc(a,b):
    return a/b**2
final = imc(peso,estaturam)

print("Tu peso es de ", peso,"kg")
print("Tu estatura es de ", estaturam,"m")
print("Te identificas como ", genero)
print("por lo tanto: ")
print("Tu IMC es de: ", final)

if(0<final<10):
    print("Algo anda mal")
    print("sugerencia: Revisa nuevamente los datos ingresados")
elif(10<final<=16):
  print("Tu IMC muestra delgadez severa")
  print("sugerencia: consulte a su médico")
elif(16<final<=17):
  print("Tu IMC muestra delgadez moderada")
  print("Sugerencia: Mantenga una dieta equilibrada")
elif(17<final<=18.49):
  print("Tu IMC muestra delgadez aceptable")
  print("Sugerencia: Mantenga una dieta equilibrada")
elif(18.49<final<=24.99):
  print("Tu IMC muestra un peso normal")
  print("Sugerencia: Ejercitese y tenga una dieta equilibrada")
elif(24.99<final<=29.99):
  print("Tu IMC muestra sobrepeso")
  print("Sugerencia: Ejercitese, consulte a su medico y tenga una dieta equilibrada")
elif(29.99<final<=35):
  print("Tu IMC muestra obesidad")
  print("Sugerencia: Consulte a su medico")





    



