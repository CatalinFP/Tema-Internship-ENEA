import pyaudio
import wave


def record_audio(duration):
    filename = "record_audio.wav"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 2
    sample_rate = 44400
    record_seconds = duration
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