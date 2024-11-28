'''
data poinits = 1000
if 1 batch = 10 data points 
1 epoch = (1000/10) batch =100 batch 
'''



from sklearn.datasets import make_regression
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split

# ডেটাসেট তৈরি করা
X, y = make_regression(n_samples=1000, n_features=1, noise=10)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# মডেল তৈরি করা
model = SGDRegressor(max_iter=100, warm_start=True)

# 5 Epoch-এর জন্য ট্রেনিং করা
for epoch in range(5):
    model.fit(X_train, y_train)
    print(f"Epoch {epoch+1}: Training complete")
