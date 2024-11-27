import numpy as np

# লস ফাংশন (উদাহরণ)
def loss_function(w):
    return w**2 - 4*w + 4

# লস ফাংশনের গ্রেডিয়েন্ট
def gradient(w):
    return 2*w - 4

# লার্নিং রেট
learning_rate = 0.1
epochs = 20

# প্রাথমিক ওজন (initial weight)
w = 0.0

# গ্রেডিয়েন্ট ডিসেন্ট অ্যালগরিদম
for epoch in range(epochs):
    grad = gradient(w)
    w = w - learning_rate * grad
    print(f"Epoch {epoch+1}: Weight = {w}, Loss = {loss_function(w)}")
