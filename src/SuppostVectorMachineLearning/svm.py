from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# ডেটাসেট লোড করা
iris = datasets.load_iris()
X = iris.data
y = iris.target

# ডেটা ভাগ করা
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# SVM মডেল তৈরি করা (RBF Kernel)
model = SVC(kernel='rbf', gamma='scale')
model.fit(X_train, y_train)

# পূর্বাভাস এবং একিউরেসি স্কোর
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
