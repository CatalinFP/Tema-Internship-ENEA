from threading import Thread
from search_youtube import search_youtube
from record_audio import record_audio
from record_video import record_video
from db_extract import extract_db_file
import os


if __name__ == '__main__':
    search_ytb = Thread(target=search_youtube(search_key = "python"))
    search_ytb.start()
    search_ytb.join()

    rec_vid = Thread(target=record_video)
    rec_aud = Thread(target=record_audio)

    rec_vid.start()
    rec_vid.join()
    rec_aud.start()
    rec_aud.join()

    os.system("ffmpeg -i record_video.avi -i record_audio.wav -c:v copy -c:a aac output.mp4") #combine video and audio file

    db = Thread(target=extract_db_file)
    db.start()