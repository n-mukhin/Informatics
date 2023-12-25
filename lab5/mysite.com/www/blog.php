<?php require_once ("MySiteDB.php"); 

mb_internal_encoding('UTF-8');

mysqli_select_db($link, "mysitedb");
// Выполнение запроса на выборку
$select_notes = mysqli_query($link, "SELECT * FROM notes");

// Проверка результата выполнения запроса
if (!$select_notes) {
    die("Ошибка выполнения запроса: " . mysqli_error($link));
}
// Цикл для вывода всех записей
while ($note = mysqli_fetch_array($select_notes)) {
    echo "note". " " . "№" .$note['id'], "<br>";
    echo "id:" . " " . $note['id'], "<br>";
    echo 'title:';
?>
<a href="comments.php?note=<?php echo $note['id']; ?>">
<?php echo $note['title'] ; ?></a> <br>
<?php
    echo "created:" . " " . $note['created'], "<br>";
    echo "article:" . " " . $note['article'], "<br>";
    echo "<p>";
}
?>

