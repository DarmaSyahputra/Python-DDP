# memmbuat list

buah = ["mangga","melon","jeruk",]
print (buah[0])

buah.append("mangga")

buah[0] = "jambu"
print(buah)

del buah[1]
print(buah)

print(buah.pop())

print(len(buah))

buah.insert(1,"melon")
for i in buah:
    print(i)