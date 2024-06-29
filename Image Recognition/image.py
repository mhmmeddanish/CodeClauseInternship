import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
import numpy as np

# Step 1: Load the Dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Step 2: Preprocess the Data
x_train, x_test = x_train / 255.0, x_test / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Step 3: Define the CNN Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Step 4: Train the Model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Step 5: Evaluate the Model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# Step 6: Save the Model
model.save('cifar10_cnn_model.h5')

# Step 7: Load the Model and Make Predictions
def predict(image):
    # Preprocess the image
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    
    # Get the prediction
    prediction = model.predict(image)
    return np.argmax(prediction, axis=1)

# Example: Predict the class of the first test image
predicted_class = predict(x_test[0])
print(f'Predicted class: {predicted_class}')
