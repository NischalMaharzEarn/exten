import pandas as pd

a = range(5,15)
s = pd.Series(a, index=list('asdfghjklz'))

print(s.head())
print(s.tail(5))
print(s.head(-2))
print(s['s'])
print(s[1])
print(s.get('h'))
print(s.iloc[1])
print(s.loc['a'])