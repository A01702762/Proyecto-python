#Georgina Alessabdra Corona Velázquez
#A01702762
#Calculadora de Indice de Masa Corporal(peso, edad, altura y genero)



#Crear una función llamada imc que va a mandar llamar la estatura y el peso

print("¿Cuantos años tienes?")

edad=int(input())

print("¿Cual es tu estatura en cm?")

estaturacm=float(input())
estaturam=estaturacm/100
estaturasqrt=estaturam**2

print("¿Cual es tu peso en kg?")

peso=float(input())

print("¿Eres hombre o mujer?")

genero=str(input())


print("Tu peso es de ", peso,"kg")
print("Tu estatura es de ", estaturam,"m")
print("Te identificas como ", genero)
print("por lo tanto: ")

imc=peso/estaturasqrt

print("Tu IMC es de: ", imc)



if(24>=imc>18):
    
    print("Tu IMC es normal")
    print("sugerencia: haga ejercicio regularmente y alimentese sanamente")

elif(imc<18):
    
    print("Tu IMC es bajo")
    print("Sugerencia: consulte a su médico")
    

elif(imc>24):
    
    print("Tu IMC es alto")
    print("Sugerencia: consulte a su médico")






    



