import tensorflow as tf
import numpy as np

# Input array
arr = np.array([
    [1, 2],
    [3, 4]
])

# Add a batch dimension (batch size = 1)
arr = np.expand_dims(arr, axis=0)  # Shape becomes (1, 2, 2)

# Create a Flatten layer
flatten_layer = tf.keras.layers.Flatten()

# Apply the Flatten layer
output_data = flatten_layer(arr)

# Print the output
print(output_data.numpy())

output_data = np.squeeze(output_data.numpy())
print(output_data)