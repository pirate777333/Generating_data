# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt

# IMPORT DATA FRAME
df=pd.read_csv('color_6.csv')
# PLOT
for i in range(df.shape[0]):
    plt.scatter(df.iloc[i,0],df.iloc[i,1], color=df.iloc[i,2])

# SHOW
plt.show()
