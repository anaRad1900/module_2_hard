def generate_password(n):
    if n < 3 or n > 20:
        return "Число должно быть в диапазоне от 3 до 20"

    password = ""

    # Генерируем уникальные пары
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            # Проверка кратности
            if n % pair_sum == 0:
                password += f"{i}{j}"

    return password

# Примеры использования функции
for number in range(3, 21):
    result = generate_password(number)
    print(f"{number} - {result}")