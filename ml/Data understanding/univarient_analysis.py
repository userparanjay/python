import pandas as pd                  # Import pandas for data manipulation
import seaborn as sns               # Import seaborn for advanced visualization
import matplotlib.pyplot as plt     # Import matplotlib for basic plotting

# Load dataset from CSV file into a DataFrame
df = pd.read_csv('train.csv')

# Display first 5 rows to understand structure of data
df.head()


# Count plot for 'Survived' column (0 = No, 1 = Yes)
# Shows how many people survived vs not survived
sns.countplot(x=df['Survived'])

# Alternative way (commented): bar plot using value_counts
# df['Survived'].value_counts().plot(kind='bar')


# Count plot for 'Sex' column
# Shows number of males vs females in dataset
sns.countplot(x=df['Sex'])


# Pie chart for 'Embarked' column
# Shows percentage distribution of passengers from each port
df['Embarked'].value_counts().plot(kind='pie', autopct='%.2f')


# Histogram for 'Age'
# Shows distribution of age (frequency of different age ranges)
plt.hist(df['Age'])


# Distribution plot (DEPRECATED in seaborn)
# Shows histogram + KDE (smooth density curve)
# ⚠️ Replace with: sns.histplot(df['Age'], kde=True)
sns.distplot(x=df['Age'])


# Box plot for 'Fare'
# Shows median, quartiles, and detects outliers in fare data
sns.boxplot(x=df['Fare'])


# Get minimum value of 'Age'
# Useful to check youngest passenger
df['Age'].min()


# Calculate skewness of 'Age'
# > 0 → right skew (tail on right)
# < 0 → left skew (tail on left)
df['Age'].skew()