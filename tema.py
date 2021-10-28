from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import cv2
import numpy as np
import pyautogui
import pyaudio
import wave
from threading import Thread, setprofile
from scipy.io.wavfile import write, read
import os
import math
import audioop
import scipy.io.wavfile as wf
import random
import sounddevice as sd
import time

def search_youtube(search_key):

# Opne Youtube and play something
    driver_opt = Options()
    driver_opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=driver_opt)
    driver.get("http://www.youtube.com")
    driver.implicitly_wait(15)
    driver.find_element(By.CSS_SELECTOR, "tp-yt-paper-button[aria-label='Agree to the use of cookies and other data for the purposes described']").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, "search_query")))
    search = driver.find_element(By.NAME, "search_query")
    search.click()
    search.send_keys(search_key)
    search.submit()

    driver.implicitly_wait(10)

    links = driver.find_elements(By.XPATH, '(//a[@id="thumbnail"])')

    random_link = random.randrange(0, len(links))
    if links[random_link] is not None:
        links[random_link].click()

    assert "No results found." not in driver.page_source

def record_video():
#video record

    SCREEN_SIZE = pyautogui.size()

    codec = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter("record_video.avi", codec, 5.5, (SCREEN_SIZE))
    cv2.namedWindow("screen_record", cv2.WINDOW_NORMAL)
    capture_duration = 10

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

#audio record
def record_audio():
    filename = "record_audio.wav"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 2
    sample_rate = 44400
    record_seconds = 10
    # device = 'digital output'
    play = pyaudio.PyAudio()

    stream = play.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = [] #frames array

    #record for 2 minutes
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    play.terminate()

    #save record
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(play.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()
    print("Audio Record Finished")

def extract_db_file():
    samprate, wavdata = wf.read('record_audio.wav')
    chunks = np.array_split(wavdata, 1024)

    f = open("dB_extracted.txt", "w")

    for chunk in chunks:
        rms = audioop.rms(chunk,2)
        dB=20*math.log10(rms)
        dB = "{:.2f}".format(dB)
        print (dB)
        f.write(str(dB) + os.linesep)

    f.close
        
if __name__ == '__main__':
    # search_ytb = Thread(target=search_youtube(search_key = "python"))
    # search_ytb.start()
    # search_ytb.join()

    rec_vid = Thread(target=record_video)
    rec_aud = Thread(target=record_audio)

    # rec_vid.start()
    # rec_vid.join()
    # rec_aud.start()
    # rec_aud.join()

    # os.system("ffmpeg -i record_video.avi -i record_audio.wav -c:v copy -c:a aac output.mp4") #combine video and audio file

    db = Thread(target=extract_db_file)
    db.start()
