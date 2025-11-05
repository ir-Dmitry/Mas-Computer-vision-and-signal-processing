import cv2
import numpy as np


def reconstruct_from_shuffled(img, stripe_h):
    h = img.shape[0]

    stripes = [img[i : i + stripe_h] for i in range(0, h, stripe_h)]
    n = len(stripes)
    if n <= 1:
        return img.copy()

    # Строим матрицу различий
    diff = np.full((n, n), np.inf, dtype=np.float32)
    for i in range(n):
        for j in range(n):
            if i != j:
                diff[i, j] = np.mean(
                    np.abs(
                        stripes[i][-1].astype(np.float32)
                        - stripes[j][0].astype(np.float32)
                    )
                )

    # Находим стартовую полосу
    top_incompat = [min(diff[i, j] for i in range(n) if i != j) for j in range(n)]
    order = [int(np.argmax(top_incompat))]
    used = [False] * n
    used[order[0]] = True

    # Жадная сборка
    for _ in range(n - 1):
        cur = order[-1]
        nxt = min((j for j in range(n) if not used[j]), key=lambda j: diff[cur, j])
        order.append(nxt)
        used[nxt] = True

    return np.vstack([stripes[i] for i in order])


# main
shuffled = cv2.imread(r"images\cat_in_grass_shuffled.jpg")
if shuffled is None:
    raise FileNotFoundError("Перемешанное изображение не найдено.")

stripe_h = int(input("Введите высоту полосы: "))
restored = reconstruct_from_shuffled(shuffled, stripe_h)

cv2.imwrite(r"images\cat_in_grass_restored.jpg", restored)
cv2.imshow("Shuffled", shuffled)
cv2.imshow("Restored", restored)
cv2.waitKey(0)
cv2.destroyAllWindows()
