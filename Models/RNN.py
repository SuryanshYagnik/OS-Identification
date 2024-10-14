import tensorflow as tf
from tensorflow.keras import layers, models

# Model Definition
rnn_model = models.Sequential([
    layers.SimpleRNN(128, input_shape=(10, X.shape[2]), activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # Adjust for number of classes
])

# Compile Model
rnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
