import numpy as np
from scipy.io.wavfile import write, read
import os
import math
import audioop
import scipy.io.wavfile as wf


def extract_db_file():
    samprate, wavdata = wf.read('./Tema Internship/record_audio.wav')
    chunks = np.array_split(wavdata, 1024)

    f = open("./Tema Internship/dB_extracted.txt", "w")

    for chunk in chunks:
        rms = audioop.rms(chunk,2)
        dB=20*math.log10(rms)
        dB = "{:.2f}".format(dB)
        f.write(str(dB) + os.linesep)

    f.close