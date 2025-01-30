import numpy as np
import matplotlib.pyplot as plt

# ডাটা সেট তৈরি করা
X = np.array([1, 2, 3, 4, 5])  # ইনপুট ফিচার
y = np.array([2, 3, 4, 5, 6])  # আসল আউটপুট

# ইনিশিয়ালাইজ করব
theta0 = 0   # ইন্টারসেপ্ট (bias)
theta1 = 0   # স্লোপ (weight)
alpha = 0.01  # লার্নিং রেট
epochs = 1000  # ইটারেশনের সংখ্যা
m = len(X)  # মোট ডাটা পয়েন্ট সংখ্যা

# গ্রেডিয়েন্ট ডিসেন্ট ইমপ্লিমেন্টেশন
for _ in range(epochs):
    y_pred = theta0 + theta1 * X  # বর্তমান প্রেডিকশন
    error = y_pred - y  # ভুলের পরিমাণ

    # গ্রেডিয়েন্ট (ঢাল) বের করা
    d_theta0 = (1/m) * np.sum(error)
    d_theta1 = (1/m) * np.sum(error * X)

    # আপডেটিং ফর্মুলা
    theta0 = theta0 - alpha * d_theta0
    theta1 = theta1 - alpha * d_theta1

# প্রেডিকশন লাইন আঁকা
plt.scatter(X, y, color='red', label='Actual Data')  # আসল ডাটা
plt.plot(X, theta0 + theta1 * X, color='blue',
         label='Predicted Line')  # প্রেডিকশন লাইন
plt.xlabel("X (Input Feature)")
plt.ylabel("y (Output)")
plt.legend()
"""_summary_
    """
plt.title("Gradient Descent for Linear Regression")
plt.show()

# ফাইনাল থেটা ভ্যালু প্রিন্ট করা
print(f"Final theta0: {theta0:.4f}, Final theta1: {theta1:.4f}")
