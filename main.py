import sounddevice as sd
import pandas as pd
import numpy as np
from recorder import recorder
from fingerprinter import fingerprinter
from load_database import load_database
from matcher import lego_it, match_it

if __name__ == '__main__':

    # Type the complete route of fingerprints.csv !
    # Just in case ... 

    db = pd.read_csv(r'fingerprints.csv')

    # Load database with song's fingerprints.
    # Database is created by file "create_database.py"

    FingerprintLibrary = load_database(db) # Converts songs into fing

    sampling_rate, myrecording = recorder() # Record sample from a song in the database

    freq_times, freq_highs = fingerprinter(sampling_rate, myrecording) # Fingerprint the record
    tfg = np.array([freq_times, freq_highs])

    LegoLibrary = lego_it(FingerprintLibrary) # Prepare for match
    sample_lego = lego_it(tfg) # Prepare sample for match

    print(f'Tu canción es: {match_it(LegoLibrary, sample_lego)}') # Track returned