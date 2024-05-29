import tensorflow as tf
import numpy as np
tf.__version__

# 影像的類別數目
category = 10
# 載入資料（將資料打散，放入 train 與 test 資料集）
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# 將原始資料轉為正確的影像排列方式
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
# 標準化輸入資料
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# 將數字轉為 One-hot 向量
y_train2 = tf.keras.utils.to_categorical(y_train, category)
y_test2 = tf.keras.utils.to_categorical(y_test, category)
print(y_train[0])
print("↧")
print(y_train2[0])

# 建立模型
model = tf.keras.models.Sequential()

# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), padding="same", activation='relu', input_shape=(28,28,1)))
model.add(tf.keras.layers.Conv2D(filters=40, kernel_size=(2, 2),padding="same", activation='relu'))
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))# 2D 的 Max-Pooling Layer
model.add(tf.keras.layers.Conv2D(filters=40, kernel_size=(2, 2),padding="same", activation='relu'))# 2D 的 Convolution Layer
model.add(tf.keras.layers.Dropout(rate=0.01))# Dropout Layer
model.add(tf.keras.layers.Flatten())# 將 2D 影像轉為 1D 向量
model.add(tf.keras.layers.Dense(100, activation='relu'))# 連接 Fully Connected Layer，接著一層 ReLU 的 Activation 函數
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax ))# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數

model.summary()
# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(loss=tf.keras.losses.categorical_crossentropy,
              optimizer=tf.keras.optimizers.Adam(lr=0.001),
              metrics=['accuracy'])

# 訓練模型
history=model.fit(x_train, y_train2,
          batch_size=1000,
          epochs=10)
#測試
score = model.evaluate(x_test, y_test2, batch_size=128)
# 輸出結果
print("score:",score)

predict = model.predict(x_test)
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))
print("y_test",y_test[:4])

import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('model accuracy')
plt.ylabel('acc & loss')
plt.xlabel('epoch')
plt.legend(['acc', 'loss'], loc='upper left')
plt.show()