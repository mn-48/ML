import numpy as np

# লস ফাংশন: J(theta) = theta^2
def loss(theta):
    return theta**2

# গ্রেডিয়েন্ট: dJ(theta)/dtheta = 2 * theta
def gradient(theta):
    return 2 * theta

# Gradient Descent Function
def gradient_descent(starting_theta, learning_rate, iterations):
    theta = starting_theta
    for i in range(iterations):
        grad = gradient(theta)  # গ্রেডিয়েন্ট বের করা
        theta -= learning_rate * grad  # প্যারামিটার আপডেট
        print(f"Iteration {i+1}: Theta = {theta}, Loss = {loss(theta)}")
    return theta

# উদাহরণ: শুরুতে theta = 2.0, eta = 0.1, 10 iterations
final_theta = gradient_descent(starting_theta=2.0, learning_rate=0.1, iterations=10)
