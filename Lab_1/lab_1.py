from cv2 import imread, imwrite, imshow, waitKey
import numpy as np
import random

# Загрузка изображения
im = imread(r"images\cat_in_grass.jpg")
if im is None:
    raise FileNotFoundError("Изображение не найдено. Проверьте путь.")

h, w = im.shape[:2]
print("Высота изображения:", h)
# stripe_h = 100
stripe_h = int(input("Введите высоту полосы: "))

# На полосы
new_h = (h // stripe_h) * stripe_h
im_cropped = im[:new_h]
stripes = [im_cropped[i : i + stripe_h].copy() for i in range(0, h, stripe_h)]

random.shuffle(stripes)

y = 0
for stripe in stripes:
    h_s = stripe.shape[0]
    im_cropped[y : y + h_s, :] = stripe
    y += h_s

# Результат
imshow("Shuffled", im_cropped)
key = waitKey(0)

if key == 13:
    imwrite(r"images\cat_in_grass_shuffled.jpg", im_cropped)
    print("Изображение сохранено!")
