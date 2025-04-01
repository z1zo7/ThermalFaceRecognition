#---------- AI libraries -----------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import glob as gb
import cv2
import keras
import tensorflow as tf
from tensorflow.keras.models import load_model
import inference_sdk

from library import *

def testImages():
    testpath = r"test_images"

    code = {'Mohamed Amr':0,'Moaaz Hail':1,'Moaaz Hail With Glasses':2,'Moaz Salem':3,'Moaz Salem With Glasses':4
        ,'Mohamed Amr With Glasses':5,'Mostafa Mamdouh':6,'Abdullah Yassin':7,'Mohamed Adel':8,"Mohamed Hossam":9
        , "Hossam Magdy":10, "Ali Badawy":11, "Mohamed Mostafa":12, "Ahmed Ramadan":14, "Mohamed Youssef":15,
            "Youssef Khaled":16, "Mostafa Taher":17, "Abdelrahman Sameh":18,"Ezz Ahmed":19,"Abdelrahman Essam":20,
            "Omar Abdelrahman":21,"Mohamed Mahmoud":22,"Adham Rabeh":23,"Mohamed Ismail":24,"Ahmed Sameh":25,
            "Mohamed Khaled":26,"Ahmed Samir":27,"Mohamed Hosny":28,"Nader Mohamed":29,"Ahmed Hussien":30,
            "Abdelrahman Ibrahim":31,"Hussien Mohamed":32,"Sameh Samy":33,"Adham Ahmed":34,"Omar Ahmed":35,"Ammar Ahmed":36,
            "Ahmed Mohamed":37,"Youssef Yasser":38,"Hossam Mohamed":39,"Abdulllah Atef":40,"Abdelrahman Kamel":41,
            "Abdelrahman Gameel":42,"Abdelrahman Ayman":43,"Saif Mohamed":44,"Tarek Mohamed":45,"Abdelrahman Tarek":46,
            "Abdelrahman Emad":47,"Mohamed Hussien":48,"Islam Abdelhady":49,"Ahmed Omar":50,"Abdullah Ramadan":51,
            "Abdelrahman Fouad":52,"Abdelhameed Rezk":53,"Nooreldeen Mahmoud":54,"Mostafa Adel":55,"Abdullah Elsheikh":56,
            "Omar Mohamed":57,"Saif Farag":58,"Shreif Ashraf":59,"Abdullah Abdelrahman":60,"Moussa Abdelrasheed":61,
            "Mohamed Ahmed":62,"Mohamed Ahmed With Glasses":63}


    def getcode(n):
        for x, y in code.items():
            if n == y:
                return x


    sx = 150
    sy = 150

    # face detection function
    def crop_image(image):

        from inference_sdk import InferenceHTTPClient
        CLIENT = InferenceHTTPClient(
            api_url="https://detect.roboflow.com",
            api_key="w8a3catZTTtfgurZMJ0V"
        )

        result = CLIENT.infer(image, model_id="persondog-lkd0u/2")
        if len(result["predictions"]) == 0:
            print("failed")
            return image
        x_min = int(result["predictions"][0]["x"])
        y_min = int(result["predictions"][0]["y"])
        width = int(result["predictions"][0]['width'])
        height = int(result["predictions"][0]['height'])

        cropped = image[y_min - int(0.5 * height):y_min + int(0.5 * height),
                  x_min - int(0.5 * width):x_min + int(0.5 * width)]
        # y- nos el rectangle mn foo2 , y+nos el rectangle el t7t
        # x - nos el rectangle mn el shmal , x+ nos el rectangle mn yemeen
        return cropped

    X_test = []
    X_test.clear()
    files = gb.glob(pathname=str(testpath + '/*.bmp'))
    for file in files:
        image = cv2.imread(file)
        image_array = crop_image(image)
        image_array = cv2.resize(image_array, (sx, sy))
        cv2.imwrite(r"cropped_image\newImage.bmp",image_array)
        X_test.append(list(image_array))

    print(f'we have {len(X_test)} items in X_test')

    X_test_array = np.array(X_test)
    print(f'X_test shape  is {X_test_array.shape}')

    loaded_model = load_model(r'test model.h5')

    y_result = loaded_model.predict(X_test_array)
    print('test Shape is {}'.format(y_result.shape))

    for i in range(len(X_test)):
        name = getcode(np.argmax(y_result[i]))
        faceName = name

    print(faceName)
    return(faceName)
    print(metrics)
