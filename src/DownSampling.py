import pandas as pd
from sklearn.utils import resample

# ডেটাসেট তৈরি
data = pd.DataFrame({
    'feature': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'class': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']
})

# মেজরিটি এবং মাইনরিটি ক্লাস বিভক্ত করা
majority_class = data[data['class'] == 'A']
minority_class = data[data['class'] == 'B']

# Down Sampling
downsampled_majority = resample(majority_class, 
                                replace=False, # ডেটা পুনরাবৃত্তি নয়
                                n_samples=len(minority_class), # মাইনরিটি ক্লাসের সমান সংখ্যা
                                random_state=42)

# নতুন ডেটাসেট তৈরি
balanced_data = pd.concat([downsampled_majority, minority_class])
print(balanced_data)
