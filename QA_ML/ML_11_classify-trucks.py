# import tensorflow as tf
# import numpy as np
# from tensorflow.keras.preprocessing import image

# # Define the CNN Model
# def classify_trucks():
#     model = tf.keras.models.Sequential(
#         [
#             tf.keras.layers.Conv2D(
#                 16, (3, 3), activation="relu", input_shape=(224, 224, 3), kernel_initializer="he_normal"
#             ),
#             tf.keras.layers.MaxPooling2D((2, 2)),
#             tf.keras.layers.Conv2D(32, (3, 3), activation="relu", kernel_initializer="he_normal"),
#             tf.keras.layers.MaxPooling2D((2, 2)),
#             tf.keras.layers.Conv2D(64, (3, 3), activation="relu", kernel_initializer="he_normal"),
#             tf.keras.layers.Flatten(),
#             tf.keras.layers.Dense(20, activation="relu", kernel_initializer="he_normal"),
#             tf.keras.layers.Dense(1, activation="sigmoid", kernel_initializer="glorot_normal"),
#         ]
#     )

#     model.compile(
#         optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
#         loss=tf.keras.losses.BinaryCrossentropy(),
#         metrics=["binary_accuracy"],
#     )

#     return model

# # Load or Train the Model
# try:
#     model = tf.keras.models.load_model("model.h5")  # Load pre-trained model if available
#     print("Model loaded successfully!")
# except:
#     model = classify_trucks()  # If model is not found, create a new one
#     print("New model created!")

# # Function to Predict on a New Image
# def predict_truck(image_path):
#     # Load and preprocess the image
#     img = image.load_img(image_path, target_size=(224, 224))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array = img_array / 255.0  # Normalize the image

#     # Predict using the trained model
#     prediction = model.predict(img_array)
    
#     # Interpretation of the prediction
#     if prediction[0][0] >= 0.5:
#         print("🚛 Truck detected!")
#     else:
#         print("❌ No truck detected.")

# # Predict on "my-image.jpg"
# # predict_truck("my-image.jpg")
# predict_truck("dusk.jpg")

# # Save the model for future use
# model.save("model.h5")



import tensorflow as tf

def classify_trucks():
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Conv2D(16, (3,3), activation="relu", input_shape=(224, 224, 3), kernel_initializer="he_normal"),
            tf.keras.layers.MaxPooling2D((2,2)),
            tf.keras.layers.Conv2D(32, (3,3), activation="relu", kernel_initializer="he_normal"),
            tf.keras.layers.MaxPooling2D((2,2)),
            tf.keras.layers.Conv2D(64, (3,3), activation="relu", kernel_initializer="he_normal"),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(20, activation="relu", kernel_initializer="he_normal"),
            tf.keras.layers.Dense(1, activation="sigmoid", kernel_initializer="glorot_normal")
        ]
    )

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
        loss=tf.keras.losses.BinaryCrossentropy(),
        metrics=["binary_accuracy"],
    )

    return model






