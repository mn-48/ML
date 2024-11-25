
'''
Cross-Entropy Loss-এর ব্যবহার
_________________________________

    Logistic Regression:
        Binary Classification সমস্যায় ক্ষতি নির্ধারণ করতে ব্যবহৃত হয়।

    Neural Networks:
        মাল্টি-ক্লাস সমস্যায় Softmax Activation Function এর সাথে Cross-Entropy Loss ব্যবহার হয়।

    Deep Learning Models:
        এটি আধুনিক শ্রেণিবিন্যাস মডেলের মানসম্মত ক্ষতি ফাংশন।

'''


import numpy as np

# প্রকৃত লেবেল (One-hot Encoding)
y_true = np.array([1, 0, 0])  # প্রকৃত ক্লাস 0

# মডেলের ভবিষ্যদ্বাণীকৃত সম্ভাবনা
y_pred = np.array([0.7, 0.2, 0.1])  # ক্লাস 0, 1, 2 এর জন্য

# Cross-Entropy Loss ফাংশন
def cross_entropy_loss(y_true, y_pred):
    # ছোট মান এড়াতে log-এর মধ্যে epsilon যোগ করা হয়
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.sum(y_true * np.log(y_pred))

# লস গণনা
loss = cross_entropy_loss(y_true, y_pred)
print("Cross-Entropy Loss:", loss)


