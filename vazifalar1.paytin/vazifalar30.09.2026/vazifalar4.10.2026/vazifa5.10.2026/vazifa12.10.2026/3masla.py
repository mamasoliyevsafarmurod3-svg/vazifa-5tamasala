
marka = input("marka:")
yil = input("yil:")
narxi = input("narxi:")

with open("Avtomabil.txt", "w") as fayl:
    fayl.write(f"{marka}\n")
    fayl.write(f"{yil}\n")
    fayl.write(f"{narxi}\n")