# стр 32, номер 14
A = float(input("Введите размер стипендии: "))
current_expenses = float(input("Введите начальные ежемесячные расходы: "))

tottal_needed = 0

for mouth in range(1, 11):
    deficit = current_expenses - A
    tottal_needed += deficit
    current_expenses *= 1.03

print(f"Сумма, которую нужно попросить у родителей: {tottal_needed:.2f} руб.")