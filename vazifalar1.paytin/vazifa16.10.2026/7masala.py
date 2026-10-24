from matplotlib import pyplot

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

pyplot.plot(testlar, guruh_a, color="blue", marker="o", label="A guruh")
pyplot.plot(testlar, guruh_b, color="red", marker="s", label="B guruh")
pyplot.title("Ikki guruhning test natijalari")
pyplot.xlabel("Testlar")
pyplot.ylabel("Ball")
o_rtacha_a = sum(guruh_a) / len(guruh_a)
o_rtacha_b = sum(guruh_b) / len(guruh_b)
print("A guruhning o'rtacha bali:", o_rtacha_a)
print("B guruhning o'rtacha bali:", o_rtacha_b)
print("B guruh natijasi yaxshiroq: o'rtacha bali (76) A guruhnikidan (75) yuqori va oxirgi testlarda B guruh 88 va 90 ball olgan.")
print("Lekin A guruh natijalari o'sgan, B guruhda esa ballar ko'tarilib-tushib turgan.")