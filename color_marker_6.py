# IMPORT LIBRARIES
import random
import numpy as np
import pandas as pd

# CREATING MARKERS AND COLORS 
m=['o','v','s','x','d','h']
c=['r','g','b','k','m','c']

# CREATE DATA FRAME
df=pd.DataFrame(columns=['x_axis','y_axis','markers','colors'])
# SET THE COUNTER
b=0
# 3000 ROWS
# FILLING THE DATA FRAME
for i in range(6000):
    if b<1001:
        df.loc[i]=random.randint(0,50),random.randint(0,50),m[0],c[0]
    if b>1000 and b<2001:
        df.loc[i]=random.randint(51,100),random.randint(0,50),m[1],c[1]
    if b>2000 and b<3001:
        df.loc[i]=random.randint(0,50),random.randint(51,100),m[2],c[2]
    if b>3000 and b<4001:
        df.loc[i]=random.randint(51,100),random.randint(51,100),m[3],c[3]
    if b>4000 and b<5001:
        df.loc[i]=random.randint(0,50),random.randint(101,150),m[4],c[4]
    if b>5000 and b<6001:
        df.loc[i]=random.randint(51,100),random.randint(101,150),m[5],c[5]

    b=b+1
# PRINT CREATED DATA FRAME
print(df)
# CREATE CSV FILE
df.to_csv('color_marker_6.csv', index=False)
