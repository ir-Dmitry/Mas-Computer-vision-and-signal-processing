import cv2
import numpy as np

im = cv2.imread(r"images/cat_in_grass.jpg")
if im is None:
    raise FileNotFoundError("Изображение не найдено!")

blurred = cv2.GaussianBlur(im, (31, 31), 15)
gray_bgr = cv2.cvtColor(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)

accum = np.zeros(im.shape[:2], np.float32)
win = "Task 7: Permanent"


def on_mouse(event, x, y, *_):
    global accum
    if event == cv2.EVENT_MOUSEMOVE:
        r = cv2.getTrackbarPos("Radius", win)
        blur = cv2.getTrackbarPos("Blur", win)
        temp = np.zeros_like(accum)
        cv2.circle(temp, (x, y), r, 1.0, -1)
        temp = cv2.GaussianBlur(temp, (blur * 2 + 1, blur * 2 + 1), blur)
        accum[:] = np.clip(accum + temp, 0, 1)


cv2.namedWindow(win)
cv2.setMouseCallback(win, on_mouse)
cv2.createTrackbar("Radius", win, 50, 200, lambda _: None)
cv2.createTrackbar("Blur", win, 15, 50, lambda _: None)

print("Водите мышью — след остаётся. Нажмите любую клавишу для выхода.")

while True:
    m3 = np.stack([accum] * 3, -1)
    res = (blurred * (1 - m3) + gray_bgr * m3).astype(np.uint8)
    cv2.imshow(win, res)
    if cv2.waitKey(30) != -1:
        break

cv2.destroyAllWindows()
