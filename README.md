本章内容： Opencv从摄像头捕获画面 和 mss从桌面捕获画面
--
环境：
--
python 3.9.7

opencv

mss

安装：
--
pip install mss

pip install opencv(上期已经安装)

摄像头：
--
* 读取



    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()    



* 释放



    cap.release()
    cv2.destroyAllWindows()
    

桌面捕获：
--

* 捕获帧



    frame = mss.mss().grab()








