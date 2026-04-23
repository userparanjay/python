# Import pandas for data handling (DataFrame)
import pandas as pd

# Import numpy for numerical operations
import numpy as np

# Import matplotlib for plotting graphs
import matplotlib.pyplot as plt

# Import train_test_split to divide data into training and testing sets
from sklearn.model_selection import train_test_split

# Import accuracy_score to check model performance
from sklearn.metrics import accuracy_score

# Import function to visualize decision boundary
from mlxtend.plotting import plot_decision_regions

# Import pickle to save trained model into file
import pickle


# Load dataset from CSV file
df = pd.read_csv("/content/placement.csv")

# Show first 5 rows of dataset
df.head()

# Show dataset info (columns, datatype, null values)
df.info()

# Remove first unnecessary column (Unnamed index column)
df = df.iloc[:, 1:]

# Scatter plot of cgpa vs iq
plt.scatter(df["cgpa"], df["iq"])

# Scatter plot with placement color coding
# placement = 0 or 1
plt.scatter(df["cgpa"], df["iq"], c=df["placement"])


# Select input features (cgpa and iq)
input = df.iloc[:, 0:2]

# Select output target column (placement)
output = df.iloc[:, -1]


# Split data into train and test sets
# 90% training, 10% testing
input_train, input_test, output_train, output_test = train_test_split(
    input, output, test_size=0.1
)


# Import Logistic Regression model
from sklearn.linear_model import LogisticRegression

# Create model object
model = LogisticRegression()

# Train model using training data
model.fit(input_train, output_train)

# Predict results on test data
output_pred = model.predict(input_test)

# Print predicted values
print(output_pred)

# Calculate model accuracy
accuracy = accuracy_score(output_test, output_pred)

# Print accuracy score
print(accuracy)

# Plot decision boundary of trained model
plot_decision_regions(
    input_train.values,
    output_train.values,
    clf=model,
    legend=2
)

# Save trained model into model.pkl file
pickle.dump(model, open("model.pkl", "wb"))