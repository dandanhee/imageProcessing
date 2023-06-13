import cv2

## 함수선언부 ##


## 전역변수부 ##
src1,dest1 = None,None
path1 = "/Users/idanhui/Desktop/깃관련/imageProcessing/images/picture08.jpg"

## 메인코드부 ##
src1 = cv2.imread(path1)

cv2.imshow('src1',src1)

# 마무리
cv2.waitKey(0)
cv2.destroyAllWindows()
