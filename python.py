#Georgina Alessabdra Corona Velázquez
#A01702762
#Calculadora de Indice de Masa Corporal(peso, edad, altura y genero)    
from colorama import *
#Importe como biblioteca externa colorama
print("""Elige una opcion:
1. Calcular tu imc
2. Ingresa los datos de tus ultimos 4 meses de consultas
""")
opcion=int(input())

if opcion==1:
    mujer="mujer"
    hombre="hombre"
    nombre = ''
    while not nombre:
        init();
        nombre=input(Back.BLACK + Fore.CYAN + "Escribe tu" + Back.YELLOW + Fore.BLACK + Style.BRIGHT + "nombre: ")
        #Aguegue elementos de colorama al programa, como estilo con Style. , color con Fore. y fondo en los texto con Back. para resaltar lo que te pedia y darle estetica. 

    edad= ''
    while not edad:
        edad=input(Back.BLACK + Fore.CYAN + Style.DIM + "¿Cuantos" + Back.YELLOW + Fore.BLACK + Style.BRIGHT + " años" + Back.BLACK + Fore.CYAN + Style.DIM + " tienes?")
        #Agregue en formato diferente en cada linea de texto debido a que si la aplicas desde arriba tela aplica a todo el texto
    estaturacmstr=float()
    while not estaturacmstr:
        estaturacmstr=input(Back.BLACK + Fore.CYAN + Style.DIM + "¿Cual es tu" + Back.YELLOW + Fore.BLACK + Style.BRIGHT + "estatura en cm?")
    int_estaturacm = int(estaturacmstr)
    pesostr=float()
    while not pesostr:
        pesostr=input(Back.BLACK + Fore.CYAN + Style.DIM + "¿Cual es tu" + Back.YELLOW + Fore.BLACK + Style.BRIGHT + " peso en kg?")
    int_peso = int(pesostr)
    genero=''
    while not genero:
        genero=input(Back.BLACK + Fore.CYAN + Style.DIM + "¿Eres" + Back.YELLOW + Fore.BLACK + Style.BRIGHT + " hombre o mujer?")
    def estaturaenm(a):
        return a/100
    estaturam = estaturaenm(int_estaturacm)
    def imc(a,b):
        return a/b**2
    final = imc(int_peso,estaturam)

    print(Back.MAGENTA + Fore.YELLOW + "Tu peso es de ", pesostr,"kg")
    print("Tu estatura es de ", estaturam,"m")
    print("Te identificas como ", genero)
    print("por lo tanto, ")
    print("Tu IMC es de: ", final)

    if genero==mujer:
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
        elif(18.49<final<=23.99):
            print("Tu IMC muestra un peso normal")
            print("Sugerencia: Ejercitese y tenga una dieta equilibrada")
        elif(23.99<final<=28.99):
            print("Tu IMC muestra sobrepeso")
            print("Sugerencia: Ejercitese, consulte a su medico y tenga una dieta equilibrada")
        elif(28.99<final<=37):
            print("Tu IMC muestra obesidad")
            print("Sugerencia: Consulte a su medico")
        else:
            print("Verifica otra vez, parece haber un error")
    elif genero==hombre:
        if(0<final<10):
            print("Algo anda mal")
            print("sugerencia: Revisa nuevamente los datos ingresados")
        elif(10<final<=20):
            print("Tu IMC muestra delgadez severa")
            print("sugerencia: consulte a su médico")
        elif(20<final<=21):
            print("Tu IMC muestra delgadez moderada")
            print("Sugerencia: Mantenga una dieta equilibrada")
        elif(21<final<=22.49):
            print("Tu IMC muestra delgadez aceptable")
            print("Sugerencia: Mantenga una dieta equilibrada")
        elif(22.49<final<=24.99):
            print("Tu IMC muestra un peso normal")
            print("Sugerencia: Ejercitese y tenga una dieta equilibrada")
        elif(24.99<final<=29.99):
            print("Tu IMC muestra sobrepeso")
            print("Sugerencia: Ejercitese, consulte a su medico y tenga una dieta equilibrada")
        elif(29.99<final<=40):
            print("Tu IMC muestra obesidad")
            print("Sugerencia: Consulte a su medico")
        else:
            print("Verifica otra vez, parece haber un error")
    else:
        genero=input("Verfique de nuevo si se identifica como hombre o como mujer de manera biologica, si es no binario favor de seleccionar el que considere su medico: ")

if opcion==2:
    matriz=[["","mes 1",0],["","mes 2",""],["","mes 3",""],["","mes 4",""]]
 
    def m(mat,col):
        i=0
        for linea in mat:
            j=0
            for col in linea:
                print("Cual fue tu peso?")
                peso1=int(input())
                mat[i][j]=peso1
            i=i+1
    res=m(matriz,0)
    def perdido(mat,col):
        i=0
        for linea in mat:
            j=2
            for col in linea:
                mat[i][j]=mat[i][0]-mat[i-1][0]
            i=i+1
    per=perdido(matriz,0)
    print(matriz)
