from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5]]
y = [0, 1, 0, 1, 0]

# `random_state` ছাড়া
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print("Without random_state:")
print("X_train:", X_train)
print("X_test:", X_test)

# `random_state` সহ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("\nWith random_state=42:")
print("X_train:", X_train)
print("X_test:", X_test)
