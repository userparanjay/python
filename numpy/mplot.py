import matplotlib.pyplot as plt  # Import matplotlib for plotting graphs

# ---------------- LINE PLOT (Basic Styling) ----------------
# x = [1,2,3,4]   # X-axis values
# y = [10,20,15,25]  # Y-axis values

# Plot line with styling options
# plt.plot(x, y,
#          color="red",              # Line color
#          linewidth=2,              # Thickness of line
#          linestyle="dashed",       # Line style
#          marker="o",               # Marker shape
#          markersize=10,            # Marker size
#          markerfacecolor="blue",   # Marker fill color
#          markeredgecolor="black")  # Marker border color

# Add title and labels
# plt.title("test")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")

# Save the plot as image
# plt.savefig("test.png")


# ---------------- MULTIPLE LINE PLOT ----------------
# a=[1,2,3]        # X-axis (Months)
# b=[10,20,30]     # Sales 2025
# c=[40,50,60]     # Sales 2026

# Plot two lines
# plt.plot(a,b,label="Sales 2025")
# plt.plot(a,c,label="Sales 2026")

# Labels and title
# plt.ylabel("Sales")
# plt.xlabel("Months")
# plt.title("Sales Data")

# Show legend (important for multiple lines)
# plt.legend()

# Save image
# plt.savefig("sales.png")


# ---------------- BAR CHART ----------------
# a=['A','B','C','D']   # Categories
# b=[10,20,30,40]      # Values

# plt.bar(a,b)         # Create bar chart
# plt.title('Bar Chart')
# plt.savefig("bar.png")


# ---------------- HISTOGRAM ----------------
# data = [10, 12, 15, 18, 20, 22, 25, 30]

# plt.hist(data,bins=5)   # Divide data into 5 bins
# plt.title('Histogram Chart')
# plt.savefig("histogram.png")


# ---------------- PIE CHART ----------------
# categories=['A','B','C','D']
# values=[15,30,45,10]

# plt.pie(values,
#         labels=categories,     # Labels for slices
#         autopct='%1.1f%%')     # Show percentage

# plt.title('Pie Chart')
# plt.savefig("pie.png")


# ---------------- SCATTER PLOT ----------------
# y1=[10,20,30,40,50]
# y2=[15,25,35,45,55]

# plt.scatter(y1,y2)   # Scatter plot

# plt.ylabel("Sales")
# plt.xlabel("Months")
# plt.title("Scatter Chart")

# plt.savefig("scatter.png")


# ---------------- SUBPLOTS (MULTIPLE CHARTS IN ONE FIGURE) ----------------
# a=['A','B','C','D']
# b=[10,20,30,40]

# y1=[10,20,30,40,50]
# y2=[15,25,35,45,55]

# plt.figure(figsize=(10,5))   # Set figure size

# First subplot (1 row, 2 columns, position 1)
# plt.subplot(1,2,1)
# plt.bar(a,b)
# plt.title('Bar Chart')

# Second subplot (position 2)
# plt.subplot(1,2,2)
# plt.scatter(y1,y2)

# plt.ylabel("Sales")
# plt.xlabel("Months")
# plt.title("Scatter Chart")

# plt.savefig("subplot.png")


# ---------------- USING PANDAS + MATPLOTLIB ----------------
import pandas as pd   # Import pandas for data handling

# Create dictionary (dataset)
data = {
    'Months': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'Sales': [150,200,250,300,350,400,450,500,550,600,650,700]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

print(df)  # Print the dataset

# Create bar chart using pandas data
plt.bar(data['Months'], data['Sales'])

# Add labels and title
plt.title('Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales')

# Save the graph as image
plt.savefig("bar_graph_by_pandas.png")