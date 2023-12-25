<?php require_once ("MySiteDB.php");

mb_internal_encoding('UTF-8');

mysqli_select_db($link, "mysitedb");

//Получение id заметки из GET-запроса
$note_id = $_GET['note'];

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    //Получение данных из формы
    $author = $_POST['author'];
    $content = $_POST['content'];



    //Добавление комментария в таблицу
    $query = "INSERT INTO comments (art_id, author, content, created) VALUES (
        $note_id,
        '$author',
        '$content',
        NOW()
    )";

    mysqli_query($link, $query);
}

//Формирование SQL-запроса на выборку заметки
$query = "SELECT created, title, article FROM notes WHERE id = $note_id";

//Реализация SQL-запроса
$result = mysqli_query($link, $query);

//Проверка результата выполнения запроса
if (!$result) {
    die("Ошибка выполнения запроса: " . mysqli_error($link));
}

//Вывод заметки
$note = mysqli_fetch_array($result);
?>

<h1><?php echo $note['title']; ?></h1>
<p><?php echo $note['created']; ?></p>
<p><?php echo $note['article']; ?></p>

<?php
//Формирование SQL-запроса на выборку комментариев
$query_comments = "SELECT * FROM comments WHERE art_id = $note_id";

//Реализация SQL-запроса
$result_comments = mysqli_query($link, $query_comments);

//Проверка результата выполнения запроса
if (!$result_comments) {
    die("Ошибка выполнения запроса: " . mysqli_error($link));
}
$query = "INSERT INTO comments (art_id, author, content, created) VALUES (
    1,
    'Джон',
    'комментарий',
    NOW()
  )";
  $query = "UPDATE comments SET status = 1 WHERE id = 1";
  mysqli_query($link, $query);

//Вывод комментариев
if (mysqli_num_rows($result_comments) > 0) {
    while ($comment = mysqli_fetch_array($result_comments)) {
        ?>
        <div class="comment">
            <p><?php echo $comment['author']; ?></p>
            <p><?php echo $comment['content']; ?></p>
        </div>
        <?php
    }
} 
else {
    ?>

    <p>Эту запись еще никто не комментировал.</p>
    <?php
}
?>

