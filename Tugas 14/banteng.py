from parent_Hewan import binatang

class Banteng(binatang):
    def __init__(self, nama, makanan, hidup, berkembang_biak, tanduk, punuk):
        super( ).__init__( nama, makanan, hidup, berkembang_biak)
        self.tanduk = tanduk
        self.punuk = punuk
        
    def cetak(self) :
        print("Memiliki \t:",self.tanduk,
                "\nBerbulu \t:",self.punuk,
                "\n--------------------------------")