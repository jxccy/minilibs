import cv2  # 需要先pip install opencv-python
import numpy as np  # 安装opencv-python的时候会自动安装numpy


def get_gap(recovery_png, gap_png):
    target = cv2.imread(recovery_png, 0)
    template = cv2.imread(gap_png, 0)
    w, h = target.shape[::-1]
    temp = 'temp.jpg'
    targ = 'targ.jpg'
    cv2.imwrite(temp, template)
    cv2.imwrite(targ, target)
    target = cv2.imread(targ)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    target = abs(255 - target)
    cv2.imwrite(targ, target)
    target = cv2.imread(targ)
    template = cv2.imread(temp)
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    # y就是水平缺口
    print(x, y)


get_gap("recovery.png", "slice.png")
