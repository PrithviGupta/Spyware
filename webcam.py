import time
import cv2
img_counter = 0
while True:
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Loading..")
    ret, frame = cam.read()
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    time.sleep(30)
