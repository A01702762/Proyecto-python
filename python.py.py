#Georgina Alessabdra Corona Velázquez
#A01702762
#Calculadora de Indice de Masa Corporal(peso, edad, altura y genero)    
print("""Elige una opcion:
1. Calcular tu imc
2. Ingresa los datos de tus ultimos 4 meses de consultas
""")
opcion=int(input())

if opcion==1:
    nombre = ''
    while not nombre:
        nombre=input('Escribe tu nombre: ')
    edad= ''
    while not edad:
        edad=input("¿Cuantos años tienes?")
    estaturacmstr=float()
    while not estaturacmstr:
        estaturacmstr=input("¿Cual es tu estatura en cm?")
    int_estaturacm = int(estaturacmstr)
    pesostr=float()
    while not pesostr:
        pesostr=input("¿Cual es tu peso en kg?")
    int_peso = int(pesostr)
    genero=''
    while not genero:
        genero=input("¿Eres hombre o mujer?")
    def estaturaenm(a):
        return a/100
    estaturam = estaturaenm(int_estaturacm)
    def imc(a,b):
        return a/b**2
    final = imc(int_peso,estaturam)

    print("Tu peso es de ", pesostr,"kg")
    print("Tu estatura es de ", estaturam,"m")
    print("Te identificas como ", genero)
    print("por lo tanto, ")
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
    else:
        print("Verifica otra vez, parece haber un error")

if opcion==2:
    matriz=[["","mes 1",""],["","mes 2",""],["","mes 3",""],["","mes 4",""]]
 
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
                mat[i][j]=mat[i][j-2]-mat[i-1][j-2]
            i=i+1
    per=perdido(matriz,0)
    print(matriz)

#me falta corregir que no se vaya revisando uno por uno, debido a que tienes que ingresar el dato 12 veces por los 12 lugares para que te lleve al siguiete paso
