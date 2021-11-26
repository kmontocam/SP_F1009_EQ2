TOLERANCE_FREQ = 20
TOLERANCE_TIME = 0.1

def lego_it(material):
    if isinstance(material, dict):
        LegoLibrary = dict()
        for track in material:
            lego_stack = list()
            for freci in range(0, len(material[track][1]) - 3):
                lego = [material[track][1][freci], material[track][1][freci + 3], 
                        material[track][0][freci + 3] - material[track][0][freci]]
                lego_stack.append(lego)
            LegoLibrary[track] = lego_stack
        return LegoLibrary
        
    else:
        lego_stack = list()
        for freci in range(0, len(material[1]) - 3):
            lego = [material[1][freci], material[1][freci+3],
                    material[0][freci + 3] - material[0][freci]]
            lego_stack.append(lego)
        return lego_stack

def match_it(LegoLibrary, sample_lego):
    n_matches = 0
    matches = list()
    matches_average = list()

    for track in LegoLibrary:
        for lego_track in range(0, len(LegoLibrary[track])):
            for piece in range(0, len(sample_lego)):
                if (((sample_lego[piece][0]) - TOLERANCE_FREQ <= (LegoLibrary[track][lego_track][0]) <= (sample_lego[piece][0]) + TOLERANCE_FREQ)  and
                    ((sample_lego[piece][1]) - TOLERANCE_FREQ <= (LegoLibrary[track][lego_track][1]) <= (sample_lego[piece][1]) + TOLERANCE_FREQ) and 
                    ((sample_lego[piece][2]) - TOLERANCE_TIME <= (LegoLibrary[track][lego_track][2]) <= (sample_lego[piece][2]) + TOLERANCE_TIME)):

                    n_matches += 1
                    
        matches.append(n_matches)
        matches_average.append(n_matches/len(LegoLibrary[track]))
        n_matches = 0

    return list(LegoLibrary.keys())[matches_average.index(max(matches_average))]