import cv2
import webcam
import numpy as np

def make_mask(image):
    # 4. face_mask에 contour 찾기
    # - 전처리 : 흑백 -> 이진화 -> findContour()
    gray_icon = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    _, bin_icon = cv2.threshold(255 - gray_icon, 70, 255, cv2.THRESH_BINARY)

    # 5. contour로 mask 만들기 
    contours, _ = cv2.findContours(bin_icon, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(gray_icon)
    cv2.drawContours(mask, contours, -1, 255, -1)

    return mask

def process(frame):
    # 1. 얼굴 인식
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(70, 70))

    # 2. 얼굴 마다 작업 진행
    for (x, y, w, h) in faces:        

        # 3. 얼굴 이미지를 하나 생성한다.
        roi = frame[y-15:y+h+15, x-15:x+w+15]
        # cv2.imshow('roi', roi)
        
        # 4. 얼굴 이미지에서 mask를 생성한다. -> mask에 해당
        mask = make_mask(roi)
        # cv2.imshow('mask', mask)

        # 5. 얼굴 이미지를 블러한다. -> icon 이미지 만드는 영역에 해당
        blurred_roi = cv2.blur(roi, (15, 15))
        # cv2.imshow('blurred', blurred_roi)

        roi[mask==255] = blurred_roi[mask==255]

    return frame

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
webcam.play(process)