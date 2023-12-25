<?php

mb_internal_encoding('UTF-8');

//Соединение с сервером
$link = mysqli_connect('localhost', 'admin', 'admin');

//Выбор БД
$db = "mySiteDB";
$select = mysqli_select_db($link, $db);
if ($select) {
    echo "База успешно выбрана", "<br>";
} else {
    echo "База не выбрана";
}

//Создание таблицы
//Формирование запроса
$query = "CREATE TABLE notes
(id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY (id),
created DATE,
title VARCHAR (20),
article VARCHAR (255))";
//Реализация запроса
$create_tbl = mysqli_query($link, $query);
if ($create_tbl) {
    echo "Таблица успешно создана", "<br>";
} else {
    echo "Таблица не создана";
    echo "<p>";
}

$sql = "INSERT INTO notes (created, title, article) VALUES 
            ('2023-07-20', 'Заголовок 1', 'Текст заметки 1'), 
            ('2023-07-21', 'Заголовок 2', 'Текст заметки 2')"; 
       
if($link->query($sql)){
    echo "Данные успешно добавлены";
} else{
    echo "Ошибка: " . $link->error;
}


mysqli_close($link);

?>
