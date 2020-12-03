import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import math

respuesta = 1

#Función para Graficar y mostrar coordenadas
def graficar(x_list,y_list,selected_color):
    print(pd.DataFrame({"X":x_list, "Y":y_list}))
    plt.scatter(x_list, y_list, color=selected_color)
    plt.plot(x_list, y_list)
    plt.show()

#Función Linea DDA
def dda_linea():
    x1 = int(input("Enter x1 :")) 
    y1 = int(input("Enter y1 :")) 
    x2 = int(input("Enter x2 :")) 
    y2 = int(input("Enter y2 :"))
    selected_color = input('Ingrese el color "EN INGLÉS" que quiera utilizar: ')
    x2_last = x2
    y2_last = y2


    px = x2 - x1
    py = y2 - y1

    #ABS - Retorna valor absoluto
    #Validador para saber cuanto vale pasos
    #Error si no es valor absoluto por diferentes tipos de variables
    if abs(px)>=abs(py):
        paso = abs(px)
    else:
        paso = abs(py)

    #Genera el valor de las pendientes
    px /= paso
    py /= paso

    #display list
    x_list = []
    y_list = []

    i=1

    while i<=paso:
        #Agrega los datos al arreglo
        x_list.append(int(x1))
        y_list.append(int(y1))
        x1 += px
        y1 += py
        i+=1

    x_list.append(x2_last)
    y_list.append(y2_last)
    graficar(x_list,y_list,selected_color)

#Función Linea Bresenham
def bre_linea():
    #Se ingresan los datos
    x1 = int(input("Ingrese x1 :")) 
    y1 = int(input("Ingrese y1 :")) 
    x2 = int(input("Ingrese x2 :")) 
    y2 = int(input("Ingrese y2 :"))
    selected_color = input('Ingrese el color "EN INGLÉS" que quiera utilizar: ')

    #Se guardan los ultimos dos datos para simplemente ser agregados al final del arreglo
    x2_last = x2
    y2_last = y2

    dx = x2- x1
    dy = y2- y1

    #Se genera la pendiente que tendrá la linea
    m = dy/dx

    #
    e = m - 0.5

    #Arreglo para los datos
    x_list = []
    y_list = []

    for i in range(dx):
        x_list.append(x1)
        y_list.append(y1)
        while(e>0):
            y1+=1
            e=e-1
        x1+=1
        e+=m
    x_list.append(x2_last)
    y_list.append(y2_last)
    graficar(x_list,y_list,selected_color)

#Función Circulo DDA
def dda_circulo():
    #Ingreso de datos
    x_ing = int(input("Ingrese x :")) 
    y_ing = int(input("Ingrese y :"))
    rad = int(input("Ingrese radio: "))
    selected_color = input('Ingrese el color "EN INGLÉS" que quiera utilizar: ')

    #Generar el valor de Radio al Cuadrado
    rad2 = pow(rad,2)

    #Se ingresa x como si fuera cero ya que todos los datos se comienzan de la posición 0,0, 
    #Por lo que si se ingresa despues una coordenada diferente solo se sumen los datos
    x = 0

    #Se genera X^2
    x2 = pow(x,2)
    #Se resta radio al cuadrado por x al cuadrado
    raiz = rad2-x2
    #El Valor de Y como si estuviera comenzando en la posición 0
    y = int(round(math.sqrt(raiz)))
  
    #Contenedores de Coordenadas
    x_list = []
    y_list = []

    while x < y:
        #Agrega las coordenadas como si estuvieran en 0,0 pero suma los datos ingresados
        #Normal Primer
        x_list.append(x_ing+x)
        y_list.append(y_ing+y)
        #Espejo Primer
        x_list.append(x_ing+y)
        y_list.append(y_ing+x)

        #Normal Segundo
        x_list.append(x_ing-x)
        y_list.append(y_ing+y)
        #Espejo Segundo
        x_list.append(x_ing-y)
        y_list.append(y_ing+x)

        #Normal Tercer
        x_list.append(x_ing-x)
        y_list.append(y_ing-y)
        #Espejo Tercer
        x_list.append(x_ing-y)
        y_list.append(y_ing-x)

        #Normal Ultimo
        x_list.append(x_ing+x)
        y_list.append(y_ing-y)
        #Espejo Ultimo
        x_list.append(x_ing+y)
        y_list.append(y_ing-x)

        #Incrementa uno en X y Y lo vuelve a sacar para volver a validar
        # SQRT(R^2 - X^2)
        x += 1
        x2 = pow(x,2)
        raiz = rad2-x2
        y = int(round(math.sqrt(raiz)))

    graficar(x_list,y_list,selected_color)

