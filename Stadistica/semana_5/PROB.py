
for simulations in range(0, 10):
    count = 0
    tosses = np.random.randint(2, size=4000)
    P_heads = []
    
    for i in range(1, 4001):
        index1 = [j for j in range(0, i) if tosses[j] == 1]
        P_heads.append(len(index1) / i)
        
    plt.xlabel('Number of iterations', fontsize=24)
    plt.ylabel('Probability', fontsize=24)
    plt.plot(np.arange(1, 4001), P_heads[0:4000])
    plt.gcf().set_size_inches(20, 10)
    plt.gca().set_xlim([1, 4000])
    plt.xticks(np.arange(400, 4001, 400), fontsize=20)
    plt.yticks(fontsize=20)
plt.plot(range(0, 4000), [1 / 2] * 4000, 'k', linewidth=5.0, label = 'Theoretical probability')
plt.legend(fontsize=20)
plt.show()
