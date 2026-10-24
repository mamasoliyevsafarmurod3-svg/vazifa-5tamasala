from matplotlib import pyplot

kunlar = [1, 2, 3, 4, 5, 6, 7]
ali = [10, 15, 12, 20, 25, 22, 30]
vali = [8, 12, 18, 16, 22, 27, 28]

pyplot.plot(kunlar, ali, color="blue", marker="o", label="Ali")
pyplot.plot(kunlar, vali, color="red", marker="s", label="Vali")
pyplot.title("Ali va Vali ning haftalik o'qish natijalari")
pyplot.xlabel("Kunlar")
pyplot.ylabel("Natija")
pyplot.show()