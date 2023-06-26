

import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title

    if event == cv2.EVENT_LBUTTONDOWN:

        cv2.circle(image, pt, 5, 100, 1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        # 크기 30x30인 사각형 그리기
        cv2.rectangle(image, pt, pt+(30+30), 100, 2)
        cv2.imshow(title, image)



image = np.ones((300, 300), np.uint8) * 255
title = 'test'
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()