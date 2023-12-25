<?php
 # FileName="Connection_php_mysql.htm"
 # Type="MYSQL"
 # HTTP="true"
 
 mb_internal_encoding('UTF-8');
 $localhost = "localhost";
 $db = "mysitedb";
 $user = "admin";
 $password = "admin";
 $link = mysqli_connect($localhost, $user, $password) or
 trigger_error(mysql_error(),E_USER_ERROR);


?>

