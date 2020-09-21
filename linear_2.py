# IMPORT LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

# np.linspace(start, stop, number) : Return evenly spaced numbers over a specified interval.
# random.gauss() - generate random numbers - parameters: mean and sigma(std)

x=np.linspace(-10,10,10000)

a=2 # SLOPE
b=2 # Y INTERCEPT

y=a*x+b # LINEAR EQUATION

yup=[]
for i in x:
    yup.append(a*i+b+abs(random.gauss(8,2))) 
ydown=[]
for i in x:
    ydown.append(a*i+b-abs(random.gauss(8,2)))

plt.plot(x,y, color='orange')

plt.scatter(x,yup,color='red')
plt.scatter(x,ydown,color='blue')

plt.grid(alpha=0.4, linestyle='--')
plt.title('Linear Equation')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

x=x.tolist()

xrow=x+x
yrow=yup+ydown

c1=[]
for i in range(10000):
    c1.append('red')
c2=[]
for i in range(10000):
    c2.append('blue')

crow=c1+c2
print(len(xrow),len(yrow),len(crow))

d={'x_axis':xrow,'y_axis':yrow,'color':crow}
df=pd.DataFrame(d)
print(df)
df.to_csv('linear_2.csv',index=False)
