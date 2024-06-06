from Chroma import Chroma
from Support import *

class Chord(Chroma):
    # 4 constructors diff.
    # p1 String(nom de chroma), Obj chroma
    # p2 String(TypeAccord), intervals
        
    def __init__(self , nom, intervals):
        super().__init__(nom)
        if type(intervals) == str:
            self.type_accord = intervals
            self.intervals = dict_intervals[self.type_accord]
        else :
            self.intervals = self.__reverse(intervals)
            self.type_accord = Type_accord.getAccordType(self.intervals)
    
    def transpose(self, n ):
        super().transpose(n)

    def __reverse(self, intervals:list):
        print(intervals)
        return [i%12 for i in intervals].sort()
        
    def getProfile():
        pass

    def computeDistance(profile2:list = []):
        pass # return correlation entre self.getProfile et profile2

