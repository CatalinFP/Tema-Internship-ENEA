import cv2
import numpy as np
import pyautogui
import time


def record_video(duration):
#video record

    SCREEN_SIZE = pyautogui.size()

    codec = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter("./Tema Internship/record_video.avi", codec, 5.5, (SCREEN_SIZE))
    cv2.namedWindow("screen_record", cv2.WINDOW_NORMAL)
    capture_duration = duration

    start_time = time.time()
    while( int(time.time() - start_time) < capture_duration ):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow('screen_record', frame)
        if cv2.waitKey(1) == ord("q"): #close the recorder
            break
    out.release()
    cv2.destroyAllWindows()
    print("Video Record Finished")