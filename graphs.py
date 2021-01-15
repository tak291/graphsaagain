import pandas as pd 

df = pd.read_csv('/home/kike/python/pythonprojects/graphs/graphsaagain/assignment.csv',header=None, skiprows=1)


#Printing the first 10 columns
#print (df.head(1))


location = df[0]
dates = df[1]
orders = df[2]
percentage = df[3]

#print(location)

seen = set()
result = []

# for i in location:
#     if i not in location:
#         seen.add(i)
#         result.append(i)

#list comprehensions.sum()
[seen.add(i) for i in location if i not in seen]


print (seen)


print (df.groupby([1]).sum())


