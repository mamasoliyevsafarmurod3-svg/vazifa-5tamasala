n = int(input("1 dan 7 gacha son: "))

kunlar = {
    1: "Dushanba",
    2: "Seshanba",
    3: "Chorshanba",
    4: "Payshanba",
    5: "Juma",
    6: "Shanba",
    7: "Yakshanba",
}

print(kunlar.get(n, "Noto'g'ri son"))