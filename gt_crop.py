import cv2
import os
import platform


def txt_read(txtname):      #txt파일 읽어와서 문자열 분리
    f = open(txtname, "r")
    lines = f.readlines()
    return lines


def img_crop(img_name):
    
    dir_ = "img_old/"
    txt_name = img_name.split(".")[0] + ".txt"

    ir = cv2.imread(dir_ + img_name)
    tr = txt_read(dir_ + txt_name)

    for i, txt_data in enumerate(tr):
        txt_data = txt_data.split(" ")

        #txt 상대값 읽어오기
        x1= float(txt_data[1])   #0.544141
        y1= float(txt_data[2])   #0.492361
        x2= float(txt_data[3])   #0.410156
        y2= float(txt_data[4])   #0.531944

        h,w,c = ir.shape    #img width, img height

        x1= float(w*x1)     #상대값 -> 절대값
        x2= float(w*x2)
        y1= float(h*y1)
        y2= float(h*y2)


        a1= int(x1-(x2/2))  #crop 범위 지정
        b1= int(y1-(y2/2))
        a2= int(a1+x2)
        b2= int(b1+y2)


        dst = ir[b1:b2, a1:a2].copy()   #image crop

        result_name = ""
        if i == 0:
            result_name = img_name # apis0003.jpeg 고대로
        else:
            split_name = img_name.split(".")
            result_name = f"{split_name[0]}_{i}.{split_name[1]}" # apis0003_1.jpeg
            print(result_name)


        if platform.system() == 'Linux':
            cv2.imwrite(f'{os.getcwd()}/result/{result_name}', dst)

file_list = os.listdir('img_old')

file_list_2 = []

for file_name in file_list:
    if file_name[-3:] != "txt":
        file_list_2.append(file_name)



for file_name in file_list_2:
    img_crop(file_name)






'''
temp_list = ["apple", "banana", "kiwi"]

for i in range(len(temp_list)): # range(3) = 0,1,2
    print(temp_list[i])

#print(temp_list[0])
#print(temp_list[1])
#print(temp_list[2])

print("##########################################")

for furuit in temp_list:
    print(furuit)



# marks1.py
marks = [90, 25, 67, 45, 80]



for i, mark in enumerate(marks): 
    if mark >= 60: 
        # print("%d번 학생은 합격입니다." % i+1)
        print(f"{i+1}번 학생은 합격입니다.")
    else: 
        # print("%d번 학생은 불합격입니다." % i+1)
        print(f"{i+1}번 학생은 불합격입니다.")


temp_str = "010-1234-5678"
result = temp_str.split("-")
print(result)
'''

'''
file_list_2 = []
for file_name in file_list:
    file_name = file_name.split(".")[0]
    file_list_2.append(file_name)
file_list_2 = list(set(file_list_2))
print(len(file_list_2))
'''
