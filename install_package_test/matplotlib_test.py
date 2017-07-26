import numpy as np
import matplotlib.pyplot as plt
# Generate a sequence of integers
x = np.arange(20)
# create a second array using sinus
y = np.sin(x)
# The plot function makes a line chart of one array against another
plt.plot(x, y, marker="x")
# plt.show() # to show multiple plot
z = np.cos(x)
plt.figure() # to show multiple plot
plt.plot(x, z, marker="o")
plt.show()
