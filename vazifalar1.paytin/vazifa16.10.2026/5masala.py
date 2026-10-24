from matplotlib import pyplot

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

pyplot.plot(mashgulot, masofa, color="green", marker="o", linewidth=3)
pyplot.title("Sportchining yugurgan masofalari")
pyplot.xlabel("Mashg'ulot")
pyplot.ylabel("Masofa")
print("Sportchining natijalari umuman olganda o'sib borgan: masofa 2.0 dan 4.0 gacha oshgan.")
print("Faqat 3-mashg'ulotda masofa biroz kamaygan (2.5 dan 2.3 ga), keyin yana o'sgan.")