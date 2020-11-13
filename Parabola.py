import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

x_point = []
y_point = []
pk = 0
TwoXk1 = 2
TwoYk1 = 2

x = int(input("Enter x :"))
x_point.append(x)
x+=1
y = int(input("Enter y :"))
y_point.append(y)
y+=1
steps = int(input("Enter the number of steps: "))
selected_color = input("Type the name of the color you would like to use: ")

for i in range(steps):
    if pk > 0:
        pk -= TwoYk1
        x_point.append(x)
        y_point.append(y)
        y += 1
        x += 1
        TwoYk1 += 2
        TwoXk1 += 2
    else:
        x_point.append(x)
        y_point.append(y)
        pk += 1
        x += 1
        TwoXk1 += 2

print(pd.DataFrame({"X point":x_point,"Y point":y_point}))
plt.scatter(x_point, y_point, color=selected_color)
plt.plot(x_point, y_point)
plt.show()