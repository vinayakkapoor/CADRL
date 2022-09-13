import matplotlib.pyplot as plt

epsilon_decay = 750
episodes = 1000
epsilon_start = 0.5
epsilon_end = 0.1
epsilon = []

for i in range(1,episodes+1):
    epsilon.append(epsilon_start + (epsilon_end - epsilon_start) / epsilon_decay * i)
    
plt.plot(range(1,episodes+1), epsilon)
plt.ylim([0,1])
plt.show()