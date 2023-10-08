def hamming_decode(bits):
    # Проверка на длину сообщения
    if len(bits) != 7:
        return "Ошибка: Неверная длина сообщения. Должно быть 7 бит."

    # Расчет битов паритета
    p1 = int(bits[0]) ^ int(bits[2]) ^ int(bits[4]) ^ int(bits[6])
    p2 = int(bits[1]) ^ int(bits[2]) ^ int(bits[5]) ^ int(bits[6])
    p4 = int(bits[3]) ^ int(bits[4]) ^ int(bits[5]) ^ int(bits[6])

    # Проверка на наличие ошибок
    error_bit = p1 + p2 * 2 + p4 * 4
    if error_bit == 0:
        info_bits = bits[2] + bits[4] + bits[5] + bits[6]
        return f"Правильное сообщение: {info_bits}"
    else:
        # Исправление бита с ошибкой
        corrected_bits = list(bits)
        corrected_bits[error_bit - 1] = str(1 - int(bits[error_bit - 1]))
        corrected_message = ''.join(corrected_bits)
        return f"Ошибка в бите {error_bit}. Исправленное сообщение: {corrected_message}"

if __name__ == "__main__":
    input_bits = input("Введите 7 битов (0 и 1, без пробелов): ")
    result = hamming_decode(input_bits)
    print(result)