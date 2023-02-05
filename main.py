import PIL.Image as Image
import os
import cv2


def three_To_one(path, save_path, file_list):
    i = 0

    for file in file_list:
        print("file_path:" + path + "/" + file_list[i])
        imgs = cv2.imread(path + "/" + file_list[i])


        file_name = os.path.splitext(file)[0]

        print("file_name: " + save_path + "/" + file_name + ".png")

        img_one = cv2.cvtColor(imgs, cv2.COLOR_RGB2GRAY)

        cv2.imwrite(save_path + "/" + file_name + ".png", img_one)
        i = i + 1


patient_save_path = "./data_png/patient"
tumor_save_path = r"./data_png/tumor"

patient_path = r"./data/patient"
print("patient_path:" + patient_path)

tumor_path = r"./data/tumor"
print("tumor_path:" + tumor_path)

patient_list = os.listdir(patient_path)
tumor_list = os.listdir(tumor_path)

three_To_one(tumor_path, tumor_save_path, tumor_list)

