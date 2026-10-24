n = (input())

fayl = open("xodimlar.txt", "w")

for i in range(n):
    ism, yosh, oylik = input().split()
    xodim = {
        "ism": ism,
        "yosh": (yosh),
        "oylik":(oylik)
    }

    fayl.write(xodim["ism"] + " " + (xodim["yosh"]) + " "+(xodim["oylik"]) + "\n")

fayl.close()