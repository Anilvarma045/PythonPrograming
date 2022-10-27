import pandas as pd
import numpy as np

labels = ['a','b','c']
my_data = [11,22,33]

arr=np.array(my_data)      # np.array() is from numpy to convert List to array for faster process
d = {'a':11,'b':22,'c':33}

print(arr)          # array
print(my_data)      # List

# EX: print data as series it's mean index with existing Data

ex1 = pd.Series(my_data);      # print list as Series with index
print(ex1)

ex2= pd.Series(arr, labels)
# pd.Series(data=my_data,index=labels)    # anoter way    Customized index
print(ex2)

# Index and Slicing
ser1= pd.Series([1,2,4],['Ab','Bb','Cc'])
ser2= pd.Series([5,6,7],['An','il','va'])

print("values of Ab in Series",ser1[2])        # print with index
print("value of Bb in Series",ser1[1:2])      # print series with Range

# to read CSV
df=pd.read_csv('data.csv')
# above method to read data from pandas

print(df.to_string())