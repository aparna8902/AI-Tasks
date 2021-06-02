import matplotlib.pyplot as plt
n=int(input("Enter the number of coordinates: "))
x=[]
y=[]
for i in range(n):
    a=float(input("Enter x"+str(i+1)+" : "))
    b=float(input("Enter y"+str(i+1)+" : "))
    x.append(a)
    y.append(b)

plt.plot(x,y,color='red', marker='o', markerfacecolor='blue', markersize=8)
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.title('Graph of the entered coordinates', fontsize='14')
plt.show()
