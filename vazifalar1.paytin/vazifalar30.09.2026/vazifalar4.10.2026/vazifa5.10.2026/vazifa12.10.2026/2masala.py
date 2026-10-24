
nomi = input("nomi:")
narxi = input("narxi:")
miqdori = input("miqdori:")

with open("Mahsulot.txt", "w") as fayl:
    fayl.write(f"{nomi}\n")
    fayl.write(f"{narxi}\n")
    fayl.write(f"{miqdori}\n")