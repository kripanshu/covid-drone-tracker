"""
@author: Kripanshu
Reference : https://github.com/kripanshu/FaceMaskDetector
"""

import numpy as np
import tensorflow.keras.backend as k
from tensorflow.keras.layers import Conv2D, MaxPooling2D, SpatialDropout2D, Flatten, Dropout, Dense
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import image
from numpy import unravel_index
import cv2
import datetime

mymodel = load_model('mask_model_125X125.h5')

# cap=cv2.VideoCapture(0) // If you want to test on live front cam feed.
cap = cv2.VideoCapture('udp://@0.0.0.0:11111?overrun_nonfatal=1&fifo_size=50000000')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while cap.isOpened():
    ret, img = cap.read()
    if ret:
        face = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)
        for (x, y, w, h) in face:
            face_img = img[y:y + h, x:x + w]
            cv2.imwrite('temp.jpg', face_img)
            test_image = image.load_img('temp.jpg', target_size=(125, 125, 3))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            pred = mymodel.predict(test_image)
            row, index = unravel_index(pred.argmax(), pred.shape)
            if index == 1:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(img, 'MASK', ((x + w) // 2, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, 'NO MASK', ((x + w) // 2, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            datet = str(datetime.datetime.now())
            cv2.putText(img, datet, (400, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow('img', img)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
