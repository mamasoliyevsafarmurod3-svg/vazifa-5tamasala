n = int(input())
sonlar = list(map(int, input().split()))
natija = list(map(lambda son: son ** 3, sonlar))
print(natija)