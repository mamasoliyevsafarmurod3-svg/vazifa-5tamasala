talabalar = []

while True:
    print("1. Talaba qo'shish")
    print("2. Talabalarni ko'rish")
    print("3. O'rtacha yoshni hisoblash")
    print("4. Chiqish")

    tanlov = "".join(input("\nTanlov: ").split())

    if tanlov == "1":
        ism = " ".join(input("Ism: ").split())
        yosh_matni = "".join(input("Yosh: ").split())
        if yosh_matni.isdigit():
            talabalar.append({"ism": ism, "yosh": int(yosh_matni)})
            print("Talaba qo'shildi.")
        else:
            print("Xato: yosh butun son bo'lishi kerak!")

    elif tanlov == "2":
        if len(talabalar) == 0:
            print("Talabalar mavjud emas.")
        else:
            for talaba in talabalar:
                print("\nIsm:", talaba["ism"])
                print("Yosh:", talaba["yosh"])

    elif tanlov == "3":
        if len(talabalar) == 0:
            print("Talabalar mavjud emas.")
        else:
            jami = 0
            for talaba in talabalar:
                jami += talaba["yosh"]
            print("O'rtacha yosh:", jami / len(talabalar))

    elif tanlov == "4":
        print("Dastur tugadi.")
        break

    else:
        print("Noto'g'ri tanlov:")