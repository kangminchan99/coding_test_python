# 200행, 300열의 행렬 2개를 만들어서 다음과 같이 배치하시오.

import numpy as np, cv2

# 크기가 200x300이고 모든 픽셀 값이 100인 이미지 배열입니다.
# 이러한 이미지는 회색조 이미지로, 모든 픽셀이 밝기 값으로 100을 가집니다.
img1 = np.full((200,300), 100, np.uint8)
img2 = np.full((200,300), 100, np.uint8)

title1, title2 = 'win_model1', 'win_model2'

w, h = img1.shape


# 
cv2.imshow(title1, img1)
cv2.imshow(title2, img2)
# 위치 변경
cv2.moveWindow(title1, 0, 0)
cv2.moveWindow(title2, h, w)

cv2.waitKey(0)
cv2.destroyAllWindows()