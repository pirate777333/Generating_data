# IMPORT LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

# np.linspace(start, stop, number) : Return evenly spaced numbers over a specified interval.
# random.gauss() - generate random numbers - parameters: mean and sigma(std)

x1=[]
for i in range(10000):
    x1.append(random.uniform(0,3.5))

y1=[]
for i in range(10000):
    y1.append(random.uniform(1,9))

plt.scatter(x1,y1,color='red')

x2=[]
for i in range(10000):
    x2.append(random.uniform(3.55,6.5))

y2=[]
for i in range(10000):
    y2.append(random.uniform(1,9))

plt.scatter(x2,y2,color='green')

x3=[]
for i in range(10000):
    x3.append(random.uniform(6.55,10))

y3=[]
for i in range(10000):
    y3.append(random.uniform(1,9))

plt.scatter(x3,y3,color='blue')

plt.show()

c1=[]
for i in range(10000):
    c1.append('red')
c2=[]
for i in range(10000):
    c2.append('green')
c3=[]
for i in range(10000):
    c3.append('blue')


xrow=x1+x2+x3
yrow=y1+y2+y3
crow=c1+c2+c3
d={'x_axis':xrow,'y_axis':yrow,'color':crow}
df=pd.DataFrame(d)
print(df)
df.to_csv('squared_3.csv',index=False)
