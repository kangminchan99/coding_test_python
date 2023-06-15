# 600행, 400열의 윈도우를 만들고,
# 영상 안의 (100, 100) 좌표에 200x300 크기의 빨간 사각형을 그리시오.

import numpy as np, cv2

# 600행, 400열의 윈도우를 만들고(3채널 흰 영상)
image1 = np.full((600, 400, 3), (255,255,255), uint8)
title = 'test'

# 영상의 (100, 100) 좌표에 200x300 크기의 빨간색 사각형을 그리시오
pt1, pt2 = (100,100), (200, 300)
red = (0,0,255)
cv2.rectangle(image1, pt1, pt2, red, -1)

cv2.imshow(title, img)

cv2.waitKey(0)
cv2.destroyAllWindows()