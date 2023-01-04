class mahasiswa:
    def _init_(self, nim, nama, rombel) :
        self.nim = nim
        self.nama = nama
        self.rombel = rombel

    #atribut
    def lulus (self, nilai):
        if (nilai> 90):
            print("lulus")
        else:
            print("tidak lulus")

    def cetak(self):
         print("nama :" , self.nama)
         print("nim :", self.nim)
         print("rombel :", self.rombel)


#membuat objek
mahasiswa1 = mahasiswa("011023", "ahmad", "ti-05")


mahasiswa1.cetak()
mahasiswa1.lulus(95)



# print(help(mahasiswa1))

mahasiswa2 = mahasiswa("0110223", "udin", "ti-05")


mahasiswa2.cetak()
mahasiswa2.lulus(85)