
# MultinomialNB
# BernoulliNB
# GaussianNB

# prerequisite
'''
Python(list comprehension, basic OOP)
Numpy(broadcasting)
Basic Linear Algebra
Probability(gaussian distribution)
'''

# # MultinomialNB ------------------------------------
# from sklearn.naive_bayes import MultinomialNB

# # উদাহরণ ডেটা
# X = [[2, 1], [1, 1], [2, 0], [0, 1]]  # প্রতিটি ইমেইলে শব্দের সংখ্যা
# y = [1, 1, 0, 0]  # শ্রেণী লেবেল: 1 = স্প্যাম, 0 = নন-স্প্যাম

# model = MultinomialNB()
# model.fit(X, y)

# # নতুন ডেটা প্রেডিকশন
# print(model.predict([[1, 0]]))  # প্রেডিকশন করে দেখায় ইমেইলটি স্প্যাম কিনা


# # BernoulliNB ------------------------------------
# from sklearn.naive_bayes import BernoulliNB

# # উদাহরণ ডেটা
# X = [[1, 0], [1, 1]]  # "অফার" এবং "বিনামূল্যে" এর উপস্থিতি
# y = [1, 0]  # শ্রেণী লেবেল: 1 = স্প্যাম, 0 = নন-স্প্যাম

# model = BernoulliNB()
# model.fit(X, y)


# print(model.predict([[1, 1]]))  # প্রেডিকশন করে দেখায় ইমেইলটি স্প্যাম কিনা


# GaussianNB -------------------------------------------
from sklearn.naive_bayes import GaussianNB

# উদাহরণ ডেটা
X = [[180, 80], [160, 55], [170, 50]]  # উচ্চতা ও ওজন
y = [1, 0, 1]  # শ্রেণী লেবেল: 1 = পুরুষ, 0 = নারী

model = GaussianNB()
model.fit(X, y)
print(model.predict([[170, 67]]))