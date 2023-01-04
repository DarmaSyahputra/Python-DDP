gorengan = ("bakwan","combro","misro")
sop = ("sop iga","sop buntut","sop kaki")
nasi = ("nasi uduk","nasi goreng","nasi remes")

makanan = (gorengan, sop, nasi)
#index      0       1       2

# cetak gorengan dari variable makanan dikeluarkan dari buka tutup kurung

for i in makanan[0]:
    print(i)

print(makanan[1][1])

print(makanan[2][2])

for i in makanan:
    for detail_makanan in i:
        print(detail_makanan)