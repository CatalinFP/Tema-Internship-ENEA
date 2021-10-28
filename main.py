from threading import Thread
import logger
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import wait
from search_youtube import search_youtube
from record_audio import record_audio
from record_video import record_video
from db_extract import extract_db_file
import subprocess
import time

def main():

    get_time = 5 #record video/audio time

    try:
        # search_ytb = Thread(target=search_youtube(search_key = "python"))
        rec_vid = Thread(target=record_video, args=(get_time, ))
        rec_aud = Thread(target=record_audio, args=(get_time, ))
        db = Thread(target=extract_db_file)

        # search_ytb.start()
        # search_ytb.join()

        rec_vid.start()
        rec_aud.start()

        rec_aud.join()
        rec_vid.join()

    except TimeoutException as timerr:
        print(timerr)

    except Exception as weberr:
        raise WebDriverException("No internet connection!", weberr)

    time.sleep(5)
    try:
        subprocess.call(f'ffmpeg -i "./Tema Internship/record_video.avi" -i "./Tema Internship/record_audio.wav" -c:v copy -c:a aac "./Tema Internship/output.mp4"', shell=True) #combine video and audio file

    except subprocess.SubprocessError:
        print("Missing files!")

    # try:
    #     db.start()
    # except Exception as e:
    #     print("No such file or directory!", e)


if __name__ == '__main__':
    main()