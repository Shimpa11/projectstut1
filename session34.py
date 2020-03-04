import numpy as np
import pandas as pd
# numpy array
array1=np.arange(1,101,2)
# array2 is a list
array2=list(range(1,101,2))
print(array1)
print(array2)

# pd series can take input as numpr array as well as list arrays
# S1=pd.Series(array2)
S1=pd.Series(array1)
print(S1)

print(S1.axes)

# but values are always numpy array
print(S1.values)
print(type(S1.values))


print(S1.head(5))
print(S1.tail(5))