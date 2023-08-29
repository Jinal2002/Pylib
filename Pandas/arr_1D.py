# WAP to print 1D arry using pandas
'''
import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print(ds)
'''

# Program to convert a pandas module series into list using pandas
'''
import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds)
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))
'''

# WAPP to compare the elements of two pandas series
'''
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print("Series1: \n", ds1)
print("Series2: \n ", ds2)
print("Compare the elements of the said Series:")
print("Greater than: \n ", ds1 > ds2)
print("Less than:\n", ds1 < ds2)
'''

# WAPP to find scalar value
'''
import pandas as pd
import numpy as np

s = pd.Series("Arundhatee",index=range(1,14,3))
    
print(s)
'''

# WAP to modify the series
'''
import pandas as pd
ser1 = pd.Series([12, 34, 45, 50, 24])
ser1[0] = 2200
print(ser1)
ser1[0:3] = 1200
print(ser1)
'''

# Transpose in dataframe
'''
import pandas as pd
import numpy as np
staff=pd.Series([20,30,50])
salaries=pd.Series([40000,30000,25000])
avg=salaries/staff
org={'ppl':staff,'amount':salaries,'avg':avg}
df=pd.DataFrame(org)
print(df)
print("Now Transpose")
print(df.T)
'''

