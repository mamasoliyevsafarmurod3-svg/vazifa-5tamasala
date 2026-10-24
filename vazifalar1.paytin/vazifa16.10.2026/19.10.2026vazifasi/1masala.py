with open("tasks.csv", "r") as file:
    lines = file.readlines()

for i in range(1, len(lines)):
    parts = lines[i].strip().split(",")
    print("Vazifa", i, ":")
    for p in parts:
        print("   ", p)