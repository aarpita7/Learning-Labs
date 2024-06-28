# Matplotlib
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

import matplotlib.pyplot as plt

# Basic Plotting
# Creating a simple line plot

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Creating a plot
plt.plot(x, y)
plt.title('Basic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()

# Plotting with Labels and Titles
# Adding labels and titles to the plot

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Creating a plot with labels and title
plt.plot(x, y, label='Quadratic')
plt.title('Line Plot with Labels and Title')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Display the plot
plt.show()

# Plotting Multiple Lines
# Creating a plot with multiple lines

# Data for plotting
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]

# Creating a plot with multiple lines
plt.plot(x, y1, label='Prime Numbers')
plt.plot(x, y2, label='Square Numbers')
plt.title('Multiple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Display the plot
plt.show()


# Summary
# - Matplotlib is a powerful library for creating various types of plots and visualizations in Python.
# - Basic plotting includes line plots, bar plots, and scatter plots.

