import sounddevice as sd
import time

SAMPLING_RATE = 11025  # Sample rate
DURATION = 20  # Duration of recording

def recorder():

    print('Recording...')
    myrecording = sd.rec(int(DURATION * SAMPLING_RATE), samplerate = SAMPLING_RATE, channels = 1)
    sd.wait()  # Wait until recording is finished
    myrecording = myrecording.flatten()
    myrecording[myrecording > 5000], myrecording[myrecording < -5000] = 0, 0 # Eliminate frequencies above 5kHz
    print('Done!')

    return SAMPLING_RATE, myrecording