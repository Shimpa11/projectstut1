import numpy as np
import pandas as pd
data=np.random.randn(5,4)
print(data)

# labelling cols yourself
table=pd.DataFrame(data,columns=["col1","col2","col3","col4"])
print(table)
# print(table["col2"])
# print(table.col3)

# iterate in DAtaframe-> will iterate col wise
print("iterate in DF1")
for key ,value in table.iteritems():
    print(key)
    print("===========")
    print(value)

print("iterate in DF2 row wise")
for key, value in table.iterrows():
        print(key)
        print("===========")
        print(value)

print("Entire data in tuples")
for row in table.itertuples():
    print(row)
    print("============")
