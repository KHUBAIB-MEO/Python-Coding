import numpy as np
import matplotlib.pyplot as plt 
import tensorflow as tf
import os
import seaborn as sn
from sklearn.metrics import confusion_matrix

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
model.fit(x_train, y_train, epochs = 1)
#model.save('KHUBAIB_model.keras')
#model = tf.keras.models.load_model('KHUBAIB_model.keras')
y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)
cm = confusion_matrix(y_test, y_pred_classes)
plt.figure(figsize=(10, 8))
sn.heatmap(cm, annot=True, fmt='d', cmap="Blues",
    linewidths=.5,
    linecolor="lightgray",
    cbar_kws={"shrink": 0.8})
plt.title('Confusion Matrix')
plt.ylabel('Truth')
plt.xlabel('Predicted')
plt.show()