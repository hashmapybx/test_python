import cv2
import numpy as np

def hProject(binary):
    h,w = binary.shape
    hProjection = np.zeros(binary.shape, dtype=np.uint8)

    # 创建h长度都为0的数组
    h_h = [0]*h
    for j in range(h):
        for i in range(w):
            if binary[j,i] == 0:
                h_h[j] += 1
    # 画出投影图
    for j in range(h):
        for i in range(h_h[j]):
            hProjection[j,i] = 255
    cv2.imshow('hpro', hProjection)
    return h_h

if __name__ == '__main__':
    img = cv2.imread('14.jpg')
    # 可选
    # img = cv2.resize(img,(500, 200), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img1 = cv2.GaussianBlur(gray, (3,3),0)

    # 方法一 霍夫变换直线检测
    edges = cv2.Canny(img1, 100 ,290,apertureSize=3)
    cv2.imshow('edge', edges)
    lines = cv2.HoughLines(edges, 1.5, np.pi / 180, 190)
    print(lines.shape[0])
    for line in lines:
        rho , theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        #cv2.line(img,(x1,y1),(x2,y2), (255,0,0), 2)
    #cv2.imshow('image', img)
    # 方法二
    center = edges.shape[1] // 2
    count = 0
    begin = -1
    for i in edges[1:,center]:
        # if begin == i:
        #     bigin = i
        #     continue
        # if begin != i) and i==255 :count+=1
        if i == 255:
            count += 1
    print(count)

    # 方法三：根据不同图需要调整阈值
    ret, th = cv2.threshold(img1, 130, 255, cv2.THRESH_BINARY)
    cv2.imshow('th', th)


    cv2.waitKey(0)
    cv2.destroyAllWindows()