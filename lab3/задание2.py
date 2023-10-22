import re

#ИСУ:409203
#Вариант:3

def find_vt_itmo(text):
    pattern = r'\bВТ\b\s+(?:\w+\s+){0,4}ИТМО\b'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(0)
    else:
        return "Фрагмент не найден."

# Примеры текстов для тестирования
texts = [
    "А ты знал, что ПИиКТ – лучший факультет в ИТМО?",
    "На ВТ факультете ИТМО обучается много студентов.",
    "ВТ в ИТМО - это достойно!",
    "ИТМО ВТ Лучший!",
    "Нет совпадений в этом тексте."
]

# Проведем тесты
for text in texts:
    result = find_vt_itmo(text)
    print(f"Текст: {text}\nНайденный фрагмент: {result}\n")



