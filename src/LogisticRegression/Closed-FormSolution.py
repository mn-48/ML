import numpy as np

# ডেটা তৈরি
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.array([6, 8, 9, 11])

# Closed-form solution
X_transpose = X.T
weights = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)

print("Weights:", weights)
