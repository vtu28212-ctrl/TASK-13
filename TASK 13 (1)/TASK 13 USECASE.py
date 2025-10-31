import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11, 1)
p = 0.5
probabilities = [p**k * (1-p)**(10-k) for k in x]

plt.plot(x, probabilities, marker='o', linestyle='-', color='blue', label='Probability')
plt.title("Plotting Probabilities using Matplotlib")
plt.xlabel("Event Occurrence (k)")
plt.ylabel("Probability")
plt.grid(True)
plt.legend()
plt.show()
