
class Chroma:    
    #static or instance attribute depending on whether prefix is class name or instance
    chroma=('Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si')
    
    def __init__(self,nom:str = None)-> None:
        self.nom = nom
        self.index = Chroma.chroma.index(nom)
            
    def transpose(self, n:int=0) -> str:
        return Chroma.chroma [ (self.index+n) % len(Chroma.chroma) ]
