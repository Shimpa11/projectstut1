import numpy as np
import pandas as pd
oddNumbers=np.arange(1,100,2)
evenNumbers=np.arange(0,100,2)
# python dictionary
numbers={
    "oddNumbers":oddNumbers,"evenNumbers":evenNumbers
}
table=pd.DataFrame(numbers)
print(table)
print("---sum is---:")
print(table.sum())
print("----max---- ")
print(table.max())
print("====standard deviation==")
print(table.std())
print("-----min----")
print(table.min())