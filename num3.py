#стр 31 номер 3
n = int(input("Длительность(в часах): "))
amoeba = 1
for i in range(2, n, 3):
    amoeba *= 2
print(f"Через {n} часов амёб будет {amoeba}")