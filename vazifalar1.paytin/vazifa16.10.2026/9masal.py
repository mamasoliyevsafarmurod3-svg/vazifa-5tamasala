from matplotlib import pyplot

kunlar = [1, 2, 3, 4, 5, 6, 7]
suv = [1.5, 2.0, 1.8, 2.2, 2.5, 2.1, 2.4]

pyplot.plot(kunlar, suv, color="blue", marker="o", linewidth=2)
pyplot.title("Haftalik ichilgan suv miqdori")
pyplot.xlabel("Kunlar")
pyplot.ylabel("Suv miqdori (litr)")
pyplot.savefig("natija.png")
pyplot.show()