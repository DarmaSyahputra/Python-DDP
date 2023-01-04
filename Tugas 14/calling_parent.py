from macan import Macan
from gajah import Gajah
from burungelang import Burung_Elang
from banteng import Banteng

#===================================================
# Membuat Objek Macan
macan = Macan("Macan", "Daging", "Di Darat", "Melahirkan", "Taring", "Loreng")

# print macan
print(f"Hewan \t\t: {macan.nama}")
print(f"Makanan \t: {macan.makanan}")
print(f"Hidup \t\t: {macan.hidup}")
print(f"Berkembang Biak : {macan.berkembang_biak}")

# Cetak macan 
macan.cetak()

#===================================================
# Membuat Objek Gajah
gajah = Gajah("Gajah", "Rumput", "Di Darat", "Melahirkan", "Belalai", "Gading")

# print Gajah
print(f"Hewan \t\t: {gajah.nama}")
print(f"Makanan \t: {gajah.makanan}")
print(f"Hidup \t\t: {gajah.hidup}")
print(f"Berkembang Biak : {gajah.berkembang_biak}")

# Cetak Gajah
gajah.cetak()

#===================================================
# Membuat Objek Burung Elang
burungelang = Burung_Elang("Burung_Elang", "Daging", "Di Darat / Di Udara", "Bertelur", "Sayap", "Cakar")

# print Burung Hantu
print(f"Hewan \t\t: {burungelang.nama}")
print(f"Makanan \t: {burungelang.makanan}")
print(f"Hidup \t\t: {burungelang.hidup}")
print(f"Berkembang Biak : {burungelang.berkembang_biak}")

# Cetak Burung Hantu
burungelang.cetak()

#===================================================
# Membuat Objek Banteng
banteng = Banteng("Banteng", "Rumput", "Di Darat", "Melahirkan", "Tanduk", "Punuk di bidang pundak")

# print Banteng
print(f"Hewan \t\t: {banteng.nama}")
print(f"Makanan \t: {banteng.makanan}")
print(f"Hidup \t\t: {banteng.hidup}")
print(f"Berkembang Biak : {banteng.berkembang_biak}")

# Cetak Banteng
banteng.cetak()
#===================================================