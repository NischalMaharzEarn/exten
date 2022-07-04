from numpy import int32, int8
import pandas as pd

df = pd.DataFrame([[1,2,3,4],['a','b','c','d']], columns=['first value', 'second value','third value','fourth value'])
print(df['first value'])