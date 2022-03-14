import cv2 as cv

img = cv.imread("miss.jpg")

# 访问和修改像素值
px = img[100, 100]
print(px)
# 仅仅访问蓝色
blue = img[100, 100, 0]
print(blue)

# 修改像素值
img[100, 100] = [0, 0,0]

# 以上方法访问修改像素值太慢了

# 优化方案
red = img.item(10, 10, 2)
print(red)
img.itemset((10, 10, 2), 255)

# 图像的属性包含了行数 列数 通道数  图像数据类型   像素值
print(img.shape) # 返回的是行数 列数 通道数
print("image size 像素总数", img.size)
print(img.dtype)

# 图像数据感兴趣ROI

ball = img[280:340, 330: 390]
# print(ball)

print("==="* 40)
# 拆分和合并图像通道
b,g,r =  cv.split(img)



import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('opencv-logo.png')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()












