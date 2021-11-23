import pandas as pd
import numpy as np

def load_database(db):

    FingerprintLibrary = dict()

    for down, up in zip(range(0, db.columns.size + 1, 2), range(0, db.columns.size + 1, 2)[1:]):
    
        song_name = db.iloc[:, down:up].columns[0]
        freq_times = db.iloc[:, down: down + 1][1:].dropna().to_numpy().flatten().astype(float)
        freq_highs = db.iloc[:, up - 1 : up][1:].dropna().to_numpy().flatten().astype(float)

        FingerprintLibrary[song_name] = np.array([freq_times, freq_highs])

    return FingerprintLibrary