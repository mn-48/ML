# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# # উদাহরণ ডেটা
# data = {
#     "Size": [500, 1000, 1500, 2000, 2500],
#     "Location": [1, 2, 3, 4, 5],  # 1=City Outskirts, 5=City Center
#     "Price": [50, 120, 200, 300, 500]
# }

# df = pd.DataFrame(data)

# # Pairplot ব্যবহার
# sns.pairplot(df)
# plt.show()


# from sklearn.preprocessing import PolynomialFeatures

# # ডেটা
# X = [[1, 2], [2, 3], [3, 4]]
# poly = PolynomialFeatures(degree=2, interaction_only=True)
# X_poly = poly.fit_transform(X)

# print(X_poly)



# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# # উদাহরণ ডেটা
# X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # স্বাধীন ভেরিয়েবল
# Y = np.array([2, 4, 5, 4, 5])  # নির্ভরশীল ভেরিয়েবল

# # মডেল তৈরি
# model = LinearRegression()
# model.fit(X, Y)

# # ভবিষ্যদ্বাণী
# predictions = model.predict(X)

# # ফলাফল প্রদর্শন
# plt.scatter(X, Y, color='blue', label="Actual Data")
# plt.plot(X, predictions, color='red', label="Regression Line")
# plt.legend()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# ডেটা
data = {
    'Group': ['A', 'A', 'B', 'B'],
    'Treatment': ['Yes', 'No', 'Yes', 'No'],
    'Success Rate': [90, 80, 60, 50]
}

df = pd.DataFrame(data)

# বার গ্রাফ
plt.bar(df['Group'] + " (" + df['Treatment'] + ")", df['Success Rate'], color=['blue', 'orange', 'blue', 'orange'])
plt.ylabel("Success Rate")
plt.title("Simpson's Paradox Example")
plt.show()
