from matplotlib import pyplot

tillar = ["Python", "C", "JavaScript", "Java"]
oquvchilar = [15, 8, 12, 5]

pyplot.pie(oquvchilar, labels=tillar, autopct="%1.1f%%")
pyplot.title("Sevimli dasturlash tillari")
pyplot.show()