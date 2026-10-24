from matplotlib import pyplot

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

pyplot.bar(mahsulotlar, sotuv, color="orange")
pyplot.title("Do'konda bir haftada sotilgan mahsulotlar")
pyplot.xlabel("Mahsulotlar")
pyplot.ylabel("Sotilgan soni")
pyplot.show()
eng_kop = mahsulotlar[sotuv.index(max(sotuv))]
eng_kam = mahsulotlar[sotuv.index(min(sotuv))]
print("Eng ko'p sotilgan mahsulot:", eng_kop, "-", max(sotuv))
print("Eng kam sotilgan mahsulot:", eng_kam, "-", min(sotuv))