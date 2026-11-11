# стр 31, номер 5
total = 64
print("Возможные сочетания (Кролики/гуси): ")

for r in range(0, 16 + 1):
    remaining_legs = total - (r * 4)
    if remaining_legs % 2 == 0:
        g = remaining_legs // 2
        print(f"Кроликов: {r}, Гусей: {g}")