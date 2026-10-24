
ism, yosh, baho = input().split()

talaba = {
    "ism": ism,
    "yosh": int(yosh),
    "baho": int(baho)
}

fayl = open("talabalar.txt", "a")
fayl.write(talaba["ism"] + " " + str(talaba["yosh"]) + " " + str(talaba["baho"]) + "\n")
fayl.close()