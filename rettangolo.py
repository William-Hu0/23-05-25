class Rettangolo:
    def __init__(self,base,altezza,colore):
        self.base=base
        self.altezza=altezza
        self.colore=colore
    def area(self):
        return self.base*self.altezza
    def stampa_info(self):
        print(self.base)
        print(self.altezza)
        print(self.colore)
        print(self.area())    
