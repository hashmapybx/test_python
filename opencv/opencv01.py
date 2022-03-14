import cv2
import numpy as np

# 创建一个黑色的图像
img = np.zeros((512, 512, 3), np.int8)

# 在图像上绘制一条直线
cv2.line(img, (0,0), (100, 100),(0,205,0), 10)
# 定义字体颜色
font = cv2.FONT_HERSHEY_SIMPLEX

# 在图像上写入文字
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("img",img)
while True:
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()


