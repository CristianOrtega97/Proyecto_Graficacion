import pandas as pd
import matplotlib.pyplot as plt

def cal_circulo_bressenham(radio):
    switch = 3 - (2 * radio)
    x = 0
    y = radio
    #Agregar info a los Octantes
    while x <= y:
        #Primer Octante
        x_point1.append(x)
        y_point2.append(-1*(y))
        #Segundo Octante
        x_point3.append(y)
        y_point4.append(-1*(x))
        #Tercer Octante
        x_point5.append(y)
        y_point6.append(x)
        #Cuarto Octante
        x_point7.append(x)
        y_point8.append(y)
        #Quinto Octante
        x_point9.append(-1*(x))
        y_point10.append(y)       
        #Sexto Octante
        x_point11.append(-1*(y))
        y_point12.append(x)
        #Septimo Octante
        x_point13.append(-1*(y))
        y_point14.append(-1*(x))
        #Ultimo Octante
        x_point15.append(-1*(x))
        y_point16.append(-1*(y))
        if switch < 0:
            switch = switch + (4 * x) + 6
        else:
            switch = switch + (4 * (x - y)) + 10
            y = y - 1
        x = x + 1

#Primer Octante
x_point1 = []
y_point2 = []

#Segundo Octante
x_point3 = []
y_point4 = []

#Tercer Octante
x_point5 = []
y_point6 = []

#Cuarto Octante
x_point7 = []
y_point8 = []

#Quinto Octante
x_point9 = []
y_point10 = []

#Sexto Octante
x_point11 = []
y_point12 = []

#Septimo Octante
x_point13 = []
y_point14 = []

#Ultimo Octante
x_point15 = []
y_point16 = []

#ARRAY COMPLETO
x_point = []
y_point = []
radio = (int(input("Ingrese el valor numerico del radio: ")))
selected_color = input('Ingrese el color "EN INGLÉS" que quiera utilizar: ')
cal_circulo_bressenham(radio)

#Agregar Octantes al array original
#Primer Octante
for i in range(len(x_point1)):
    x_point.append(x_point1[i])
    y_point.append(y_point2[i])

#Segundo Octante
for i in range(len(x_point3)):
    x_point.append(x_point3[i])
    y_point.append(y_point4[i])

#Tercer Octante
for i in range(len(x_point5)):
    x_point.append(x_point5[i])
    y_point.append(y_point6[i])

#Cuarto Octante
for i in range(len(x_point7)):
    x_point.append(x_point7[i])
    y_point.append(y_point8[i])

#Quinto Octante
for i in range(len(x_point9)):
    x_point.append(x_point9[i])
    y_point.append(y_point10[i])

#Sexto Octante
for i in range(len(x_point11)):
    x_point.append(x_point11[i])
    y_point.append(y_point12[i])

#Septimo Octante
for i in range(len(x_point13)):
    x_point.append(x_point13[i])
    y_point.append(y_point14[i])

#Ultimo Octante
for i in range(len(x_point15)):
    x_point.append(x_point15[i])
    y_point.append(y_point16[i])

#Imprimir Circulo
print(pd.DataFrame({"X point":x_point,"Y point":y_point}))
plt.scatter(x_point, y_point, color=selected_color)
plt.plot(x_point, y_point)
plt.show()
