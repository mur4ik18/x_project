from Chroma import Chroma
from main import *
# create class midi player
# add renversemet for chords | use modulo and after use sort like this we will get this [4, 7, 12] -> [0, 4, 7] -> M
# realiser profiles for chord
RefProfiles = {
    'M':[6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88],
    'm':[6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17],
}

profiles = {
    'Do': {'M': [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88], 'm': [6.33, 2.68, 3.52, 5.38, 2.6, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]},
    'Do#': {'M': [2.88, 6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29], 'm': [3.17, 6.33, 2.68, 3.52, 5.38, 2.6, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34]},
    'Re': {'M': [2.29, 2.88, 6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66], 'm': [3.34, 3.17, 6.33, 2.68, 3.52, 5.38, 2.6, 3.53, 2.54, 4.75, 3.98, 2.69]},
    'Re#': {'M': [3.66, 2.29, 2.88, 6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39], 'm': [2.69, 3.34, 3.17, 6.33, 2.68, 3.52, 5.38, 2.6, 3.53, 2.54, 4.75, 3.98]},
    'Mi': {'M': [2.39, 3.66, 2.29, 2.88, 6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19], 'm': [3.98, 2.69, 3.34, 3.17, 6.33, 2.68, 3.52, 5.38, 2.6, 3.53, 2.54, 4.75]},
    'Fa': {'M': [5.19, 2.39, 3.66, 2.29, 2.88, 6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52], 'm': [4.75, 3.98, 2.69, 3.34, 3.17, 6.33, 2.68, 3.52, 5.38, 2.6, 3.53, 2.54]},
    'Fa#': {'M': [2.52, 5.19, 2.39, 3.66, 2.29, 2.88, 6.35, 2.23, 3.48, 2.33, 4.38, 4.09], 'm': [2.54, 4.75, 3.98, 2.69, 3.34, 3.17, 6.33, 2.68, 3.52, 5.38, 2.6, 3.53]},
    'Sol': {'M': [4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88, 6.35, 2.23, 3.48, 2.33, 4.38], 'm': [3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17, 6.33, 2.68, 3.52, 5.38, 2.6]},
    'Sol#': {'M': [4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88, 6.35, 2.23, 3.48, 2.33], 'm': [2.6, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17, 6.33, 2.68, 3.52, 5.38]},
    'La': {'M': [2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88, 6.35, 2.23, 3.48], 'm': [5.38, 2.6, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17, 6.33, 2.68, 3.52]},
    'La#': {'M': [3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88, 6.35, 2.23], 'm': [3.52, 5.38, 2.6, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17, 6.33, 2.68]},
    'Si': {'M': [2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88, 6.35], 'm': [2.68, 3.52, 5.38, 2.6, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17, 6.33]}
}

# calcule Distance between two profiles, calculate corralation
# TODO tester les constructors de Chord et Chord_keyboard

# better to use tuples instead of lists?
dict_intervals = {'M': [0,4,7], 'm':[0,3,7] ,'M7': [0,3,7,11], 'm7': [0,3,7,10], '7': [0,4,7,10], '7sus4': [0,5,7,10], '4': [0,5,7], '2': [0,2,7], '6': [0,4,7,9], 'm6': [0,3,7,9], '6sus4': [0,5,7,9], 'dim': [0,3,6], 'aug': [0,4,8] , '5': [0,7] }


# List of the main kinds of chords used in music theory
class Type_accord:
    type_accord = list(dict_intervals);

    def getAccordType(intervals):
        for key, value in dict_intervals.items():
            if value == intervals:
              return key  


def generateProfiles():
    profileRoundM = RefProfiles["M"] + RefProfiles["M"]
    profileRoundm = RefProfiles["m"] + RefProfiles["m"]
    
    
    profiles[Chroma.chroma[0]] = {}
    profiles[Chroma.chroma[0]]["M"] = RefProfiles["M"]
    profiles[Chroma.chroma[0]]["m"] =RefProfiles["m"]
    landscapeM = [1] + RefProfiles["M"]
    landscapem = [1] + RefProfiles["m"]
    
    for i in range(1,12):
        profiles[Chroma.chroma[i]] = {}
        profiles[Chroma.chroma[i]]["M"] = profileRoundM[12-i : 24-i]
        profiles[Chroma.chroma[i]]["m"] = profileRoundm[12-i : 24-i]

        landscapeM.append([corr(landscapeM[0],landscapeM[-1])] + profileRoundM[12-i : 24-i])# ajouter correlation
        landscapem.append([corr(landscapem[0],landscapem[-1])] + profileRoundm[12-i : 24-i])
        

    landscapeM.sort()
    landscapem.sort()
    return landscapeM, landscapem

          
if __name__ == "__main__":
    M,m = generateProfiles()

    print(profiles)

    print(M)
    print(m)
