import pandas as pd

r = pd.read_csv('pandas/abc.csv',usecols=['age'])
print(r.isnull())

a =r.dropna(inplace=False) #copy
print(a)
print(r)
print(r.fillna(0))
print(r.describe())
print(r.idxmax())

for i,v in a.items():
    print(i)