data = {"nama":"Darma Syahputra"}

print(data["nama"])

nilai = {"firda":89, "inaya":100, "deden":59, "ucup":57}

for skor in nilai.values():
    print(skor)

for skor in nilai.keys():
        print(skor)

for nama,nilai in nilai.items():
    print (nama, ":" ,nilai)