import cv2
print(cv2.__version__)

#image 읽기
image = cv2.imread('cat.jpg')
gray_image = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

# image 새창으로 열기
cv2.imshow('cat', image)
cv2.imshow('gray cat', gray_image)

# 윈도우가 닫히지 않게 키 입력 대기
cv2.waitKey(0)
cv2.destroyAllWindows()