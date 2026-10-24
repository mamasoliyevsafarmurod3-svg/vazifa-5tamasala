baholar = list(map(int, input().split()))
natija = list(filter(lambda son: son > 70, baholar))
print(natija)