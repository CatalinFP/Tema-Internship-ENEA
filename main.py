from threading import Thread
import logger
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from search_youtube import search_youtube
from record_audio import record_audio
from record_video import record_video
from db_extract import extract_db_file
import subprocess
import logging


if __name__ == '__main__':

    try:
        # search_ytb = Thread(target=search_youtube(search_key = "python"))
        # rec_vid = Thread(target=record_video)
        # rec_aud = Thread(target=record_audio)
        db = Thread(target=extract_db_file)

        # search_ytb.start()
        # search_ytb.join()

        # rec_vid.start()
        # rec_vid.join()
        # rec_aud.start()
        # rec_aud.join()

    except TimeoutException as timerr:
        print(timerr)

    except WebDriverException as weberr:
        msg = str(webdriver.msg)
        
        if 'ERR_INTERNET_DISCONNECTED' in msg:
            print("No internet connection!")

    try:
        subprocess.run(["ffmpeg -i record_video.avi -i record_audio.wav -c:v copy -c:a aac output.mp4"], check=True) #combine video and audio file
    
    except subprocess.CalledProcessError:
        logging.exception("Missing Files!")
    

    try:
        db.start()
    except Exception:
        print("No such file or directory!")