#Importacion de Librerias Necesarias
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pylab as pl
import numpy as np
import math
import os


#Declaracion de variable global
sumatoria = 0.0
sumatoria_izquierda = 0.0
sumatoria_derecha = 0.0
sumatoria_central = 0.0
Valor_DeltaX = 0.0


#Funcion de Xi
def Funcion_Xi (Xi) :
    #Expresar en Operadores la Funcion de X
    Valor_Xi =  Xi**2
    return Valor_Xi


def Delta_X (Rango_A, Rango_B, Intervalos):
    global Valor_DeltaX
    Valor_DeltaX = (Rango_B - Rango_A) / Intervalos
    #print (Valor_DeltaX)


def Fsumatoria_izquierda(Rango_A, Rango_B, Intervalos):
    global sumatoria_izquierda
    global Valor_DeltaX
    
    for i in np.arange(Rango_A, Rango_B, Valor_DeltaX):
        #print (i)
        sumatoria_izquierda = sumatoria_izquierda + (Funcion_Xi(i)*Valor_DeltaX)
    
    print("Valor de la sumatoria por izquierda hasta: ",sumatoria_izquierda)
    
    atenuacion = (Rango_B-Rango_A)/100
    x = np.arange(Rango_A, Rango_B+atenuacion, atenuacion)
    plt.plot(x, Funcion_Xi(x), color='blue')

    #Generacion de los valores del rango antes preestablecido
    Valores = [i for i in np.arange(Rango_A,Rango_B, Valor_DeltaX)]

    #Generacion de los valores de la sumatoria usando la funcion Funcion() 
    Array = [Funcion_Xi(i) for i in np.arange(Rango_A,Rango_B,Valor_DeltaX)]

    plt.bar(Valores,Array,width=Valor_DeltaX,alpha=0.5,align= 'edge', facecolor='red')
    plt.xlabel('xi')
    plt.ylabel('f(xi)')
    plt.title('Suma Izquierda de Riemann para f(xi)')
    plt.figtext(0.01,0.01, "Suma de Riemann: " + str(sumatoria_izquierda), color='r')
    plt.show()

    #Declaracion de la ventana
    fig, ax = plt.subplots()

    print("")
    print("******************** Resultados Generados ************************")
    print("")
    print(" Generando la grafica .....")
    #Hacer una pausa para verificar los datos
    os.system("pause")
    #Generacion de la grafica en la variable de declaracion de ventana
    ax.plot(Valores , Array, marker = 'o')

    #Instrucciones para extender al maximo la ventana para mostrar la Grafica
    #wm = plt.get_current_fig_manager()
    #wm.window.state('zoomed')

    #Mostrar la ventana con la grafica
    plt.show()


def Fsumatoria_derecha(Rango_A, Rango_B, Intervalos):
    global sumatoria_derecha
    global Valor_DeltaX    

    for i in np.arange(Rango_A + Valor_DeltaX, Rango_B + 0.01, Valor_DeltaX):
        #print (Rango_A + Valor_DeltaX)
        sumatoria_derecha = sumatoria_derecha + (Funcion_Xi(i)*Valor_DeltaX)
        
    print("Valor de la sumatoria por derecha hasta: ",sumatoria_derecha)
    
    atenuacion = (Rango_B-Rango_A)/100
    x = np.arange(Rango_A, Rango_B+atenuacion, atenuacion)
    plt.plot(x, Funcion_Xi(x), color='blue')

    #Generacion de los valores del rango antes preestablecido
    Valores = [i for i in np.arange(Rango_A,Rango_B, Valor_DeltaX)]

    #Generacion de los valores de la sumatoria usando la funcion Funcion() 
    Array = [Funcion_Xi(i) for i in np.arange(Rango_A+Valor_DeltaX,Rango_B+atenuacion,Valor_DeltaX)]

    plt.bar(Valores,Array,width=Valor_DeltaX,alpha=0.5,align= 'edge', facecolor='red')
    plt.xlabel('xi')
    plt.ylabel('f(xi)')
    plt.title('Suma Derecha de Riemann para f(xi)')
    plt.figtext(0.01,0.01, "Suma de Riemann: " + str(sumatoria_derecha), color='r')
    plt.show()

    #Declaracion de la ventana
    fig, ax = plt.subplots()
    

    print("")
    print("******************** Resultados Generados ************************")
    print("")
    print(" Generando la grafica .....")
    #Hacer una pausa para verificar los datos
    os.system("pause")
    #Generacion de la grafica en la variable de declaracion de ventana
    ax.plot(Valores , Array, marker = 'o')

    #Instrucciones para extender al maximo la ventana para mostrar la Grafica
    #wm = plt.get_current_fig_manager()
    #wm.window.state('zoomed')

    #Mostrar la ventana con la grafica
    plt.show()


