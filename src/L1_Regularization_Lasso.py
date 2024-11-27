from sklearn.linear_model import Lasso
# from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# ডেটাসেট তৈরি করা
X = np.random.rand(100, 5)
y = np.random.rand(100)

# ডেটা ভাগ করা
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Lasso Regression
model = Lasso(alpha=0.1)  # L1 Regularization
model.fit(X_train, y_train)

# প্রেডিকশন
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
