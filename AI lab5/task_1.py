import cv2  # type: ignore
import numpy as np
import matplotlib.pyplot as plt # type: ignore
import tensorflow as tf # type: ignore
import os

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape = (28,28)))
model.add(tf.keras.layers.Dense(units = 128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(units = 128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(units = 10, activation = tf.nn.softmax))
model.compile(optimizer = 'adam', 
loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
model.fit(x_train, y_train, epochs = 10)


image_number = 1
while os.path.isfile(f"digits/digit{image_number}.png"):
    img = cv2.imread(f"digits/digit{image_number}.png")[:, :, 0]
    img=np.invert(np.array([img]))
    prediction = model.predict(img)
    print("The Digit Becomes : ",np.argmax(prediction))
    plt.imshow(img[0],cmap = plt.cm.binary)
    plt.show()
    image_number += 1
