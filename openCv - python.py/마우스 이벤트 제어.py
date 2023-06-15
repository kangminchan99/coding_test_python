# 마우스 오른쪽 버튼 클릭 시 원(클릭 좌표에서 반지름 20화소)을 그린다.
# 마우스 왼쪽 버튼 클릭 시 사각형(크기 30*30)을 그린다.

import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title
    # 마우스 오른쪽 버튼 클릭 시
    if event == cv2.EVENT_RBUTTONDOWN:
        # 클릭 좌표에서 반지름이 20인 원 그리기
        cv2.circle(img, (x, y), 20, (0, 0, 255), 2) # 두께가 2인 빨간 원
    # 마우스 왼쪽 버튼 클릭 시
    elif event == cv2.EVENT_LBUTTONDOWN:
        # 크기 30x30인 사각형 그리기
        cv2.rectangle(img, (x, y), (x+30, y+30), (255, 0, 0), 2) # 두께가 2인 파란 사각형

    cv2.imshow(title, img)

img = np.full((400, 300, 3), (255, 255, 255), np.uint8)
title = 'test'
cv2.imshow(title, img)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()