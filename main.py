import cv2
from mss import mss
import numpy as np
# 摄像头

# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     cv2.imshow("frame", frame)
#     if cv2.waitKey(1) == ord("q"):
#         cap.release()
#         cv2.destroyAllWindows()
#         break


# 桌面
# while True:
#     img = mss().grab(monitor={"top":0, "left": 0, "width": 500, "height": 500})
#     img = np.array(img)
#     cv2.imshow("img", img)
#     if cv2.waitKey(1) == ord("q"):
#         cv2.destroyAllWindows()
#         break

img = mss().grab(monitor={"top":0, "left": 0, "width": 500, "height": 500})
print(img)