import numpy as np
import statsmodels.api as sm

# ডামি ডেটা তৈরি করা
X = np.random.rand(100, 2)  # ফিচার
y = np.random.randint(0, 2, 100)  # বাইনারি টার্গেট

# মডেল ফিট করা
X = sm.add_constant(X)  # ইন্টারসেপ্ট যোগ করা
model = sm.Logit(y, X).fit()

# মডেল সারাংশ
print(model.summary())

# McFadden's Pseudo R^2
pseudo_r2 = 1 - (model.llf / model.llnull)
print(f"McFadden's Pseudo R^2: {pseudo_r2}")
