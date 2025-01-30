import random

n = 42
# Seed সেট করার আগে
random.seed(n)
print(random.randint(1, 100))  # Output: 81
print(random.randint(1, 100))  # Output: 14
# print(random.randint(1, 100))  # Output: 14
print()
print()
# আবার একই seed ব্যবহার
random.seed(n)
print(random.randint(1, 100))  # Output: 81
print(random.randint(1, 100))  # Output: 14
print(random.randint(1, 100))  # Output: 14
print(random.randint(1, 100))  # Output: 14
print(random.randint(1, 100))  # Output: 14
print(random.randint(1, 100))  # Output: 14
print()
print()
random.seed(n)
print(random.randint(1, 100))  # Output: 81
print(random.randint(1, 100))  # Output: 14
print(random.randint(1, 100))  # Output: 14
print()
print()
