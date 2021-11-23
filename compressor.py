from scipy import signal

DOWNSAMPLING_RATE_11025 = 11025 # Downsampling rate, 11.025 kHz

def compressor11025(audio_freq, audio):

    audio = audio.sum(axis = 1) / 2 # Convert to mono channel

    audio[audio > 5000], audio[audio < -5000] = 0, 0  # Avoid aliasing by removing frequencies above 5khz
    duration = round(len(audio)/audio_freq) # Seconds in track
    samps = duration * DOWNSAMPLING_RATE_11025

    audio = signal.resample(audio, samps)
    
    return DOWNSAMPLING_RATE_11025, audio