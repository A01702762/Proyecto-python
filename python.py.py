#Georgina Alessabdra Corona Velázquez
#A01702762
#Calculadora de Indice de Masa Corporal(peso, edad, altura y genero)



#Crear una función llamada imc que va a mandar llamar la estatura y el peso

print("¿Cuantos años tienes?")

edad=int(input())

print("¿Cual es tu estatura en cm?")

estaturacm=float(input())
estaturam=estaturacm/100

print("¿Cual es tu peso en kg?")

peso=float(input())

print("¿Eres hombre o mujer?")

genero=str(input())

def imc(a,b):
  return a/b**2
 
final = imc(peso,estaturam)

print("Tu peso es de ", peso,"kg")
print("Tu estatura es de ", estaturam,"m")
print("Te identificas como ", genero)
print("por lo tanto: ")


print("Tu IMC es de: ", final)



if(24>=final>18):
    
    print("Tu IMC es normal")
    print("sugerencia: haga ejercicio regularmente y alimentese sanamente")

elif(final<18):
    
    print("Tu IMC es bajo")
    print("Sugerencia: consulte a su médico")
    

elif(final >= 25 and final <30):
    
    print("Tu IMC es alto")
    print("Sugerencia: consulte a su médico")

elif(final >= 30):
    print("Tu IMC muestra sobrepeso")
    print("Sugerencia: Su salud peligra")




    



