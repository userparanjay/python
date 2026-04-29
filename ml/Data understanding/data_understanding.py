import pandas as pd

df=pd.read_csv('data.csv')

# Questions to ask to understand data 

# Q1.How big is your data?
df.shape()

# Q2.How does the data look like?
df.head()  or df.sample(5)

# Q3.What is the data type of cols?
df.info()

# Q4.Are there any missing values?
df.isnull().sum()

# Q5.How does the data look mathematically?
df.describe()

# Q6.Are there any duplicate values?
df.duplicated().sum()

# Q7.How is the correlation between cols?
df.corr() 
# it give range -1 to 1 -1 means inverse relation and 1 means direct relation