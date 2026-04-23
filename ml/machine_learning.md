Machine Learning Beginner Notes
1. What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence where computers learn patterns from data and make predictions without being explicitly programmed for every rule.

Instead of writing:

if cgpa > 7 and iq > 120:
    placed = True

We provide historical data, and the model learns the pattern itself.

2. Real Life Examples
Netflix movie recommendations
Amazon product recommendations
Spam email detection
Face recognition
Fraud detection
Student placement prediction
House price prediction
3. Types of Machine Learning
A. Supervised Learning

We have:

Input (X)
Output (Y)
X → Y

Example:

CGPA	IQ	Placement
7.5	120	1
5.0	90	0

Use when output is known.

Types of Supervised Learning
i) Regression

Predict numerical values.

Examples:

House price
Salary
Temperature
ii) Classification

Predict categories.

Examples:

Spam / Not Spam
Placed / Not Placed
Disease / No Disease
B. Unsupervised Learning

Only input is available, no output.

Model finds hidden patterns.

Examples:

Customer segmentation
Student grouping
Clustering
C. Reinforcement Learning

Agent learns using reward and punishment.

Examples:

Self-driving car
Chess AI
Game bots
4. ML Workflow
Collect Data
Clean Data
Select Features
Split Data
Train Model
Test Model
Evaluate
Deploy
5. Important Terms
Dataset

Collection of rows of data.

Features (Input / X)

Columns used for prediction.

Example:

cgpa, iq
Target (Output / Y)

What we predict.

placement
6. Example Dataset
cgpa	iq	placement
8.1	130	1
5.5	95	0

Inputs:

X = [cgpa, iq]

Output:

y = placement
7. Common Python Libraries
Library	Use
NumPy	Arrays / math
Pandas	Data analysis
Matplotlib	Graphs
Scikit-learn	Machine Learning
8. First ML Example
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("placement.csv")

X = df[['cgpa', 'iq']]
y = df['placement']

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print(prediction)
9. Train Test Split

Split data into:

Training Data = Learn
Testing Data = Check performance

Usually:

80% Train
20% Test
10. fit() vs predict()
fit()

Train model.

model.fit(X_train, y_train)
predict()

Make prediction.

model.predict(X_test)
11. Accuracy

Measures correct predictions.

from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)

Example:

0.85 = 85%
12. Common Algorithms
Classification
Logistic Regression
Decision Tree
Random Forest
SVM
KNN
Regression
Linear Regression
Ridge
Lasso
Clustering
KMeans
13. Overfitting

Model memorizes training data but performs badly on new data.

Signs
Train Accuracy = 99%
Test Accuracy = 60%
Fix
More data
Simpler model
Regularization
14. Underfitting

Model is too simple and performs badly everywhere.

15. Deployment

Save model:

import pickle

pickle.dump(model, open("model.pkl", "wb"))

Use with:

React + Flask
FastAPI
Django
Streamlit
16. Beginner Roadmap
Stage 1: Python Basics
Variables
Loops
Functions
Lists
Dictionaries
Stage 2: NumPy
Arrays
Indexing
Shape
Stage 3: Pandas
read_csv()
head()
info()
iloc()
loc()
Stage 4: Visualization
Scatter Plot
Histogram
Stage 5: ML Basics
train_test_split
fit()
predict()
accuracy_score()
Stage 6: Algorithms
Linear Regression
Logistic Regression
KNN
Tree Models
17. What to Learn Next

Since you already trained placement model:

Linear Regression
Logistic Regression deeply
Decision Tree
Feature Scaling
Confusion Matrix
Cross Validation
Hyperparameter Tuning
Deployment
18. Golden Rule
Data Quality > Fancy Algorithm
19. Job Ready Skills
Python
SQL
Pandas
Scikit-learn
Projects
Deployment
Statistics
Git
APIs
20. One Line Summary
Machine Learning = Learning patterns from old data to predict new data.