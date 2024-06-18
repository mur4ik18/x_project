from Chroma import Chroma
from Support import *

class Chord(Chroma):
    # 4 constructors diff.
    # p1 String(nom de chroma), Obj chroma
    # p2 String(TypeAccord), intervals
        
    def __init__(self , nom:str = None, accord_type:str|None=None, intervals:list|None=None)->None:
        if nom != None:
            super().__init__(nom)
        else:
            raise ValueError("Name of Chroma can't be None")
        
        if accord_type != None:
            self.type_accord = accord_type
            self.intervals = dict_intervals[self.type_accord]
        elif intervals != None :
            self.intervals = self.__reverse(intervals)
            self.type_accord = Type_accord.getAccordType(self.intervals)
        else:
            raise ValueError("Accord type or intervals is obligatory")
    
    def transpose(self, n:int )->None:
        super().transpose(n)

    def __reverse(self, intervals:list[int])->list[int]:
        res = list([i%12 for i in intervals])
        res.sort()
        return res
        
    def getProfile(self)->None:
        prof = profiles[self.type_accord]
        start = self.index
        self.profile = {}
        for i in range(0,12):
            self.profile[Chroma.chroma[i]] = prof[(i-start)%12]

    def computeDistance(profile2:list = []):
        pass # return correlation entre self.getProfile et profile2

if __name__ == "__main__":
    x = Chord(nom="Do", accord_type="M")
    print(x.nom, x.type_accord, x.intervals)

    y = Chord(nom="Do", intervals=[0,4,7])
    print(y.nom, y.type_accord, y.intervals)


    # with reverse
    y = Chord(nom="Mi", intervals=[4,7,12])
    print(y.nom, y.type_accord, y.intervals)

    
    try:
        x = Chord("Do")
        print(x.nom, x.type_accord, x.intervals)
    except ValueError as e:
        print("ValueError", e)

    y.getProfile()
    print(y.profile)
