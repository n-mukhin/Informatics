import json
import yaml

# Чтение JSON-данных из файла schedule.json
with open('schedule.json', 'r', encoding="utf-8") as json_file:
    schedule_data = json.load(json_file)

# Преобразование данных в словарь для YAML
yaml_data = {
    "group": schedule_data["group"],
    "date": schedule_data["date"],
    "week": schedule_data["week"],
    "schedule": []
}

for entry in schedule_data["schedule"]:
    yaml_entry = {
        "day": entry["day"],
        "time": entry["time"],
        "week": entry["week"],
        "subject": entry["subject"],
        "teacher": entry["teacher"],
        "type": entry["type"],
        "format": entry["format"]
    }
    yaml_data["schedule"].append(yaml_entry)

# Запись данных в YAML-файл
with open('schedule.yaml', 'w', encoding="utf-8") as yaml_file:
    yaml.dump(yaml_data, yaml_file, default_flow_style=False, allow_unicode=True)

print("Расписание успешно преобразовано и записано в файл schedule.yaml.")



