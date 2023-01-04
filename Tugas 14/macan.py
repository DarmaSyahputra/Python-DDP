from parent_Hewan import binatang

class Macan(binatang):
    def __init__(self, nama, makanan, hidup, berkembang_biak, taring, loreng):
        super( ).__init__( nama, makanan, hidup, berkembang_biak)
        self.taring = taring
        self.loreng = loreng
        
    def cetak(self) :
        print("Memiliki \t:",self.taring,
                "\nBerbulu \t:",self.loreng,
                "\n--------------------------------")