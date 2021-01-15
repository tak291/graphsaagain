import pandas as pd 

df = pd.read_csv('/home/kike/Programming/python/graphs/assignment.csv',header=None, usecols=[1,2,3])

print (df.head(10))

