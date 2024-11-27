from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# ডেটাসেট লোড করা
data = load_iris()
X = data.data
y = data.target

# ডেটা ভাগ করা
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Logistic Regression মডেল তৈরি
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Accuracy পরীক্ষা
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")
