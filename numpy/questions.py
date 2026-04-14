import numpy as np   # Import NumPy library for numerical operations

# ---------------- ARRAY CREATION ----------------
x = np.array([1,2,3,4,5,6,7,8,9,10])   # Create a 1D array

y = np.zeros((3,3))   # Create a 3x3 matrix filled with zeros

w = np.ones((2,4))    # Create a 2x4 matrix filled with ones

t = np.arange(10,50,2)  # Create array from 10 to 50 with step 2

# ---------------- ARRAY INDEXING ----------------
a = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

a = np.array([10, 20, 30, 40, 50])  # 1D array

# Access elements using index
print(a[0], a[-1], a[1:3])  
# a[0] -> first element
# a[-1] -> last element
# a[1:3] -> elements from index 1 to 2

# ---------------- 2D ARRAY SLICING ----------------
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(a[1,1], a[2,:], a[:,2])

# a[1,1] -> element at row 1 column 1
# a[2,:] -> entire third row
# a[:,2] -> entire third column

# ---------------- ARRAY OPERATIONS ----------------
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)  # Element-wise addition
print(a*b)  # Element-wise multiplication

# ---------------- MATHEMATICAL FUNCTIONS ----------------
print(np.sqrt(a))   # Square root of each element
print(np.mean(a))   # Mean (average)
print(np.std(a))    # Standard deviation
print(np.median(a)) # Median value

# ---------------- RESHAPING ARRAYS ----------------
a = np.array([1,2,3,4,5,6])

print(a.reshape(2,3))  # Convert 1D array into 2x3 matrix

# ---------------- FLATTEN ARRAY ----------------
x = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])

print(x.flatten())  # Convert 2D array to 1D array

# ---------------- MATRIX MULTIPLICATION ----------------
a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

print(np.dot(a,b))  # Matrix multiplication

# ---------------- BOOLEAN FILTERING ----------------
a = np.array([10, 15, 20, 25, 30])
b = np.array([1,2,3,4,5])

# Replace even numbers with 0
b[b % 2 == 0] = 0

# Filter elements greater than 20
print(a[a > 20], b)

# print(x,y,w,a)  # Uncomment to print all arrays