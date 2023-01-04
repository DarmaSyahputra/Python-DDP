from parent_Hewan import binatang

class Gajah(binatang):
    def __init__(self, nama, makanan, hidup, berkembang_biak, belalai, gading):
        super( ).__init__( nama, makanan, hidup, berkembang_biak)
        self.belalai = belalai
        self.gading = gading
        
    def cetak(self) :
        print("Memiliki \t:",self.belalai,
                "\nMemiliki \t:",self.gading,
                "\n--------------------------------")