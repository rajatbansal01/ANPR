from functions import *
import time


cap_plate = cv2.VideoCapture("uiet_test.mp4")
num = []
prev = 0
new = 0
while cap_plate.isOpened():
    # time.sleep(0.05)
    ret, frame = cap_plate.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        try:
            vehicle, LpImg, cor = get_plate(frame)
            #plate = draw_box(frame,cor)
            plate = image_for_ocr(LpImg)[2]
        except AssertionError:
            plate = frame
        # code to calculate the fps.
        font = cv2.FONT_HERSHEY_SIMPLEX
        new = time.time()
        # print(new)
        fps = 1 // (new-prev)
        prev = new
        # cv2.putText(plate, str(fps), (7, 70), font, 3,
        #             (100, 255, 0), 3, cv2.LINE_AA)

        # code end for fps
        cv2.imshow("plate", plate)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 13 is enter key
            break
    else:
        break
cap_plate.release()
cv2.destroyAllWindows()
