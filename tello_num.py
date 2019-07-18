# coding:utf8
import cv2
import numpy as np


def mathc_img(frame, Target, value):
    # image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target, 0)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where(res >= threshold)
    is_match = 0
    for pt in zip(*loc[::-1]):
        # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)
        if pt:
            is_match = 1
        else:
            is_match = 0
    return is_match


def number_detect(frame):
    Target = [r"\tpl\tpl1.jpg", r"\tpl\tpl2.jpg", r"\tpl\tpl3.jpg"] # 若报错，可替换为绝对路径
    value = 0.7
    for i in range(0, 3):
        flag = mathc_img(frame, Target[i], value)
        if flag:
            return i + 1
    return 0
