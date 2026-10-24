def daraja(son, n=2):
    return son ** n

data = input().split()
if len(data) == 2:
    print(daraja(int(data[0]),int(data[1])))
else:
    print(daraja(int(data[0])))