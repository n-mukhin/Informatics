#ИСУ 409203
#Вариант 27 из json в YAML

# Инициализируем пустую строку для хранения YAML
yaml_data = ''

# Читаем содержимое файла schedule.json
with open('schedule.json', 'r', encoding="utf-8") as json_file:
    # Считываем JSON-данные из файла
    schedule_data = eval(json_file.read())

# Преобразовываем данные в YAML-подобный формат
yaml_data += "group: " + schedule_data["group"] + "\n"
yaml_data += "date: " + schedule_data["date"] + "\n"
yaml_data += "week: " + str(schedule_data["week"]) + "\n"
yaml_data += "schedule:\n"

for entry in schedule_data["schedule"]:
    yaml_data += "  -\n"
    yaml_data += "    day: " + entry["day"] + "\n"
    yaml_data += "    time: " + entry["time"] + "\n"
    yaml_data += "    week: " + entry["week"] + "\n"
    yaml_data += "    subject: " + entry["subject"] + "\n"
    yaml_data += "    teacher: " + entry["teacher"] + "\n"
    yaml_data += "    type: " + entry["type"] + "\n"
    yaml_data += "    format: " + entry["format"] + "\n"

# Записываем полученный YAML-подобный текст в файл schedule.yaml
with open('schedule.yaml', 'w',encoding="utf-8") as yaml_file:
    yaml_file.write(yaml_data)

print("Расписание успешно преобразовано и записано в файл schedule.yaml.")








