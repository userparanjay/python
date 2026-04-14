import numpy as np

# -------------------------------
# Creating a NumPy array
# -------------------------------
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", a)

# -------------------------------
# Basic properties of array
# -------------------------------
print("Dimensions (ndim):", a.ndim)        # Number of dimensions
print("Shape:", a.shape)                  # (rows, columns)
print("Size:", a.size)                    # Total number of elements
print("Data type:", a.dtype)              # Type of elements
print("Type of object:", type(a))         # Should be numpy.ndarray
print("Item size (bytes):", a.itemsize)   # Size of each element in bytes
print("Total bytes:", a.nbytes)           # Total memory used

# -------------------------------
# Indexing and slicing
# -------------------------------
print("Element at [1, -2]:", a[1, -2])    # Row 1, second last column
print("First row:", a[0, :])              # All columns of first row
print("Third column:", a[:, 2])           # All rows of 3rd column

# -------------------------------
# Creating arrays with defaults
# -------------------------------
x = np.zeros((2, 3))                      # 2x3 array filled with 0
print("Zeros array:\n", x)

y = np.ones((2, 3))                       # 2x3 array filled with 1
print("Ones array:\n", y)

z = np.full((2, 3), 99)                   # 2x3 array filled with 99
print("Full array (99):\n", z)

q = np.eye(3)                             # Identity matrix (3x3)
print("Identity matrix:\n", q)

# -------------------------------
# Special array creation
# -------------------------------
print("Empty array:", np.empty(2))        # Uninitialized (garbage values)

print("Arange:", np.arange(1, 10, 2))     # Start=1, Stop=10, Step=2

print("Linspace:", np.linspace(1, 10, 4)) # 4 evenly spaced values

# -------------------------------
# Random values
# -------------------------------
print("Random float array:", np.random.rand(1, 2))       # Values between 0 and 1

print("Random int array:", np.random.randint(1, 10, (2, 3)))  # Integers between 1–9

print("???????????????????????????????????????????????????????????????????????????")
x=[[1,2,3],[4,5,6]]
print(x[1])
print(x[:,0])