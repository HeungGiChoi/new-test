import cv2

def play(x):
    cap = cv2.VideoCapture(0) # 0은 기본 웹캠을 의미

    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        if not ret:
            print("동영상 재생이 완료되었습니다.")
            break

        cv2.imshow('faces_detect', x(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()