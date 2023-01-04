from parent_Hewan import binatang

class Burung_Elang(binatang):
    def __init__(self, nama, makanan, hidup, berkembang_biak, sayap, cakar):
        super( ).__init__( nama, makanan, hidup, berkembang_biak)
        self.sayap = sayap
        self.cakar = cakar
        
    def cetak(self) :
        print("Memiliki \t:",self.sayap,
                "\nMemiliki \t:",self.cakar,
                "\n--------------------------------")