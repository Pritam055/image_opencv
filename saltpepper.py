import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random


def salt_n_pepper():
    img = cv.imread("train.jfif", cv.IMREAD_COLOR)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    rows, columns, channels = img.shape
    p = 0.05
    # p is probability of the occurence of the pixel

    output = np.zeros((rows, columns, channels), np.uint8)
    for i in range(rows):
        for j in range(columns):
            r = random.random()
            if r < p / 2:
                # pepper sprinkled
                output[i][j] = [0, 0, 0]
            elif r < p:
                # salt sprinkled
                output[i][j] = [255, 255, 255]
            else:
                output[i][j] = img[i][j]

    #   plt.imshow(img)
    plt.imshow(output)
    plt.title("salt and pepper noise")
    plt.show()


if __name__ == "__main__":
    salt_n_pepper()