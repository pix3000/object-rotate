import cv2
import numpy as np
import math


ori_img = cv2.imread("test/black0613.JPG")
padding_img = cv2.imread("test/test0613_1.jpg")

h,w,c = padding_img.shape


rh = int(h/100)
rw =  int(w/100)

print(h,w)  #1313, 1370
print(rh,rw) #13, 13

BG_img = ori_img[0:rw, 0:rh]
BG_img = cv2.resize(BG_img, (h, w))

BGh, BGw, BGc = BG_img.shape    #1313, 1370
print(BGw, BGh)


img1 = BG_img
img2 = cv2.imread("test/black0613.JPG")

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

rows,cols,channels = img2.shape

roi = img1[0:rows, 0:cols]

hpos, vpos, cpos = img1.shape

hpos =  int((hpos-cols)/2)
vpos = int((vpos-rows)/2)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)



dst = cv2.add(img1_bg, img2_fg)

img1[vpos:rows+vpos, hpos:cols+hpos] = dst

cv2.imwrite('test/test0613_(1%).jpg',img1)

th, tw, tx = img1.shape
print(tw, th)