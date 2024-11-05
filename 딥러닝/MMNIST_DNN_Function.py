import sys
from tensorflow import keras
import sklearn
import tensorflow as tf
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import time


#class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
#               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

#print(class_names)


def load_data():
    # 먼저 MNIST 데이터셋을 로드
    # 28*28 - 0~255로 진행 - keras 데이터로 (sklearn 데이터 x)
    # fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
    (X_train_full, y_train_full), (
    X_test, y_test) = tf.keras.datasets.mnist.load_data()  # 훈련 세트는 60,000개의 흑백 이미지입니다. 각 이미지의 크기는 28x28 픽셀입니다:
    return X_train_full, y_train_full, X_test, y_test


def data_normalization(X_train_full, y_train_full, X_test):
    # 전체 훈련 세트를 검증 세트와 (조금 더 작은) 훈련 세트로 나누어 보죠. 또한 픽셀 강도를 255로 나누어 0~1 범위의 실수로 바꾸겠습니다.

    # 2. 0~255 기존과 0~1 정규화한 결과 비교 - 초기화 동일한 조건
    X_valid, X_train = X_train_full[:5000] / 255., X_train_full[5000:] / 255.
    y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
    X_test = X_test / 255.

    return X_valid, X_train, y_valid, y_train, X_test


# def show_oneimg(X_train):
#     # 맷플롯립의 `imshow()` 함수와 `'binary'` 컬러맵을 사용해 이미지를 출력할 수 있습니다:
#     plt.figure()
#     plt.imshow(X_train[0], cmap="binary")
#     plt.axis('off')


# def show_40images(X_train, y_train):
#     # 이 데이터셋에 있는 샘플 이미지를 몇 개 출력해 보죠:
#     n_rows = 4
#     n_cols = 10
#     plt.figure(figsize=(n_cols * 1.2, n_rows * 1.2))
#     for row in range(n_rows):
#         for col in range(n_cols):
#             index = n_cols * row + col
#             plt.subplot(n_rows, n_cols, index + 1)
#             plt.imshow(X_train[index], cmap="binary", interpolation="nearest")
#             plt.axis('off')
#             plt.title(class_names[y_train[index]], fontsize=12)
#     plt.subplots_adjust(wspace=0.2, hspace=0.5)
#     plt.show()


def makemodel(X_train, y_train, X_valid, y_valid):
    model = keras.models.Sequential()
    # 0. train, test 8:2 분리하기
    # 1. 가중치 초기화 지정 - Random or Xavier
    # 3. dropout 여부 
    model.add(keras.layers.Flatten(input_shape=[28, 28]))
    model.add(keras.layers.Dense(300, activation="relu"))
    model.add(keras.layers.Dense(100, activation="relu"))
    model.add(keras.layers.Dense(10, activation="softmax"))

    model.summary()

    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="sgd",
                  metrics=["accuracy"])

    # 위 코드는 다음과 같음

    # ```python
    # model.compile(loss=keras.losses.sparse_categorical_crossentropy,
    #               optimizer=keras.optimizers.SGD(),
    #               metrics=[keras.metrics.sparse_categorical_accuracy])
    # ```

    # 시간 측정
    tb_hist = keras.callbacks.TensorBoard(log_dir='./graph', histogram_freq=0, write_graph=True, write_images=True)
    start = time.time()
    history = model.fit(X_train, y_train, epochs=100,
                        validation_data=(X_valid, y_valid), callbacks=[tb_hist])
    print("time :", time.time() - start)
    return model, history


def evalmodel(model, history, X_test, y_test):
    model.evaluate(X_test, y_test)

    X_new = X_test[:3]
    y_proba = model.predict(X_new)
    y_proba.round(2)

    # y_pred = model.predict_classes(X_new)
    # y_pred

    # plt.figure(figsize=(7.2, 2.4))
    # for index, image in enumerate(X_new):
    #     plt.subplot(1, 3, index + 1)
    #     plt.imshow(image, cmap="binary", interpolation="nearest")
    #     plt.axis('off')
    #     plt.title(class_names[y_test[index]], fontsize=12)
    # plt.subplots_adjust(wspace=0.2, hspace=0.5)

    # pd.DataFrame(history.history).plot(figsize=(8, 5))
    # plt.grid(True)
    # plt.gca().set_ylim(0, 1)
    # save_fig("keras_learning_curves_plot")
    # plt.show()
    # plt.show()


def main():
    X_train_full, y_train_full, X_test, y_test = load_data()

    X_valid, X_train, y_valid, y_train, X_test = data_normalization(X_train_full, y_train_full, X_test)
    #show_oneimg(X_train)
    #show_40images(X_train, y_train)
    model, history = makemodel(X_train, y_train, X_valid, y_valid)
    evalmodel(model, history, X_test, y_test)
    plt.show()


main()
