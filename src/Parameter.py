import numpy as np
from sklearn.linear_model import LinearRegression

# ডেটা তৈরি
X = np.array([[1], [2], [3], [4]])  # ফিচার
y = np.array([3, 5, 7, 9])         # লক্ষ্য

# মডেল প্রশিক্ষণ
model = LinearRegression()
model.fit(X, y)

# প্যারামিটার (ওজন এবং বায়াস)
weight = model.coef_  # ওজন
bias = model.intercept_  # বায়াস

print("Weight (Coefficient):", weight)
print("Bias (Intercept):", bias)