def Fsumatoria_central(Rango_A, Rango_B, Intervalos):
    global sumatoria_central
    global Valor_DeltaX
    
    for i in np.arange(Rango_A, Rango_B , Valor_DeltaX):
        #print (Rango_A + Valor_DeltaX)
        sumatoria_central = sumatoria_central + ((Funcion_Xi(i+(Valor_DeltaX/2)))*Valor_DeltaX)
        
    print("Valor de la sumatoria por central hasta: ",sumatoria_central)
    
    atenuacion = (Rango_B-Rango_A)/100
    x = np.arange(Rango_A, Rango_B+atenuacion, atenuacion)
    plt.plot(x, Funcion_Xi(x), color='blue')

    #Generacion de los valores del rango antes preestablecido
    Valores = [i for i in np.arange(Rango_A,Rango_B, Valor_DeltaX)]

    #Generacion de los valores de la sumatoria usando la funcion Funcion() 
    Array = [Funcion_Xi(i) for i in np.arange(Rango_A+(Valor_DeltaX/2),Rango_B+atenuacion,Valor_DeltaX)]

    plt.bar(Valores,Array,width=Valor_DeltaX,alpha=0.5,align= 'edge', facecolor='red')
    plt.xlabel('xi')
    plt.ylabel('f(xi)')
    plt.title('Suma Derecha de Riemann para f(xi)')
    plt.figtext(0.01,0.01, "Suma de Riemann: " + str(sumatoria_derecha), color='r')
    plt.show()

    #Declaracion de la ventana
    fig, ax = plt.subplots()

    print("")
    print("******************** Resultados Generados ************************")
    print("")
    print(" Generando la grafica .....")
    #Hacer una pausa para verificar los datos
    os.system("pause")
    #Generacion de la grafica en la variable de declaracion de ventana
    ax.plot(Valores , Array, marker = 'o')

    #Instrucciones para extender al maximo la ventana para mostrar la Grafica
    #wm = plt.get_current_fig_manager()
    #wm.window.state('zoomed')

    #Mostrar la ventana con la grafica
    plt.show()




Intervalo_A = 0.0 
Intervalo_B = 0.0

print("")
print("******************** Proyecto Sumas Riemann **********************")
print("******************************************************************")
print("********* Serie de sumas parciales de una Sumatoria dada *********")
print("")
Intervalo_A = float(input("Introduce intervalo A de la Funcion: "))
Intervalo_B = float(input("Introduce intervalo B de la Funcion: "))
N_Intervalos = int(input("Introduce numero de Intervalos: "))

Delta_X (Intervalo_A, Intervalo_B, N_Intervalos)

print("1.- Sumatoria Derecha")
print("2.- Sumatoria Izquierda")
print("3.- Sumatoria Central")

Valor_Menu = int(input("Selecciona la opcion a elegir: "))

if Valor_Menu == 1:
    Fsumatoria_derecha(Intervalo_A, Intervalo_B, N_Intervalos)
elif Valor_Menu == 2:
    Fsumatoria_izquierda(Intervalo_A, Intervalo_B, N_Intervalos)
elif Valor_Menu == 3:
    Fsumatoria_central(Intervalo_A, Intervalo_B, N_Intervalos)
else:
    print("No existe!")

print ("Calculo realizado!!!")

