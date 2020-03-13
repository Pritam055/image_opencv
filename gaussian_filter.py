# Gaussian filtering

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Lenna.jfif", cv.IMREAD_GRAYSCALE);

# img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

gauss = (1.0 / 273) * np.array([
    [1, 4, 7, 4, 1],
    [4, 16, 26, 16, 4],
    [7, 26, 41, 26, 7],
    [1, 4, 7, 4, 1],
    [4, 16, 26, 16, 4]
])
# gaussian filter and calculating probability

height = img.shape[0]
width = img.shape[1]

img_out = img.copy()
for i in range(2, height - 2):
    for j in range(2, width - 2):
        sum = 0
        for k in range(-2, 3):
            for l in range(-2, 3):
                a = img.item(i + k, j + l)
                p = gauss[k + 2, l + 2]
                # p is probabilit
                sum = sum + (a * p)
        b = sum
        img_out.itemset((i, j), b)

img_out = cv.cvtColor(img_out, cv.COLOR_BGR2RGB)
plt.imshow(img_out)



