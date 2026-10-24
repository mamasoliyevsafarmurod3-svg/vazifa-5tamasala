
ism = input("ism:")
yosh = input("yosh:")
ball = input("ball:")

with open("talaba.txt", "w") as fayl:
    fayl.write(f"{ism}\n")
    fayl.write(f"{yosh}\n")
    fayl.write(f"{ball}\n")