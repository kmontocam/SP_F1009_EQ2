import os
import numpy as np
import pandas as pd
from scipy.io import wavfile
from fingerprinter import fingerprinter
from compressor import compressor11025

## Type your file directory full of .wav songs
## in the variable named 'directory'
## Make sure the directory you choose is inside this project !

## A list of tracks was already preloaded. So you can start
## playing with sound even if you do not run this file!

if __name__ == '__main__':

    directory = r'/Users/you/Music/tracks'

    MUSIC_FOLDER = os.listdir(directory)
    tracks = [file for file in MUSIC_FOLDER if (file[-4:] == '.wav')]
    fingerprints = pd.DataFrame()

    for track in tracks:

        song_freq, song = wavfile.read(os.path.join(directory, track))

        compressed_freq, song_compressed = compressor11025(song_freq, song)

        freq_times, freq_highs = fingerprinter(compressed_freq, song_compressed)

        data = pd.DataFrame(list(zip(freq_times, freq_highs)),
        columns = pd.MultiIndex.from_tuples([(track[:-4], 'time'), (track[:-4], 'hz')]))
        
        fingerprints = pd.concat([fingerprints, data], axis = 1)

    fingerprints.to_csv('fingerprints.csv', index = False)
