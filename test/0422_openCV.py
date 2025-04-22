# import cv2
# print(cv2.__version__)

# #image 읽기
# image = cv2.imread('cat.jpg')
# # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# gray_image = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

# # image 새창으로 열기
# # cv2.imshow('cat', image)
# # cv2.imshow('gray cat', gray_image)

# # # 윈도우가 닫히지 않게 키 입력 대기
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # #image 저장
# # cv2.imwrite('cat_gray.jpg', gray_image)

# # print(image.shape)
# # print(gray_image.shape)

# # 절반 or 1/4만 보기
# # image = image[:334, 500:]

# # cv2.imshow('cat', image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # resize(파일명, (크기))
# # resized_image = cv2.resize(image, (300, 200))
# # print(resized_image.shape)
# # cv2.imshow('cat', resized_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # 가로/세로 비율로 크기 조정
# # scale = 0.5
# # resized_image = cv2.resize(image, None, fx=scale, fy=scale)
# # print(resized_image.shape)
# # cv2.imshow('cat', resized_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # # 실습 2 : 이미지 회전
# # cv2.imwrite('resize_cat.jpg', resized_image)
# # image = cv2.imread('resize_cat.jpg')
# # (h, w) = image.shape[:2]
# # center = (w // 2, h // 2)

# # matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
# # rotated_image = cv2.warpAffine(image, matrix, (w, h))

# # cv2.imwrite('rotate_cat.jpg', rotated_image)

# # 실습 3 : 하단 절반만 흑백
# low_img = image[334:].copy()

# low_img = cv2.cvtColor(low_img, cv2.COLOR_BGR2GRAY)
# print(low_img.shape) # (334, 1000)

# low_img = cv2.cvtColor(low_img, cv2.COLOR_GRAY2BGR)
# print(low_img.shape) # (334, 1000, 3)

# # 원본이미지에 흑백으로 변경한 부분을 붙여넣기
# image[334:, :] = low_img

# cv2.imshow('cat', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# half_gray_image = cv2.cvtColor(image[338:], cv2.COLOR_BGR2GRAY)
# cv2.imshow('cat', half_gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

# 동영상 파일 경로 설정
video_path = "C:\\Users\\choi heung ki\\Desktop\\CodingOnEDU/video.mp4"

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 동영상 재생
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("동영상 재생이 완료되었습니다.")
        break

    cv2.imshow('video', frame)

    # 속도 조절(프레임 사이에 잠시 대기)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 캡처 객체 해제
cap. release()
cv2.destroyAllWindows()