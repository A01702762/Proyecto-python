"""
Proyecto control de peso
El programa tiene 2 opciones,
calcular tu imc al darle ciertos datos o
registrar tu peso en tus meses de consulta.
Al final te lanza el peso perdido o ganado
en cada mes o tu imc considerando tu sexo,
estatura y peso
"""
#bibliotecas
from colorama import *
"""
(uso de biblioteca de python extra)
Se importa una biblioteca externa que
muestra el texto con diferentes 
fondos y colores
"""
"""
================== funciones de preguntas  =====================================
"""
"""
Se crean diferentes funciones que
se usaran a lo largo del programa
"""

def estaturaencm_a_estaturaenm(float_estaturacm):
     """
    (uso de operadores, uso de funciones)
    recibe: float_estaturacm valor numérico, 
    divide entre 100
    devuelve: la estatura en metros
    """
     return float_estaturacm/100

def calculo_imc(a,b):
    '''
    (uso de operadores, uso de funciones)
    recibe: float_peso y estaturaenm valor numérico,
    multiplica el peso por la estatura al cuadrado
    devuelve: el indice de masa corporal
    '''
    return a/b**2
"""
================== funciones auxiliares  =======================================
"""
def imc_basado_en_genero(genero,final):
    '''
    (uso de condicionales, condicionales anidadas,
    parametros y estandares)
    recibe: genero, cadena de texto, y final,
    un dato númerico
    devuelve: sugerencias y comentarios
    basado en tu genero e imc  
    '''
    '''
    Empieza un primer condicional separando
    por género, si genero=="mujer", se ejecuta
    el primer bloque
    '''
    if genero=="mujer":
        '''
        Entra al siguiente bloque de condicionales
        una vez que cumple con el primer condicional,
        ahora este se separa de acuerdo al imc
        '''
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
            print('''Sugerencia: Ejercitese, consulte a su medico y
                    tenga una dieta equilibrada''')
        elif(28.99<final<=37):
            print("Tu IMC muestra obesidad")
            print("Sugerencia: Consulte a su medico")
        else:
            print("Verifica otra vez, parece haber un error")
            
    elif genero=="hombre":
        '''
        Entra al siguiente bloque de condicionales
        una vez que cumple con el segundo condicional,
        ahora este se separa de acuerdo al imc de hombre
        '''
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
            print('''Sugerencia: Ejercitese, consulte a su medico y
                    tenga una dieta equilibrada''')
        elif(29.99<final<=40):
            print("Tu IMC muestra obesidad")
            print("Sugerencia: Consulte a su medico")
        else:
            print("Verifica otra vez, parece haber un error")
    else:
        genero=input('''Verfique de nuevo si se identifica como hombre o
                    como mujer de manera biologica,si es no binario favor de
                    seleccionar el que considere su medico: ''')

def registrar_pesos_de_consulta():
    '''
    (uso de matrices, listas y ciclo for)
    no recibe nada debido a que todo se realiza
    en la misma funcion
    devuelve: una matriz de ix3, siendo i el valor que el usuario lanza
    con peso en posicion 0,
    mes en posicion 1 y perdida en posicion 2.
    Al final imprime los datos de las diferentes
    listas
    '''
    matriz=[]
    long=int(input("Cuantos meses quieres registrar?"))
    
    contador=1
    for i in range(0,long):
        datos=[]
        peso=float(input("Cuanto pesaste?"))
        mes="mes "+str(contador)
        if i==0:
            diferencia=0
        else:
            diferencia=(matriz[i-1][0]-peso)*-1
            
        datos.append(peso)
        datos.append(mes)
        datos.append(diferencia)
        
        matriz.append(datos)
        contador=contador+1

    for i in range(0,len(matriz)):
        print("En el "+str(matriz[i][1])+" pesaste "
              +str(matriz[i][0])+" y perdiste/ganaste "
              +str(matriz[i][2]))
'''
------------------------------------------menú------------------------------------------
'''
print("""Elige una opcion:
1. Calcular tu imc
2. Ingresa los datos de tus meses en consultas
""")
opcion=int(input())
'''
En este ciclo se declaran las variables para calcular
el imc. Lo que se hace es que al no asignarle
un valor a las variables, se sigue solicitando que
el usuario asigne un valor hasta que lo declara
'''
if opcion==1:
    '''
------------------------------------variables-----------------------------------------------
    '''    
    nombre = ''
    while not nombre:
        nombre=input(Back.BLACK + Fore.CYAN + "Escribe tu"
                     + Back.YELLOW + Fore.BLACK + Style.BRIGHT + "nombre: ")
        '''
        Aguegue elementos de colorama al programa, como estilo con Style./
        , color con Fore. y fondo en los texto con Back. para resaltar lo que/
        te pedia y darle estetica.
        '''   
    edad= ''
    while not edad:
        edad=input(Back.BLACK + Fore.CYAN + Style.DIM + "¿Cuantos"
                   + Back.YELLOW + Fore.BLACK + Style.BRIGHT + " años"
                   + Back.BLACK + Fore.CYAN + Style.DIM + " tienes?")
    
    estaturacmstr=''
    while not estaturacmstr:
        estaturacmstr=input(Back.BLACK + Fore.CYAN + Style.DIM + "¿Cual es tu"
                            + Back.YELLOW + Fore.BLACK + Style.BRIGHT
                            + "estatura en cm?")
    float_estaturacm = float(estaturacmstr)

    pesostr=''
    while not pesostr:
        pesostr=input(Back.BLACK + Fore.CYAN + Style.DIM + "¿Cual es tu"
                      + Back.YELLOW + Fore.BLACK + Style.BRIGHT
                      + " peso en kg?")
    float_peso = float(pesostr)

    genero=''
    while not genero:
        genero=input(Back.BLACK + Fore.CYAN + Style.DIM + "¿Eres"
                     + Back.YELLOW + Fore.BLACK + Style.BRIGHT
                     + " hombre o mujer?")
    '''
    Aqui mandamos llamar 2 funciones y
    las declaramos en 2 funciones
    '''
    estaturaenm=estaturaencm_a_estaturaenm(float_estaturacm)
    final=calculo_imc(float_peso,estaturaenm)
    '''
    Aqui imprimimos todo lo que desplega la
    opcion 1, todo lo relacionado con el imc,
    sugerencias y con elementos de colorama
    '''
    print(Back.MAGENTA + Fore.YELLOW
      + "Tu peso es de " + pesostr,"kg")
    print("Tu estatura es de ", estaturaencm_a_estaturaenm(float_estaturacm),"m")
    print("Te identificas como ", genero)
    print("por lo tanto, ")
    print("Tu IMC es de: ", final)
    print(imc_basado_en_genero(genero,final))

elif opcion==2:
    '''
    mandamos llamar una funcion para registrar el peso
    de consultas en esta funcion
    '''
    registrar_pesos_de_consulta()
    
else:
    print("opcion no valida")
