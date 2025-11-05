import cv2
import numpy as np
import random

# Загрузка изображения
im = cv2.imread(r"images\cat_in_grass.jpg")
if im is None:
    raise FileNotFoundError("Изображение не найдено. Проверьте путь.")

h, w = im.shape[:2]
stripe_h = 100
# stripe_h = int(input("Введите высоту полосы: "))

# На полосы
stripes = [im[i : i + stripe_h].copy() for i in range(0, h, stripe_h)]

random.shuffle(stripes)

shuffled = np.zeros_like(im)

y = 0
for stripe in stripes:
    h_s = stripe.shape[0]
    im[y : y + h_s, :] = stripe
    y += h_s

# Результат
cv2.imshow("Shuffled", im)
key = cv2.waitKey(0)

if key == 13:
    cv2.imwrite(r"images\cat_in_grass_shuffled.jpg", im)
cv2.destroyAllWindows()
