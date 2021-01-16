import pandas as pd 

df = pd.read_csv('/home/kike/python/pythonprojects/graphs/graphsaagain/assignment.csv',header=None, skiprows=1,sep=',')


#Printing the first 10 columns
print (df.head(1))


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

# list comprehensions

# [seen.add(i) for i in location if i not in seen]

# print (seen)


#prints The colum names
print(df.columns)
#prints out what index the file starts at, finishes and how many it skips by.
print(df.index)

# #transfer values to arrays
# print(df.values)

#how many rows and columns?
print(df.shape)

print(df.info())

#Create a subset with just the location  and the number of orders
subset = df[[0,2]]

#Print out the first items on the subset to make sure we got the right callled callumns
print(subset.head())

#Pandas version for debugging
#print (pd.__version__)

#Locate the integer in the list.
loki = df.loc[[6,9]]

#locate by index. First make sure to put the index in the list.
loki2 = df.iloc[[7]]

print (loki2)


#This block of code needs to be checked. It's suppossed to
#iterate thorught the restaurant name given and add the column.
rest = df.loc[df[0]== "Bryant Park", [0,2]]

rest2 = rest[2].sum()

#print("Bryant park has sold", rest2, "in the year 2018")

january = df[[0,1, 2]]


print (january)

