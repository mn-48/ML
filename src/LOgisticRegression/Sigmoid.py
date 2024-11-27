import numpy as np
import matplotlib.pyplot as plt

# Sigmoid Function সংজ্ঞা
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# z এর মান এবং Sigmoid গণনা
z = np.linspace(-10, 10, 100)  # -10 থেকে 10 পর্যন্ত মান
sigmoid_values = sigmoid(z)

# গ্রাফ আঁকা
plt.plot(z, sigmoid_values, label='Sigmoid Function')
plt.title("Sigmoid Function")
plt.xlabel("z")
plt.ylabel("σ(z)")
plt.grid()
plt.legend()
plt.show()
