import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ডেটা তৈরি (উদাহরণস্বরূপ)
data = pd.DataFrame({
    'Age': [25, 34, 28, 52, 46, 30, 40, 23, 36, 50],
    'Income': [40000, 60000, 50000, 80000, 70000, 58000, 62000, 45000, 75000, 90000],
    'Car_Type': ['SUV', 'Sedan', 'SUV', 'Truck', 'Truck', 'SUV', 'Sedan', 'SUV', 'Truck', 'Sedan']
})

# print(data)

# ফিচার এবং লেবেল বিভাজন
X = data[['Age', 'Income']]
y = data['Car_Type']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Multinomial Logistic Regression মডেল
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)

# প্রেডিকশন
y_pred = model.predict(X_test)

# ফলাফল
print("Classification Report:")
print(classification_report(y_test, y_pred))
