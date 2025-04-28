import cv2
import webcam
import numpy as np

def make_mask(image):
    # 4. face_mask에 contour 찾기
    # - 전처리 : 흑백 -> 이진화 -> findContour()
    gray_icon = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    _, bin_icon = cv2.threshold(255 - gray_icon, 50, 255, cv2.THRESH_BINARY)

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

        # 3 ~ 4. icon과 mask를 global 영역에서 구함
        # 6. 얼굴 영역에 mask 이용해서 icon 덮어쓰기
        # (1) frame 직접 그릴수는 없기 때문에, 얼굴 영역을 우선 찾아야 한다.
        roi = frame[y:y+h, x:x+w]
        # (2) 얼굴 영역에 크기를 기준으로 icon의 크기와 mask의 크기를 resize 한다.
        r_icon = cv2.resize(icon, (w, h))
        r_mask = cv2.resize(mask, (w, h))
        
        # (3) roi에다가 r_icon을 r_mask를 이용해서 복사한다.
        roi[r_mask==255] = r_icon[r_mask==255]

    return frame

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# icon mask 만들기
# 3. face_mask 읽기 -> icon 사용
icon = cv2.imread('face_mask.png')
mask = make_mask(icon)


webcam.play(process)