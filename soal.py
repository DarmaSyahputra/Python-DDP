list_makanan = [
    ["bakwan" , "tempe" , "tahu"],
    ["nasi uduk" , "nasi pecel", "sate padang"]
]

print(list_makanan[1][1])

for i in list_makanan:
    for detail_makanan in i:
        print(detail_makanan)