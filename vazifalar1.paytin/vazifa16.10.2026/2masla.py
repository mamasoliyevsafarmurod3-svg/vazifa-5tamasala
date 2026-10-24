from matplotlib import pyplot

fanlar = ["Matematika", "Python", "Ingliz tili", "Fizika", "Tarix"]
ballar = [85, 95, 72, 80, 88]

pyplot.bar(fanlar, ballar)
pyplot.title("Fanlardan olingan ballar")
pyplot.xlabel("Fanlar")
pyplot.ylabel("Ball")
pyplot.show()