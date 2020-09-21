# IMPORT LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

# np.linspace(start, stop, number) : Return evenly spaced numbers over a specified interval.
# random.gauss() - generate random numbers - parameters: mean and sigma(std)

x2=np.linspace(-10,10,10000)

yup2=[]
for i in x2:
    yup2.append(i*i+abs(random.gauss(8,2)))
ydown2=[]
for i in x2:
    ydown2.append(i*i-abs(random.gauss(8,2)))
# QUADRATIC EQUATION : Y=X*X
plt.plot(x2,x2*x2, color='orange')

plt.scatter(x2,yup2,color='red')
plt.scatter(x2,ydown2,color='blue')

plt.grid(alpha=0.4, linestyle='--')
plt.title('Quadratic Equation')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

x2=x2.tolist()

xrow=x2+x2
yrow=yup2+ydown2

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
df.to_csv('quadratic_2.csv',index=False)
