
nomi = input("Nomi: ")
narxi = input("Narxi: ")
miqdori = input("Miqdori: ")

fayl = open("mahsulotlar.txt", "a")
fayl.write(nomi + " " + narxi + " " + miqdori + "\n")
fayl.close()