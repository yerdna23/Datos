import math
import numpy as np
import ipywidgets as widgets

count = 0
Outcomes = 1 + np.random.randint(6, size = 10000)
P_A = []

for i in range(1, 10001):
    outcomes_trunc = Outcomes[0:i]
    index_A = [j for j in range(0, i) if outcomes_trunc[j] == 2]
    P_A.append(len(index_A) / i)

def probability_plot(n):
    outcomes_n = Outcomes[0:n]
    index_A_n = [z for z in index_A if z < n]
    
    s = [u'x'] * len(index_A_n)
    col = ['r'] * len(index_A_n)
    S = [320] * len(index_A_n)
    y = [2] * len(index_A_n)
    x = np.array(index_A_n) + np.array([1] * len(index_A_n))
    for _s, c, _x, _y, _S in zip(s, col, x, y, S):
        plt.scatter(_x, _y, marker=_s, c=c, s=_S)

    plt.plot(range(1, n + 1), outcomes_n, 'k.', markersize = 10.0)

    axes = plt.gca()
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    plt.xticks(fontsize = 18)
    plt.yticks(fontsize = 18)
    xint = []
    locs, labels = plt.xticks()
    for each in locs:
        xint.append(int(each))
    plt.xticks(xint)
    plt.xlabel('Number of Iterations', fontsize = 18)
    plt.ylabel('Outcomes', fontsize = 18)
    axes.set_xlim([0.5, n+0.5])
    axes.set_ylim([0, 7])
    plt.show()
    axes = plt.gca()
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    plt.plot(range(0, 10000), [1 / 6] * 10000, 'b', linewidth=5.0, label='Theoretical probability')
    axes.set_xlim([0, n + 1])
    plt.plot(np.arange(1, n + 1), P_A[0:n], 'k-', linewidth=3.0, label='Empirical probability')
    xint = []
    locs, labels = plt.xticks()
    for each in locs:
        xint.append(int(each))
    plt.xticks(xint, fontsize = 18)
    plt.yticks(fontsize=18)
    plt.xlabel('Number of Iterations', fontsize = 18)
    plt.ylabel('Probability', fontsize = 18)
    axes = plt.gca()
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    axes.set_xlim([1, n])
    axes.set_ylim([min(P_A), 1])
    plt.legend(fontsize = 20)
    plt.show()


widgets.interact(
    probability_plot,
    n=widgets.IntSlider(min=10, max=10000, value = 1000,
    continuous_update=False))
