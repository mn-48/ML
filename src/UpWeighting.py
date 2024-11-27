from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.class_weight import compute_class_weight
import numpy as np
# ডেটাসেট প্রস্তুত করা
X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]  # 0 = মেজরিটি, 1 = মাইনরিটি

# ক্লাসের ওয়েট বের করা
class_weights = compute_class_weight(class_weight='balanced', classes=np.array([0, 1]), y=y)


# class_weights = compute_class_weight(class_weight = "balanced", classes= np.unique(y), y= y)

# মডেল তৈরি করা
model = RandomForestClassifier(class_weight={0: class_weights[0], 1: class_weights[1]})
model.fit(X, y)

print("Class Weights:", class_weights)
