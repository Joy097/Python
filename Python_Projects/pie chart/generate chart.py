import matplotlib.pyplot as plt

# Data
x = ['A', 'B', 'C', 'D']
y = [10, 5, 20, 15]
colors = ['purple', 'teal', 'orange']


# Create a bar chart
plt.bar(x, y,color=colors)

# Create a line plot

# Set x and y axis limits
plt.xlim(-1, 4)
plt.ylim(0, 50)

# Set chart title and axis labels
plt.title('My Chart')
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)

# Save chart as PNG image
plt.savefig('my_chart1.png')
