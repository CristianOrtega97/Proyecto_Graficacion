import pandas as pd
import matplotlib.pyplot as plt

x_init = []
y_init = []
x = int(input("Enter x :"))
y = int(input("Enter y :"))
rad = int(input("Enter radius: "))
x_init.append(x)
y_init.append(y)
pk = 1 - rad
Xk1=1
Yk1=rad
TwoXk1 = 2 * Xk1
TwoYk1 = 2 * Yk1

x_init.append(x+1)
y_init.append(y)
pk = pk + 0 + 3
Xk1 += 1
TwoXk1 += 2
x += 2
x_init.append(x)
y_init.append(y)

while TwoXk1 <= TwoYk1:
    print("PK= ",pk)
    print("X",TwoXk1)
    print("Y",TwoYk1)
    if(pk<0):
        pk = pk + TwoXk1 + 3
        TwoXk1 += 2
        x += 1
        x_init.append(x)
        y_init.append(y)    
    else:
        pk = pk + TwoXk1 - TwoYk1 + 5
        TwoXk1 += 2
        TwoYk1 -= 2
        x += 1
        y -= 1
        x_init.append(x)
        y_init.append(y) 

print(x_init)
print(y_init)
