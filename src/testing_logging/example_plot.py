import matplotlib.pyplot as plt
import numpy as np
import logging

def plot():

    # Generate some data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a plot
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')

    # Show the plot
    plt.show()
