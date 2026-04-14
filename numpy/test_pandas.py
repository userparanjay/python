import pandas as pd   # For data manipulation
import numpy as np    # For numerical operations (like NaN)

print(pd.__version__)  # Print pandas version

# ---------------- BASIC DATAFRAME CREATION ----------------
df = pd.DataFrame([11,12,13], columns=['A'])  # Create DataFrame with one column
print(df)

# Create dictionary dataset
data = {
    'Name': ["x","y","z"],
    'Age': [10,12,44],
    'Salary': [1000,2000,3000]    
}

df = pd.DataFrame(data)  # Convert dictionary to DataFrame

# ---------------- BASIC DATA EXPLORATION ----------------
print(df.head(2))      # First 2 rows
print(df.tail(1))      # Last row
print(df.columns)      # Column names
print(df.describe())   # Statistical summary
print(df.shape)        # (rows, columns)

# ---------------- COLUMN RENAME ----------------
print(df.rename(columns={'Name':'Name of the person'}))  # Temporary rename
print(df)

# Permanent rename
print(df.rename(columns={'Name':'Name of the person'}, inplace=True))
print(df)

print(df.info)  # Info about DataFrame (NOTE: should be df.info())

# ---------------- FILE OPERATIONS ----------------
df.to_csv('data.csv', index=False)  # Save to CSV

load_data_frame = pd.read_csv('data.csv')  # Load from CSV
print(load_data_frame)

# ---------------- DATA SELECTION ----------------
print(df[['Age']])              # Select column
print(df.loc[df.Age == 10])     # Filter rows using condition
print(df.iloc[0])               # Select first row (index-based)

# Multiple condition filtering
filter_df = df[(df.Age > 10) & (df.Salary > 1000)]
print(filter_df)

# Replace values conditionally
print(df.where(df.Age > 10, other="not eligible"))

# ---------------- ADDING COLUMNS ----------------
df['Role'] = ['HR','CEO','CTO']  # New column
print(df)

df['Bonus'] = df.Salary * 0.2    # Derived column
print(df)

# ---------------- ADDING / UPDATING ROWS ----------------
df.loc[len(df)] = ['C',70,9000,'Manager',1800]  # Add new row
print(df)

df.loc[0,'Salary'] = 10000  # Update value
print(df)

# Conditional update
df.loc[df['Name of the person'] == 'C', 'Role'] = 'DIRECTOR'
print(df)

# ---------------- DELETE OPERATIONS ----------------
df.drop(df[df['Name of the person'] == 'C'].index, inplace=True)  # Delete row
print(df)

print(df.drop('Bonus', axis=1, inplace=True))  # Drop column
print(df)

# ---------------- SORTING ----------------
print(df.sort_values(by='Salary', ascending=False))  # Sort by Salary
print(df)

# ---------------- DATE OPERATIONS ----------------
df['DOJ'] = ['21-10-2000','20-11-2000','14-1-1999']  # Add date column
print(df)

print(df['DOJ'].dtype)  # Current type (object/string)

# Convert to datetime
df['DOJ'] = pd.to_datetime(df['DOJ'], format='%d-%m-%Y')
print(df)

print(df['DOJ'].dtype)  # Now datetime

# Extract date parts
print(df['DOJ'].dt.year)
print(df['DOJ'].dt.month)

df['Month'] = df['DOJ'].dt.month  # New column from date
print(df)

# Add 90 days to date
df['DOJ'] = df['DOJ'] + pd.Timedelta(days=90)
print(df)

# ---------------- MISSING VALUES ----------------
print(df.isnull())  # Check null values

# Introduce NaN
df.loc[df['Salary'] == 10000, 'Salary'] = np.nan
print(df.isnull())
print(df)

print(df.isnull().sum())  # Count nulls

print(df.fillna(0))  # Replace nulls with 0

# ---------------- GROUPING & AGGREGATION ----------------
print(df.Role.value_counts())  # Count of each role

# Average salary per role
print(df.groupby('Role')['Salary'].mean())

# Multiple aggregations
print(df.groupby('Month').agg({'Salary':'mean','Age':'max'}))

# ---------------- CONCAT & MERGE ----------------
df2 = pd.DataFrame({
    'Name': ["x","y","z"],
    'ID': [1,2,3]  
})

df3 = pd.DataFrame({
    'Score': [100,90,80],
    'ID': [1,2,3] 
})

print(df2, df3)

# Vertical concat (rows)
print(pd.concat([df2, df3], axis=0))

# Horizontal concat (columns)
print(pd.concat([df2, df3], axis=1))

# Merge (like SQL JOIN)
print(pd.merge(df2, df3, how='inner', left_on='ID', right_on='ID'))

# ---------------- QUERY ----------------
print(df.query('Age > 10'))  # SQL-like filtering