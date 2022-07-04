import pandas as pd

s1 = pd.Series([1,2,3,4,5,6], index=list('asdfgh'))
s2 = pd.Series([1,2,3,4,5,6], index=list('sadfgh'))
print(s1 * s2)
print(s1.add(s2,fill_value=0)) # add function is also used to fill value