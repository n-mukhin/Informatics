<?php
mb_internal_encoding('UTF-8');

$res = array();
echo "Задание 1";

$a = 10;
$b = 20;


$res[1] = "a = $a";
$res[2] = "a = $b";

echo "<p>";
echo $res[1];
echo "<p>";
echo $res[2];
echo "<p>";

echo "Задание 2";
$c = $a + $b;
$res[3] = "c = $c";

echo "<p>";
echo $res[3];
echo "<p>";

echo "Задание 3";
$c = $c * 3;

$res[4] = "c = $c";

echo "<p>";
echo $res[4];
echo "<p>";

echo "Задание 4";
$d = $b - $a;
$e = $c/$d;

$res[5] = "c / (b - a) = $e";

echo "<p>";
echo $res[5];
echo "<p>";



echo "Задание 5";

$p = "Программа";
$b = "работает";

echo "<p>";
echo $p;
echo "<p>";
echo $b;
echo "<p>";

echo "Задание 6";
$result = $p . " " . $b;

echo "<p>";
echo $result;
echo "<p>";

echo "Задание 7";
$result .= " хорошо";

echo "<p>";
echo $result;
echo "<p>";

echo "Задание 8";
$q = 5;
$w = 7;

$q+=+$w-$w=$q;

$res[6] = "q = $q"; 
$res[7] = "w = $w";

echo "<p>";
echo $res[6];
echo "<p>";
echo $res[7];
echo "<p>";


echo "Задание 9";
$a = 23;
$b = 78;

echo "<p>";
while ($a <= $b) {
    echo $a++ . "\n";
}
echo "<p>";


echo "Задание 10";
echo "<p>";

for ($i = 1; $i <= 10; $i++) {
    echo "<ul>";
    echo "Пункт $i";
    echo "</ul>";
}

echo "Задание 11";
echo "<p>";

$arr = array();
for ($i = 0; $i < 100; $i++) {
    $arr[] = rand(0, 100);
}

// Вывод массива while

echo "while:\n";

$arr1 = $arr;
while (!empty($arr1)) {
    echo $arr1[0] . "\n";
    array_shift($arr1);
}

echo "<p>";

// Вывод массива foreach

echo "foreach:\n";
foreach ($arr as $item) {
    echo $item . "\n";
}

echo "<p>";
echo "Задание 12";
echo "<p>";

// Получаем текущий день недели
$day = date("l");

// Используем оператор switch для вывода надписи
switch ($day) {
    case "Monday":
        echo "<p>";
        echo "Сегодня понедельник";
        echo "<p>";
        break;
    case "Tuesday":
        echo "<p>";
        echo "Сегодня вторник";
        echo "<p>";
        break;
    case "Wednesday":
        echo "<p>";
        echo "Сегодня среда";
        echo "<p>";
        break;
    case "Thursday":
        echo "<p>";
        echo "Сегодня четверг";
        echo "<p>";
        break;
    case "Friday":
        echo "<p>";
        echo "Сегодня пятница";
        echo "<p>";
        break;
    case "Saturday":
        echo "<p>";
        echo "Сегодня суббота";
        echo "<p>";
        break;
    case "Sunday":
        echo "<p>";
        echo "Сегодня воскресенье";
        echo "<p>";
        break;
  }


echo "Задание 13";
echo "<p>";
function getPlus10($num) {
    $num = $num + 10;
    return $num;
}

$rn = rand(0, 100);
echo getPlus10($rn);

?>