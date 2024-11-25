import matplotlib.pyplot as plt
import numpy as np
men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)
labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
num_groups = len(labels)
bar_width = 0.35
index = np.arange(num_groups)
plt.figure(figsize=(10, 6))
bar1 = plt.bar(index, men_means, bar_width, label='Men')
bar2 = plt.bar(index + bar_width, women_means, bar_width, label='Women')
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(index + bar_width / 2, labels)
plt.legend()
