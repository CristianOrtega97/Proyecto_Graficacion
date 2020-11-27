import pandas as pd
import matplotlib.pyplot as plt

i=3
x_init = []
y_init = []
x = int(input("Enter x :"))
y = int(input("Enter y :"))
rad = int(input("Enter radius: "))
x_init.append(x)
y_init.append(y+rad)

pk = (1 - rad)
Xk1=1
Yk1=rad
TwoXk1, TwoXk1Temp = Xk1 * 2,Xk1 * 2
TwoYk1 = Yk1 * 2
x+=1
y+=rad
x_init.append(x)
y_init.append(y)
print()
print("PK= ",pk)
print("XK" ,TwoXk1)
print("YK", TwoYk1)

pk += 3
TwoXk1Temp += 2
x+=1
x_init.append(x)
y_init.append(y)
while TwoXk1 <= TwoYk1:
    print()
    print("PK= ",pk)
    print("X",TwoXk1Temp)
    print("Y",TwoYk1)
    if pk < 0:
        print("Entre MENOS 0")
        pk += TwoXk1 + 3
        x+=1
        TwoXk1 = TwoXk1Temp
        TwoXk1Temp += 2
        x_init.append(x)
        y_init.append(y)
    elif pk >= 0:
        pk += TwoXk1 -TwoYk1 + 5
        x+=1
        y-=1
        TwoXk1 = TwoXk1Temp
        TwoXk1Temp += 2
        TwoYk1 -= 2
        x_init.append(x)
        y_init.append(y)

print(x_init)
print(y_init)