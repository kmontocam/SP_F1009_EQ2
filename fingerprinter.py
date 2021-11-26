from scipy.fftpack import fft, fftfreq
import numpy as np

WINDOW = 1024
IMPACT = 2 # Coefficient used to consider relevance of fingerprints

def fingerprinter(audio_freq, audio):
    freq_times = list()
    freq_highs = list()

    for down, up in zip(range(0, len(audio), WINDOW), range(0, len(audio), WINDOW)[1:]):
        
        audio_window = audio[down:up]

        fourier_coeff = np.abs(fft(audio_window)) # Apply FFT on interval
        fourier_coeff = fourier_coeff[:len(fourier_coeff)//2] # Take only the positive half
        fourier_freq = fftfreq(len(audio_window), 1 / audio_freq) # Fix values as Hz
        fourier_freq = fourier_freq[:len(fourier_freq)//2] # Take only the positive half

        bin1 = max(fourier_coeff[:10]) # Very low sound
        bin2 = max(fourier_coeff[10:20]) # Low sound from band
        bin3 = max(fourier_coeff[20:40]) # ...
        bin4 = max(fourier_coeff[40:80])
        bin5 = max(fourier_coeff[80:160])
        bin6 = max(fourier_coeff[160:])

        bin_package = np.array([bin1, bin2, bin3, bin4, bin5, bin6])
        bin_mean = np.mean(bin_package)

        max_bins = [max_bin for max_bin in bin_package if max_bin > (IMPACT * bin_mean)]

        for ite in max_bins:
            position = np.where(fourier_coeff == ite)[0][0]
            freq_times.append((down + position)/audio_freq)
            freq_highs.append(fourier_freq[position])
    
    return freq_times, freq_highs