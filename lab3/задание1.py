import re

#ИСУ:409203
#Вариант:334

def count_smileys(text):
    pattern = r"8<\{\\"
    return len(re.findall(pattern, text))

# Тесты
text1 = " --- 8<{\\, ------- 8<{\\, ------ 8<{\\"
text2 = "8<{\\8<{\\8<{\\8<{\\"
text3 = "8<{\\ xxxxxx 8<{\\, xxxxxx 8<{\\"
text4 = "8<{\\8<{\\8<{\\8<{\\more8<{\\more8<{\\"
text5 = "8<{\\ и еще 8<{\\, но не так много 8<{\\"

# Проверка
print("Тест 1\nНайдено смайлов:",count_smileys(text1))
print("Тест 2\nНайдено смайлов:",count_smileys(text2))
print("Тест 3\nНайдено смайлов:",count_smileys(text3))
print("Тест 4\nНайдено смайлов:",count_smileys(text4))
print("Тест 5\nНайдено смайлов:",count_smileys(text5))
