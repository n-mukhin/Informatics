<?php

// Установить соединение с сервером
$link = mysqli_connect("localhost", "admin", "admin");

if ($link) {
  echo "Соединение с сервером установлено", "<br>";
} else {
  echo "Нет соединения с сервером";
}

// Создать базу данных MySiteDB
$query = "CREATE DATABASE MySiteDB";
if ($link) {
  $create_db = mysqli_query($link, $query);
  if ($create_db) {
    echo "База данных MySiteDB успешно создана";
  } else {
    echo "База не создана";
  }
} else {
  echo "Нет соединения с сервером";
}

?>