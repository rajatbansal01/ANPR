# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:48:50 2020

@author: HP
"""
from functions import *
img = cv2.imread("car.jpg")
num,image = find_num(img)
print(num)
print(img.dtype)