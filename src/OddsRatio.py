import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ডেটা তৈরি
data = pd.DataFrame({
    'Treatment': [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # 1 = ওষুধ নিয়েছে, 0 = নেয়নি
    'Outcome': [1, 1, 1, 1, 1, 0, 0, 1, 0, 1]   # 1 = ভালো হয়েছে, 0 = হয়নি
})

# ফিচার এবং টার্গেট
X = data[['Treatment']]
y = data['Outcome']

# লজিস্টিক রিগ্রেশন
model = LogisticRegression()
model.fit(X, y)

# Coefficient থেকে Odds Ratio বের করা
odds_ratio = np.exp(model.coef_[0][0])
print(f"Odds Ratio: {odds_ratio}")
