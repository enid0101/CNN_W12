# CNN_W12
W12
2024-05-29 14:18:00.849835: I tensorflow/core/util/port.cc:113] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2024-05-29 14:18:02.523984: I tensorflow/core/util/port.cc:113] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
5
↧
[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
D:\X\.venv\Lib\site-packages\keras\src\layers\convolutional\base_conv.py:107: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
2024-05-29 14:18:08.682110: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
Model: "sequential"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ conv2d (Conv2D)                      │ (None, 28, 28, 32)          │             320 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ conv2d_1 (Conv2D)                    │ (None, 28, 28, 40)          │           5,160 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ max_pooling2d (MaxPooling2D)         │ (None, 14, 14, 40)          │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ conv2d_2 (Conv2D)                    │ (None, 14, 14, 40)          │           6,440 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dropout (Dropout)                    │ (None, 14, 14, 40)          │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ flatten (Flatten)                    │ (None, 7840)                │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense (Dense)                        │ (None, 100)                 │         784,100 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_1 (Dense)                      │ (None, 100)                 │          10,100 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_2 (Dense)                      │ (None, 100)                 │          10,100 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_3 (Dense)                      │ (None, 10)                  │           1,010 │
└──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
 Total params: 817,230 (3.12 MB)
 Trainable params: 817,230 (3.12 MB)
 Non-trainable params: 0 (0.00 B)
Epoch 1/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 44s 598ms/step - accuracy: 0.6560 - loss: 1.2451
Epoch 2/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 42s 635ms/step - accuracy: 0.9417 - loss: 0.1982
Epoch 3/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 41s 681ms/step - accuracy: 0.9716 - loss: 0.0941
Epoch 4/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 40s 670ms/step - accuracy: 0.9816 - loss: 0.0600
Epoch 5/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 36s 599ms/step - accuracy: 0.9860 - loss: 0.0458
Epoch 6/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 39s 649ms/step - accuracy: 0.9894 - loss: 0.0356
Epoch 7/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 46s 757ms/step - accuracy: 0.9914 - loss: 0.0283
Epoch 8/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 39s 652ms/step - accuracy: 0.9924 - loss: 0.0244
Epoch 9/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 38s 637ms/step - accuracy: 0.9938 - loss: 0.0205
Epoch 10/10
60/60 ━━━━━━━━━━━━━━━━━━━━ 38s 623ms/step - accuracy: 0.9942 - loss: 0.0178
79/79 ━━━━━━━━━━━━━━━━━━━━ 4s 29ms/step - accuracy: 0.9877 - loss: 0.0393
score: [0.03245158493518829, 0.989300012588501]
313/313 ━━━━━━━━━━━━━━━━━━━━ 3s 10ms/step   
Ans: 7 2 1 0
y_test [7 2 1 0]
