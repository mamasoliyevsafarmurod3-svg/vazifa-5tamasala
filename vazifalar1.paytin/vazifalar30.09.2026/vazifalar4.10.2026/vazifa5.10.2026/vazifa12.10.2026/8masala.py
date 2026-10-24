n = (input())

fayl = open("avtomobillar.txt", "a")

for i in range(n):
    markasi, yili, narxi = input().split()
    avtomobil = {
        "markasi": markasi,
        "yili": (yili),
        "narxi": (narxi)
    }

    fayl.write(avtomobil["markasi"] + " " + (avtomobil["yili"]) + " " + (avtomobil["narxi"]) + "\n")

fayl.close()