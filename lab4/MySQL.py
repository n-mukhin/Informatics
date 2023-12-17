import mysql.connector
from mysql.connector import Error

# Создание базы данных
def create_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )

    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE attaadddataa")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection.is_connected():
            connection.close()

create_database()

# Подключение к базе данных
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="attaadddataa"
)

# Создание курсора
cur = conn.cursor()



# Создание таблиц
cur.execute('''
CREATE TABLE IF NOT EXISTS категории (
    id INT AUTO_INCREMENT PRIMARY KEY,
    название VARCHAR(255)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS товары (
    id INT AUTO_INCREMENT PRIMARY KEY,
    название  VARCHAR(255),
    описание TEXT,
    цена FLOAT,
    категория INT,
    остаток INT
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS клиенты (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(255),
    фамилия VARCHAR(255),
    почта VARCHAR(255),
    телефон VARCHAR(255)
)
''')

# Create the размеры table if it doesn't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS размеры (
    id_размера INT PRIMARY KEY,
    название VARCHAR(255)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS заказы (
    id INT AUTO_INCREMENT PRIMARY KEY,
    клиент INT REFERENCES клиенты (id_клиента),
    товар  INTEGER,
    размер INTEGER REFERENCES размеры (id_размера), 
    количество INT,
    цена FLOAT,
    дата_заказа DATE,
    FOREIGN KEY (товар) REFERENCES товары(id)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS магазины (
    id INT AUTO_INCREMENT PRIMARY KEY,
    название VARCHAR(255),
    адрес VARCHAR(255),
    телефон VARCHAR(255),
    город VARCHAR(255)
)
''')


# Insert data into the размеры table
sizes_data = [('XS', '1'), ('S', '2'), ('M', '3'), ('L', '4'), ('XL', '5')]

cur.executemany('''
INSERT INTO размеры (название, id_размера)
VALUES (%s, %s)
''', sizes_data)

# Заполнение таблицы shops данными
shops_data = [
    ('Сирень Москва', 'г. Москва, ул. Тверская, д. 12, стр. 2', '+7 (495) 123-45-67', 'Москва', 1),
    ('Сирень', 'г. Санкт-Петербург, ул. Большая Конюшенная, д. 25', ': +7 (812) 987-65-43', 'Санкт-Петербург', 2),
    ('Сирень Казань', 'г. Казань, ул. Профсоюзная, д. 42', '+7 (843) 567-89-01', 'Казань', 3),
]

cur.executemany('''
    INSERT INTO магазины (название, адрес, телефон, город, id)
    VALUES (%s, %s, %s, %s, %s)
''', shops_data)


# Вставка данных в таблицу items
items_data = [
    ('Футболка Сирень', 'Фирменная оверсайз футболка с нашивкой на груди. Состав:100% хлопок', 2999.0, 1, 12,1),
    ('Футболка Красная Лилия', 'Оверсайз футболка с рисунком на спине. Состав:100% хлопок', 2999.0, 1, 43,2),
    ('Футболка Темное прошлое', 'Оверсайз футболка с готическими элементами. Состав:100% хлопок', 2999.0, 1, 35,3),
    ('Лонгслив Сирень', 'Фирменный оверсайз лонгслив с нашивкой на груди. Состав:100% хлопок', 4999.0, 2, 2,4),
    ('Лонгслив Футуризм', 'Оверсайз лонгслив в стиле футуризма. Состав:60% хлопок 40% полиэстр', 4999.0, 2,13,5),
    ('Лонгслив Восстание машин', 'Лимитированный оверсайз лонгслив. Состав: 100% полиэстер', 4999.0, 2, 9,6),
    ('Рубашка Сирень', 'Фирменная оверсайз рубашка с нашивкой на груди. Состав:100% хлопок', 4499.0, 3, 23,7),
    ('Рубашка Лотос', 'Фирменная оверсайз рубашка с нашивкой на груди. Состав:100% хлопок', 4499.0, 3, 40,8),
    ('Рубашка Вечная ночь', 'Лимитированная оверсайз рубашка с вышиакой на спине. Состав:100% хлопок', 4499.0, 3, 54,9),
    ('Свитшот Сирень', 'Фирменный оверсайз свитшот с нашивкой на груди. Состав:100% хлопок', 5699.0, 4, 4,10),
    ('Свитшот Покой', 'Готический оверсайз свитшот. Состав: 55% хлопок 45% полиэстер', 5699.0, 4, 6,11),
    ('Свитшот Препятствие', 'Оверсайз свитшот из старой коллекции. Количество ограничено. Состав: 100% хлопок', 5699.0, 4,1,12),
    ('Джемпер Сирень', 'Фирменный оверсайз джемпер с нашивкой на груди. Состав:100% шерсть', 6699.0, 5, 17,13),
    ('Джемпер Холод', 'Оверсайз джемпер в холодных оттенках. Состав: 100% хлопок', 6699.0, 5, 23,14),
    ('Джемпер Изморозь', 'Альтернативная версия джемпера  "Холод"(более теплая). Состав: 30% шерсть 70% полиэтстер', 6699.0, 5, 15,15),
    ('Худи Сирень', 'Фирменнре оверсайз худи с нашивкой на груди. Состав:100% хлопок', 4999.0, 6, 5,16),
    ('Худи Соната заката', 'Худи, выполненное в коллаборации с брендом Волчок. Limited Edition. Состав: 100% хлопок', 4999.0, 6, 14,17),
    ('Худи Призрак', 'Худи из новой колекции "Сновидения". Состав: 55% хлопок 45% полиэстер', 4999.0, 6, 2,18),
    ('Брюки Сирень', 'Фирменные оверсайз брюки с нашивкой на карманах. Состав:100% хлопок', 5699.0, 7, 19,19),
    ('Брюки Черные', 'Повседневные оверсайз брюки. Состав:95% хлопок 5% полиэстер', 5699.0, 7, 12,20),
    ('Брюки Карго', 'Обычные штаны для работяг. Состав: 100% хлопок', 5699.0, 7, 30, 21),
]



for item_data in items_data:
    cur.execute('''
    INSERT INTO  товары (название, описание, цена,категория, остаток, id)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''', item_data)


# Вставка данных в таблицу categories
categories = [('ФУТБОЛКИ', 1), ('ЛОНГСЛИВЫ', 2), ('РУБАШКИ', 3), ('СВИТШОТЫ', 4), ('ДЖЕМПЕРЫ', 5), ('ХУДИ', 6), ('БРЮКИ / ДЖИНСЫ / ШОРТЫ', 7)]
for category_name, category_id in categories:
    cur.execute('''
    INSERT INTO категории(название, id)
    VALUES (%s, %s)
    ''', (str(category_name), category_id))

# Вставка данных в таблицу orders
order_data = [
    (1, 1, 2, 1, 1, 4999, '2023-11-01'),
    (2, 2, 1, 5, 2, 11398, '2023-11-04'),
    (3, 3, 3, 2, 1, 6699, '2023-11-10'),
    (4, 4, 13, 1, 2, 9998, '2023-11-12'),
    (5, 5, 18, 4, 2, 11398, '2023-11-23'),
    (6, 6, 7, 4, 2, 13398, '2023-11-21'),
    (7, 7, 19, 5, 3, 14997, '2023-11-17'),
    (8, 8, 15, 2, 2, 9998, '2023-11-14'),
    (9, 9, 14, 2, 2, 11398, '2023-11-07'),
    (10, 10, 21, 1, 2, 11998, '2023-11-15'),
    (11, 11, 5, 4, 2, 13398, '2023-11-29')
]



cur.executemany('''
INSERT INTO заказы (id, клиент, товар, размер, количество, цена, дата_заказа)
VALUES (%s, %s, %s, %s, %s, %s, %s)
''', order_data)


# Выбор всех записей из таблиц
cur.execute('''
SELECT *
FROM товары;
''')
print('Товары:')
for row in cur:
    print(row)

cur.execute('''
SELECT *
FROM категории;
''')
print('Категории:')
for row in cur:
    print(row)

cur.execute('''
SELECT *
FROM магазины;
''')
print('Магазины:')
for row in cur:
    print(row)

cur.execute('''
SELECT *
FROM клиенты;
''')
print('Клиенты:')
for row in cur:
    print(row)

# Выбор данных с использованием JOIN
cur.execute('''
SELECT товары.название, категории.название
FROM товары
JOIN категории
ON товары.категория = категории.id;
''')
print('Товары и категории:')
for row in cur:
    print(row)

# Выбор данных с использованием WHERE и GROUP BY
cur.execute('''
SELECT товары.название, SUM(заказы.количество) AS количество_проданных_товаров
FROM товары
JOIN заказы
ON товары.id = заказы.id
GROUP BY товары.название;
''')
print('Проданные товары:')
for row in cur:
    print(row)

# Вложенные SELECT-запросы
cur.execute('''
SELECT заказы.дата_заказа,
       (SELECT товары.название
        FROM товары
        WHERE товары.id = заказы.id) AS название_товара,
       заказы.количество
FROM заказы;
''')
print('Заказы:')
for row in cur:
    print(row)

# Объединение запросов (UNION)
cur.execute('''
SELECT *
FROM товары
WHERE товары.цена < 5000;
''')
print('Товары дешевле 5000 рублей:')
for row in cur:
    print(row)

cur.execute('''
SELECT *
FROM товары
WHERE товары.цена >= 5000;
''')
print('Товары дороже 5000 рублей:')
for row in cur:
    print(row)

cur.execute('''
SELECT *
FROM товары
UNION
SELECT *
FROM товары;
''')
print('Все товары:')
for row in cur:
    print(row)

# DISTINCT
cur.execute('''
SELECT DISTINCT товары.название
FROM товары;
''')
print('Уникальные названия товаров:')
for row in cur:
    print(row)

# Обновление данных
cur.execute('''
UPDATE товары
SET цена = 4599
WHERE id = 1;
''')
print('Цена товара с ID 1 обновлена до 4599 рублей.')

cur.execute('''
UPDATE клиенты
SET телефон = "+79341233252"
WHERE id = 1;
''')
print('Номер телефона клиента с ID 1 обновлен на "+79341233252".')

# Удаление данных
# Удаление заказов, связанных с товаром с ID 1
cur.execute('''
SELECT id
FROM заказы
WHERE товар = 1;
''')

order_ids = cur.fetchall()

for order_id in order_ids:
    cur.execute('''
        DELETE FROM заказы
        WHERE id = %s;
    ''', order_id)

# Удаление товара с ID 1
cur.execute('''
DELETE FROM товары
WHERE id = 1;
''')
print('Товар с ID 1 удален.')

cur.execute('''
DELETE FROM магазины;
''')
print('Все магазины удалены.')

# Сохранение изменений
conn.commit()

# Закрытие соединения
conn.close()
