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

x_ent = int(input("Ingrese x :")) 
y_ent = int(input("Ingrese y :"))
rad = int(input("Ingrese radio: "))
selected_color = input('Ingrese el color "EN INGLÉS" que quiera utilizar: ')

#Generar el valor de Radio al Cuadrado
rad2 = pow(rad,2)
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
    x_list.append(x_ent+x)
    y_list.append(y_ent+y)
    #Espejo Primer
    x_list.append(x_ent+y)
    y_list.append(y_ent+x)

    #Normal Segundo
    x_list.append(x_ent-x)
    y_list.append(y_ent+y)
    #Espejo Segundo
    x_list.append(x_ent-y)
    y_list.append(y_ent+x)

    #Normal Tercer
    x_list.append(x_ent-x)
    y_list.append(y_ent-y)
    #Espejo Tercer
    x_list.append(x_ent-y)
    y_list.append(y_ent-x)

    #Normal Ultimo
    x_list.append(x_ent+x)
    y_list.append(y_ent-y)
    #Espejo Ultimo
    x_list.append(x_ent+y)
    y_list.append(y_ent-x)

    #Incrementa uno en X y Y lo vuelve a sacar para volver a validar
    # SQRT(R^2 - X^2)
    x += 1
    x2 = pow(x,2)
    raiz = rad2-x2
    y = int(round(math.sqrt(raiz)))

graficar(x_list,y_list,selected_color)