# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:58:53 2022

@author: ronys
"""
#Librerias
from fractions import Fraction
import random
import time
import pandas as pd
import os
#Empieza menu
def main():
    nombre=input("Introduce tu nombre para iniciar: ")#Ingresemos nombre para iniciar
    while True:#Un bucle infinito, donde nada más se rompe hasta que diga el autor
        
        x=int(input("1.- Potencias\n2.- Suma de fracciones \n3.- Suma de matrices \n4.- Tictactoe\n5.- Excel \n6.- Salir\nIngrese su numero:"))
        #La viariable donde necesitas escoger que quieres hacer
        if x ==1:
            potencias(nombre)
        elif x==2:
            suma_fracciones(nombre)
        elif x==3:
            main_sumadematrices(nombre)
        elif x==4:
            juego_gato(nombre)
        elif x==5:
            archivo_excel()
        elif x==6:
            print('--------------------Gracias por jugar---------------------------')
            break
            #Aquí se rompe si lo quiere el usario
        else:
            print("Seleccione una opcion valida")
            #Si no esta dentro de los intervalos de 1 a 6

def suma_matrices(matriz1,matriz2):
    #Condicion para las matrices hechas random que tengan las mismas dimensiones
    if len(matriz1)==len(matriz2) and len(matriz2)==len(matriz1):
        mat3=[]#Crear nueva lista, donde guardar la suma de las dos matrices
        for i in range(len(matriz1)):
            mat3.append([])#Crear nueva matriz
            for j in range(len(matriz1[0])):
                mat3[i].append(matriz1[i][j]+matriz2[i][j])#Sumar cada renglon y cada columna de las dos matrices
            
        return mat3#retornar la matriz completa
def suma_us():
    renglones=2#Declarar cuantos renglones tiene la matriz
    columnas=3#Declarar cuantas comlumnas tiene la matriz
    matriz=[]#Crear la matriz
    for ren in range(renglones):#Por cada renglon adjuntar una lista
        lista=[]#Crear la lista
        for col in range(columnas):#Por cada columna adjuntar un dato
            dato=int(input("Ingrese resultado de la suma: "))#Declarar el dato
            lista.append(dato)#Agregar el dato en la lista
        matriz.append(lista)#Agregar la lista a la matriz
    return matriz#retornar la matriz completa     
def matriz_random():
    renglones=2#Declarar cuantos renglones tiene la matriz
    columnas=3#Declarar cuantas comlumnas tiene la matriz
    matriz=[]#Crear la matriz
    for ren in range(renglones):#Por cada renglon adjuntar una lista
        lista=[]#Crear la lista
        for col in range(columnas):#Por cada columana generar tres datos random
            dato=random.randint(1, 10)#dato random
            lista.append(dato)#Agregar el dato random en la lista
        matriz.append(lista)#Agregar la lista a la matriz
    return matriz#retornar la matriz completa
def main_sumadematrices(nombre):
    correcto=0#Puntuacion en cero
    incorrecto=0#Puntuacion en cero
    print('-----------------Bienvenido a suma de matrices ---------------------------')
    for a in range(10):#Hacer el bucle 10 veces
        matriz1=matriz_random()#Funcion de matriz random
        matriz2=matriz_random()#Funcion2 de matriz random
        matriz3=suma_matrices(matriz1,matriz2)#LLamar la funcion que tiene el resultado
        print(matriz1)#imprimir las matrices
        print(matriz2)#imprimir las matrices
        matriz4=suma_us()#Llamar la matriz donde vamos a poner nuestra respueta
        
        if matriz4==matriz3:#Si nuestra matriz es igual a la del resultado
            print("Es correcto", matriz4)
            correcto+=1#Contador mas1
            time.sleep(2)#un delay
        else:
            print("La suma esta mal")
            print("El resultado era", matriz3)#si esta mal mostrar enunciado con la matriz correcta
            correcto+=-1#contador menos uno
            incorrecto+=1#contador mas uno
            time.sleep(2)#delay
    if correcto==10:#si tienes todas bien completas el nivel
        print(f'Felicidades {nombre} por completar el nivel 1')
    else:
        print('no pudiste completar el nivel uno')#No tuviste todas bien
        print("Tus aciertos fueron", correcto)#tu numero de correctas
        print("Tus incorrectos fueron", incorrecto)#tu numero de incorrectas
#---------matrices
          
def suma_fracciones(nombre):
#----------Fracciones
#---------fracciones
    print('-----------------Bienvenido a suma y multiplicacion de fracciones---------------------------')
    print("el primer round van a ser sumas y sumas más complejas")
    print('Si crees que tienes lo necesario, puedes acceder al nivel dos que es multiplicaciones de fracciones ')
    print("Empieza nivel 1")
    correctas=0#contador en cero
    incorrectas=0#contador en cero
    for a in range(5):#hacer bucle 5 veces
        a=random.randrange(1,10)#dato random
        b=random.randrange(1,10)#dato random
        fraccion_1=Fraction(a , b)#funcion fraction con dato random
        fraccion_2=Fraction(a , b)#funcion fraction con dato random
        resultado=fraccion_1+fraccion_2#resultado de la fraccion
        pregunta=Fraction(input(f'¿Cuanto es la suma de {fraccion_1}+{fraccion_2}?: '))#preguntar respueta a usuario 
        if pregunta == resultado:#Si pregunta es igual a resultado esta bien
            print('Es correcto')
            correctas+=1
        else:#esta mal
            print("Esta mal")
            print('El resultado era:',resultado)#mostrar el resultado
            correctas+=-1
            incorrectas+=1
    if correctas==5:#si tienes 5 bien pasas al siguiente nivel
        print("Ahora va el segundo nivel de sumas")
        for b in range(5):#mismo proceso que arriba
            a=random.randrange(10,20)#datos random más complejos
            b=random.randrange(10,20)#datos random más complejos
            fraccion_1=Fraction(a , b)
            fraccion_2=Fraction(a , b)
            resultado=fraccion_1+fraccion_2
            pregunta=Fraction(input(f'¿Cuanto es la suma de {fraccion_1}+{fraccion_2}?: '))
            if pregunta == resultado:
                print('Es correcto')
                correctas+=1
            else:
                print("Esta mal")
                print('El resultado era: ', resultado)
                correctas+=-1
                incorrectas+=1
    if correctas==10:#Si tienen 10 bien, tienes la oportunidad a acceder a un nivel más complejo
        print(f'Felicidades {nombre} por completar el nivel 1')
        level=input("¿Quieres pasar al segundo nivel? s/n : ")#preguntar si quiere continuar
        level.lower()#por si la pone en mayuscula
        if level == 's':#si es igual a s, pasar al segundo nivel
            print("Ahora van las multiplicaciones")
            for c in range(5):#mismo proceso que nivel 1, pero con multi
               a=random.randrange(1,10)
               b=random.randrange(1,10)
               fraccion_1=Fraction(a , b)
               fraccion_2=Fraction(a,b)
               resultado=fraccion_1*fraccion_2
               pregunta=Fraction(input(f'¿Cuanto es la multiplicación de {fraccion_1}*{fraccion_2}?: '))
               if pregunta == resultado:
                   print('Es correcto')
                   correctas+=1
               else:
                   print("Esta mal")
                   print('El resultado era: ', resultado)
                   correctas+=-1
                   incorrectas+=1
            if correctas==15:
                print("Ahora va el segundo nivel de multiplicacion")
                for d in range(5):
                    a=random.randrange(1,20)
                    b=random.randrange(1,20)
                    fraccion_1=Fraction(a,b)
                    fraccion_2=Fraction(a,b)
                    resultado=fraccion_1/fraccion_2
                    pregunta=Fraction(input(f'¿Cuanto es la división de {fraccion_1}/{fraccion_2}?: '))
                    if pregunta == resultado:
                        print('Es correcto')
                        correctas+=1
                    else:
                        print("Esta mal")
                        print('El resultado era: ', resultado)
                        
                        incorrectas+=1
            if correctas==20:#Si tienes 20 bien completaste el nivel 2, si no te muestra tus incorrectas y cuantas tuviste de 20
                print(f'Felicidades {nombre} por completar el nivel 2')
                print("Estos son el numero que te equivocaste", incorrectas)
            else:
                print("No completaste el nivel, pero lo intentaste")
                print("Tus aciertos son", correctas,"/20")
        else:#por si no quieres jugar el nivel 2
            print("Gracias por jugar el nivel 1")
def potencias(nombre):
#----------Potencias
    print('-----------------Bienvenido a Potencias---------------------------')
    print("el primer round va de 1 a 10")
    print("Si crees que tienes lo necesario, puedes acceder al nivel dos que es suma de potencias ")
    print("Empieza nivel 1")
    correctas=0#contador en cero
    incorrectas=0#contador en cero
   # while correctas<10:#mientras que contador sea meno que 10 no deja avanzar
    for a in range(10):
       a=random.randint(1, 12)#dato random
       resultado=a**2#el resultado
       pregunta=(int(input(f'¿Cuanto vale {a}**2?: ')))#preguntar a usuario por respuesta
       if pregunta == resultado:
           print("Es correcto")
           print(correctas)
           correctas+=1
       else:
           print("Esta mal")
           print("El resultado es ", resultado)
           incorrectas+=1
        
    if correctas==10:#si tienen 10 bien preguntar si quieren pasar al siguiente nivel
        print(f'Felicidades {nombre} por completar el nivel 1')
        level=input("¿Quieres pasar al segundo nivel? s/n : ")#mismo proceso de suma de fracciones
        level.lower()
        if level == 's':
            for a in range(10):
                a=random.randint(1, 12)
                b=a=random.randint(1, 12)
                resultado=(a**2)+(b**2)
                pregunta=(int(input(f'¿Cuanto vale la suma de {a}**2+{b}**2?: ')))
                if pregunta == resultado:
                    print("Es correcto")
                    print(correctas)
                    correctas+=1
                else:
                    print("Esta mal")
                    print("El resultado es ", resultado)
                    incorrectas+=1
            if correctas==20:
                print(f'Felicidades {nombre} por completar el segundo nivel')
                print("Tus incorrectas son",incorrectas )
            else:
                print('No completaste el nivel')
                print("tus aciertos fueron", correctas,"/10")
    else:
            print("Gracias por haber jugado el primer nivel")
def juego_gato(nombre):
#-----Inicio del juego/ Selección de ficha----
    def inicio_juego():
        print(f'***BIENVENIDO {nombre}****')
        time.sleep(1)#delay
        while True:
            ficha=input("Seleccione ficha: X /O\n")#pedir si es Xo O
            ficha=ficha.upper()
            if ficha=='X':#si escogemos x, ordenador es O
                humano='X'
                ordenador='O'
                break
            elif ficha=='O':#o al revez
                humano='O'
                ordenador='X'
                break
            else:
                print("Por favor, introduce una ficha posible. ")
        return(humano,ordenador)#retornar la ficha
    
    #-----CREACIÓN DEL TABLERO------
    def tablero():#crear el tablero
        print("la casilla 9 es 0")
        print("TRES EN RAYA / TIC TAC TOE")
        print()
        print("    |       |     ")
        print(" 1 {}  |  2 {}     | 3 {}    ".format(matriz[0],matriz[1],matriz[2]))
        print("    |       |     ")
        print("------------------")
        print("    |       |     ")
        print(" 4 {}   | 5 {}      |6 {}     ".format(matriz[3],matriz[4],matriz[5]))
        print("    |       |     ")
        print("------------------")
        print("    |       |     ")
        print(" 7 {}   | 8 {}      |9 {}     ".format(matriz[6],matriz[7],matriz[8]))
        print("    |       |     ")
        
    #-------DEFINIR FINALES DE PARTIDA----
    def empate(matriz):#crear la posibilidad de que hacer si hay un empate
        empate=True
        i=0
        while(empate==True and i<9):
            if matriz[i]==" ":
                empate=False
            i=i+1
        return empate
    
    def victoria(matriz):#crear funcion para decidir ganadro
        if (matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" " or matriz[6]==matriz[7]==matriz[8]!=" " 
            or matriz[0]==matriz[3]==matriz[6]!=" " or matriz[1]==matriz[4]==matriz[7]!=" " or matriz[2]==matriz[5]==matriz[8]!=" " 
            or matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" " ):
            return True
        else:
            return False
    
    #-------Movimientos-----
    def movimiento_jugador():#crear los movimiento que se pueden hacer en el tablero
        while True:
            posiciones=[0,1,2,3,4,5,6,7,8]
            casilla=int(input("Seleccione casilla: "))
            if casilla not in posiciones:
                print("Casilla no disponible")
            else:
                if matriz[casilla-1]==" ":
                    matriz[casilla-1]=humano
                    break
                else:
                    print("Casilla no disponible")
                    
    def movimiento_ordenador():#crear rival en el tablero
        posiciones=[0,1,2,3,4,5,6,7,8]
        casilla=9
        parar=False
        
        for i in posiciones:
            copia=list(matriz)
            if copia[i]==" ":
                copia[i]=ordenador
                if victoria(copia)==True:
                    casilla=i
        
        if casilla==9:
            for j in posiciones:
                if copia[i]==" ":
                    copia[i]=humano
                    if victoria(copia)==True:
                        casilla=j
        if casilla==9:
            while(not parar):
                casilla=random.randint(0, 8)
                if matriz[casilla]==" ":
                    parar=True
        matriz[casilla]=ordenador
    a=True
    while a==True:#bucle para poder repetir el juego
            
        matriz=[" "]*9
        #os.system("cls")#limpia la pantalla al comienzo de cada partida
        humano,ordenador=inicio_juego()
        partida=True
        ganador=0
        
        while partida:
            ganador=ganador+1
            #os.system("cls")
            tablero()
            
            if victoria(matriz):
                if ganador%2==0:
                    print("**Gana el jugador**")
                    print("**Fin del juego**")
                    a=False
                    time.sleep(5)
                    partida=False
                else:
                    print("**Gana el ordenador**")
                    print("**Fin del juego**")
                    a=False
                    time.sleep(5)
                    partida=False
            elif empate(matriz):
                print("**Empate**")
                print("**Fin del juego**")
                a=False
                time.sleep(5)
                partida=False
            elif ganador%2==0:
                print("El ordenador esta pensando")
                time.sleep(2)
                movimiento_ordenador()
            else:
                movimiento_jugador()
def archivo_excel():
    pg1=['¿Cuál es el nombre del río más largo del mundo?', "A: Río Nilo", "B: Río Amazonas", "C: Río Danubio", "A"]
    pg2=["¿Cuál es la nación más pequeña del mundo?", "A: Andorra", "B: Mónaco", "C: El Vaticano", "C"]
    pg3=["¿Cuándo terminó la II Guerra Mundial?", "A: 1945", "B: 1947", "C: 1943", "A"]
    pg4=["¿En qué año llegó Cristobal Colón a América?", "A: 1429", "B: 1492", "C: 1592","A"]
    pg5=["¿Cuál es el libro sagrado de los musulmanes?", "A: La Biblia", "B: El Talmud", "C: El Corán", "C"]
    pg6=["¿En qué país se usó la primera bomba atómica?", "A: Rusia", "B: Estados Unidos", "C: Japón", "C"]
    pg7=[" ¿Cuál fue el primer hombre en ir a la luna?", "A: Louis Armstrong", "B: Neil Armstrong", "C: Michael Armstrong", "B"]
    pg8=["¿Quién fue el primer emperador romano?", "A: César Augusto", "B: Julio Cesar","C: Marco Aurelia", "A"]
    pg9=[" ¿Quién pintó el famoso cuadro La última cena?", "A: Rembrandt", "B: Velazquez", "C: Leonardo da Vinci", "C"]
    pg10=["¿Cuál es el único mamífero que puede volar?", "A: Murciélago", "B: Avestruz", "C: Águila", "A"]
    
    lista=[pg1,pg2,pg3,pg4,pg5,pg6,pg7,pg8,pg9,pg10]
    df_lista=pd.DataFrame(lista,
                          columns=['Pregunta', 'A', 'B', 'C', 'Respuesta'])
    df_lista.to_csv("lista.csv")
    print()            
                

main()
        
    