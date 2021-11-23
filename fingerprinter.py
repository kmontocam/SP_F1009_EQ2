from scipy.fftpack import fft, fftfreq
import numpy as np

HAMMING = 1024

def fingerprinter(audio_freq, audio):
    freq_times = list()
    freq_highs = list()

    for limit_inf, limit_sup in zip(range(0, len(audio), HAMMING), range(0, len(audio), HAMMING)[1:]):
        
        audio_hammed = audio[limit_inf: limit_sup]

        yf = np.abs(fft(audio_hammed)) # Apply FFT on interval
        yf = yf[:len(yf)//2] # Take only the positive half
        xf = fftfreq(len(audio_hammed), 1 / audio_freq) # Fix values as Hz
        xf = xf[:len(xf)//2] # Take only the positive half

        bin1 = max(yf[:10]) # Very low sound
        bin2 = max(yf[10:20]) # Low sound from band
        bin3 = max(yf[20: 40]) #...
        bin4 = max(yf[40: 80])
        bin5 = max(yf[80: 160])
        bin6 = max(yf[160:])

        bin_package = np.array([bin1, bin2, bin3, bin4, bin5])
        bin_mean = np.mean(bin_package)

        yf_highs = [f for f in bin_package if f > (1.5 * bin_mean)]

        for ite in yf_highs:
            position = np.where(yf == ite)[0][0]
            freq_times.append((limit_inf + position)/audio_freq)
            freq_highs.append(xf[position])
    
    return freq_times, freq_highs