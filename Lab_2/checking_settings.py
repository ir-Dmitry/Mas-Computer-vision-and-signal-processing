import cv2
import numpy as np

im = cv2.imread(r"images/cat_in_grass.jpg")
winName = "Main Window"
cv2.namedWindow(winName)

image_a = cv2.GaussianBlur(im, ksize=(31, 31), sigmaX=15, sigmaY=15)
image_b = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
image_b = cv2.cvtColor(image_b, cv2.COLOR_GRAY2BGR)  # что бы было 3 канала


def update_image(r):
    result = image_a.copy()
    mask = np.zeros(shape=result.shape[:2], dtype=np.uint8)
    # создаем маску в виде круга
    cv2.circle(mask, (result.shape[1] // 2, result.shape[0] // 2), r, 1, -1)
    # применяем маску
    cv2.copyTo(image_b, mask, result)
    # обновляем окно с результатом
    cv2.imshow(winName, result)


cv2.createTrackbar("R", winName, 50, 500, update_image)
cv2.waitKey(0)