#Función Circulo Bresenham
def bre_circulo():
    #Ingreso de datos
    x_ing = int(input("Ingrese x :")) 
    y_ing = int(input("Ingrese y :"))
    rad = int(input("Ingrese radio: "))
    selected_color = input('Ingrese el color "EN INGLÉS" que quiera utilizar: ')
    x = 0
    y = rad
    xK = 0
    yK = 2 * y_ing
    pK = 1 - rad

    #Contenedores de Coordenadas
    x_list = []
    y_list = []

    while x < y:
        #Agrega las coordenadas como si estuvieran en 0,0 pero suma los datos ingresados
        #Normal Primer
        x_list.append(x_ing+x)
        y_list.append(y_ing+y)
        #Espejo Primer
        x_list.append(x_ing+y)
        y_list.append(y_ing+x)

        #Normal Segundo
        x_list.append(x_ing-x)
        y_list.append(y_ing+y)
        #Espejo Segundo
        x_list.append(x_ing-y)
        y_list.append(y_ing+x)

        #Normal Tercer
        x_list.append(x_ing-x)
        y_list.append(y_ing-y)
        #Espejo Tercer
        x_list.append(x_ing-y)
        y_list.append(y_ing-x)

        #Normal Ultimo
        x_list.append(x_ing+x)
        y_list.append(y_ing-y)
        #Espejo Ultimo
        x_list.append(x_ing+y)
        y_list.append(y_ing-x)

        if pK >= 0:
            pK += xK - yK + 5
        else:
            pK += xK + 3

        if pK >= 0:
            y-=1
        
        xK = 2 * x
        yK = 2 * y
        x += 1
        
    graficar(x_list,y_list,selected_color)

#Función Elipse
def elipse():
    pass

#Función Parabola
def parabola():
    x_list = []
    y_list = []
    pk = 0
    TwoXk1 = 2
    TwoYk1 = 2

    x = int(input("Ingrese x :"))
    x_list.append(x)

    x+=1
    y = int(input("Ingrese y :"))
    y_list.append(y)
    y+=1
    pasos = int(input("Ingrese el numero de pasos: "))
    selected_color = input('Ingrese el color "EN INGLÉS" que quiera utilizar: ')

    for i in range(pasos):
        if pk > 0:
            pk -= TwoYk1
            x_list.append(x)
            y_list.append(y)
            y += 1
            x += 1
            TwoYk1 += 2
            TwoXk1 += 2
        else:
            x_list.append(x)
            y_list.append(y)
            pk += 1
            x += 1
            TwoXk1 += 2

    graficar(x_list,y_list,selected_color)

#Función Poligono
def poligono():
    pass

while respuesta != 0:
    try:
        print("---------------------------------------------------------")
        print("Seleccione una de las siguientes opciones")
        print("1.-Línea DDA")
        print("2.-Línea Bresenham")
        print("3.-Circulo DDA")
        print("4.-Circulo Bresenham")
        print("5.-Eclipse")
        print("6.-Parábola")
        print("7.-Polígono")
        print("0.-Salir")
        print("---------------------------------------------------------")
        print("")
        respuesta = int(input("Respuesta: "))
        print("")
        print("---------------------------------------------------------")

        #Linea DDA
        if respuesta == 1:
            dda_linea()

        #Linea Bresenham
        elif respuesta == 2:
            bre_linea()

        #Circulo DDA
        elif respuesta == 3:
            dda_circulo()

        #Circulo Bresenham
        elif respuesta == 4:
            bre_circulo()

        #Elipse
        elif respuesta == 5:
            elipse()

        #Parábola
        elif respuesta == 6:
            parabola()

        #Polígono
        elif respuesta == 7:
            poligono()

        #Salir
        elif respuesta == 0:
            print("Saliendo del programa")

        else:
            print("Ingrese una opción válida")

    except ValueError:
        print("Ingrese un caracter numerico y valido")