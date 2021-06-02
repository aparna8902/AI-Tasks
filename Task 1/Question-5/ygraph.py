import pandas as pd
from matplotlib import pyplot as plt
from math import log
x=[]
y=[]
for i in range(1,101):
    x.append(i)
    y.append(i**2 + log(i/2))

with open("C:/Users/aparn/OneDrive/Desktop/AI Tasks/Task 1/Question-5/input.csv",'w') as f:
    f.write("x,y\n")
    for i in range(100):
        f.write(str(x[i])+","+str(y[i])+"\n")

data = pd.read_csv('C:/Users/aparn/OneDrive/Desktop/AI Tasks/Task 1/Question-5/input.csv')
plt.plot(data.x,data.y,color='red', marker='o', markerfacecolor='blue', markersize=1)
plt.title("Graph y = x^2 + log(x/2)")
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.show()
