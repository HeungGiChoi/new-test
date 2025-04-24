import cv2

# # 얼굴 이미지 가리기
# #.얼굴/py 파일과 동일한 경로에 .xml 파일을 저장하고 파일을 로딩
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0) # 0은 기본 웹캠을 의미

# # 얼굴을 가릴 마스크
# face_mask = cv2.imread('face_mask.png')
# cv2.imshow('face mask', face_mask)

# # 동영상 재생
# while True:
#     # 프레임 읽기
#     ret, frame = cap.read()
#     if not ret:
#         print("동영상 재생이 완료되었습니다.")
#         break
    
#     # 그레이스케일로 변환
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # 얼굴탐지
#     faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

#     # 탐지된 얼굴에 사각형 그리기
#     for i, (x, y, w, h) in enumerate(faces):
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#         # mask의 사이즈를 박스 사이즈로 줄이기
#         face_mask = cv2.resize(face_mask, (w, h))

#         # 원본 이미지에 face_mask 이미지 복사하기
#         frame[y:y+h, x:x+w] = face_mask


#     cv2.imshow('faces_detect', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# 눈 디텍션
#.얼굴
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#눈
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0) # 0은 기본 웹캠을 의
# 동영상 재생
while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        print("동영상 재생이 완료되었습니다.")
        break
    
    # 그레이스케일로 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴탐지
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # 탐지된 얼굴에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # 눈 탐지
        roi = gray_frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi, scaleFactor=1.1, minNeighbors=10, minSize=(15,15))

        for( ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow('eyes', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()