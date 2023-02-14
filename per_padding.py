import cv2
import numpy as np
import PIL
from PIL import Image
import os
import platform
import math



'''
def resize(img):

    #원본 이미지 크기 줄이기
    re_img  = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    return re_img
'''


def txt_read(txtname):  #text 값 읽어오기
    f = open(txtname, "r")
    lines = f.readlines()

    return lines



def img_crop(img, txt): #img를 라벨링 데이터 txt를 불러온 후 자르기

    '''
    dir = "img_old/"

    img = cv2.imread(dir + img)
    txt = txt_read(dir + txt)
    '''

    img = cv2.imread(img)
    h,w,c = img.shape

    txt_data = txt_read(txt)


    txt_data = txt_data[0].split(" ")

    #txt 상대값 읽어오기
    x1= float(txt_data[1])   
    y1= float(txt_data[2])   
    x2= float(txt_data[3])   
    y2= float(txt_data[4])      

    x1= float(w*x1)     #상대값 -> 절대값
    x2= float(w*x2)
    y1= float(h*y1)
    y2= float(h*y2)


    a1= int(x1-(x2/2))  #편집할 범위 지정
    b1= int(y1-(y2/2))
    a2= int(a1+x2)
    b2= int(b1+y2)

    crop_img = img[b1:b2, a1:a2].copy()  #image crop

    return crop_img



#def BG_add():   #배경 세밀화 과정(단색보다 더 디테일하도록)





def padding(img, txt, n):
    
    ori_img = cv2.imread(img)
    crop_img = img_crop(img, txt)

    h,w,c = crop_img.shape
    
    padding_area = (100*h*w)/n

    #print(f'Target area:{h*w}')
    #print(f'All image area:{padding_area}')

    save_len = int(math.sqrt(h*w))
    padding_len = int(math.sqrt(padding_area)) 


    #object가 전체 이미지 크기 중 N% 비율을 차지하게끔
    top, bottom = int((padding_len-save_len)/2), int((padding_len-save_len)/2)
    left, right = int((padding_len-save_len)/2), int((padding_len-save_len)/2)


    #padding 단색 추출
    pix =  ori_img[2,2]    

    pix_0 = int(pix[0])
    pix_1 = int(pix[1])
    pix_2 = int(pix[2])


    new_img =  cv2.copyMakeBorder(ori_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[pix_0, pix_1, pix_2])
  
    
    return new_img

  

img = "img_old/black0613.JPG"
txt = "img_old/black0613.txt"



cv2.imwrite(f'save/result0033_1.jpg', padding(img, txt, 1))
cv2.imwrite(f'save/result0033_3.jpg', padding(img, txt, 3))
cv2.imwrite(f'save/result0033_5.jpg', padding(img, txt, 5))
cv2.imwrite(f'save/result0033_10.jpg', padding(img, txt, 10))