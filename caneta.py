class Caneta:
    def __init__(self,cor,marca):
        self.cor = cor
        self.marca = marca
        self.tinta = 100

    def escrever(self):
        if self.tinta > 0:
            print("escrevendo")
        else:
            print("sem tinta")    
obj_caneta = Caneta('azul','bic')
obj_caneta.escrever()         