from matplotlib import pyplot

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

pyplot.scatter(soat, ball, color="purple", s=100)
pyplot.title("Tayyorlanish vaqti va test bali")
pyplot.xlabel("Kunlik tayyorlanish vaqti (soat)")
pyplot.ylabel("Test bali")
print("Tayyorlanish vaqti oshgani sari test bali ham oshgan, ya'ni ular o'rtasida kuchli to'g'ri (musbat) bog'liqlik bor.")
print("Masalan, 1 soat o'qiganda ball 40 bo'lgan bo'lsa, 7 soat o'qiganda 90 ga yetgan.")