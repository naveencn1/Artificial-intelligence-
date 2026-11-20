# CSA17 - Artificial Intelligence | Experiment 34 (Manual Ex. 4.4): Neural Network for Image Classification (TensorFlow / Keras)
# Name            : V V Naveen Kumar
# Register Number : 192321018

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train[..., np.newaxis] / 255.0
x_test = x_test[..., np.newaxis] / 255.0

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax'),
])
model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train, epochs=3, batch_size=64, validation_split=0.1)

loss, acc = model.evaluate(x_test, y_test, verbose=0)
print("Test accuracy: %.4f" % acc)
probs = model.predict(x_test[:1])
print("Predicted digit:", int(np.argmax(probs)), "| Actual digit:", int(y_test[0]))


# ============================================================
# OUTPUT
# ============================================================
# [NOT EXECUTED HERE - requires TensorFlow + internet (MNIST download)]
# [Sample output reproduced from the lab manual; exact numbers vary per run]
#
# Epoch 1/3 loss: 0.2300 - accuracy: 0.9300 - val_accuracy: 0.9800
# Epoch 2/3 loss: 0.0600 - accuracy: 0.9810 - val_accuracy: 0.9850
# Epoch 3/3 loss: 0.0420 - accuracy: 0.9870 - val_accuracy: 0.9870
# Test accuracy: 0.9880
# Predicted digit: 7 | Actual digit: 7
