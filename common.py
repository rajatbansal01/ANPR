from functions import *
import time
df = pd.DataFrame(columns=['date', 'v_number',
                           'plate_path', 'face_path', 'status'])
df.to_csv('data_new.csv', index=False)
try:
    os.mkdir("faces")
except FileExistsError:
    print("already exists")
    pass
try:
    os.mkdir("plates")
except FileExistsError:
    print("already exists")
    pass

n = 0
cap_plate = cv2.VideoCapture("uiet_testing.mp4")
num = []
while cap_plate.isOpened():
    ret, frame = cap_plate.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        number, plate_img = find_num(gray)
        if number:
            num.append(number)
        else:
            continue
        if len(num) > 10:
            n = most_frequent(num)
            csv_updater(n)
            save_plate(plate_img, n)
            print(n)
        else:
            continue
        try:
            vehicle, LpImg, cor = get_plate(frame)
            plate = draw_box(frame, cor)
            only_plate = image_for_ocr(LpImg)[2]
        except AssertionError:
            plate = frame
            only_plate = frame

        plate = cv2.resize(plate, (0, 0), fx=0.5, fy=0.5)
        if only_plate.shape[0] > 300 and only_plate.shape[1] > 300:
            only_plate = cv2.resize(only_plate, (0, 0), fx=0.3, fy=0.3)
        # code to calculate the fps.
        font = cv2.FONT_HERSHEY_SIMPLEX
        coordinates = (20, 30)
        fontScale = 1.0
        color = (0, 0, 255)
        thickness = 4
        plate = cv2.putText(plate, str(n), coordinates, font,
                            fontScale, color, thickness, cv2.LINE_AA)
        # new = time.time()
        # print(new)
        cv2.imshow("plate", plate)
        cv2.imshow("only_plate", only_plate)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 13 is enter key
            break
    else:
        break
cap_plate.release()
cv2.destroyAllWindows()
