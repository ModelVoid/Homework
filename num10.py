# стр 31, номер 2
for x in range(29):
    number = 2 * (x ** 2) + 29
    is_prime = 1
    for i in range(2, number):
        if number % i == 0:
            is_prime = 0
            break
    if is_prime == 1:
        print(f"x = {x:2} : {number}")