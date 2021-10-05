from functions import *
vehicle, LpImg, cor = get_plate(cv2.imread('car1.jpg'))
print(type(LpImg))

while True:
    cv2.imshow('LpImg', erode(LpImg[2]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
