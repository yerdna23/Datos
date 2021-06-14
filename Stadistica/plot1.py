import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import ipywidgets as widgets

def f(x_max):
    x = np.arange(0, x_max, 0.01)
    plt.plot(x, x, 'b', linewidth = 3, label = '$x$')
    plt.plot(x, x**2, 'r', linewidth = 3, label = '$x^2$')
    plt.plot(x, 2**x, 'm', linewidth = 3, label = '$2^x$')
    plt.xlabel('x', fontsize = 20)
    plt.xticks(fontsize = 18)
    plt.yticks(np.linspace(max(2**x_max, x_max**2)/10, max(2**x_max, x_max**2), 10), fontsize = 18)
    plt.gca().set_xlim([0, x_max])
    plt.gca().set_ylim([0, max(2**x_max, x_max**2)])
    plt.gcf().set_size_inches(20, 10)
    plt.legend(fontsize = 20)
    plt.show()
    
widgets.interact(f, x_max=widgets.FloatSlider(min = 0.5, max = 20, step = 0.5))
