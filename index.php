<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="utf-8"/>
		<title>Dungeon</title>
		<link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
		<script defer src="https://pyscript.net/latest/pyscript.js"></script>
	</head>
	<body>
    <py-script  output="out">
<?php
$file = file_get_contents('./dungeon.py');
$file = explode("\n",$file);
array_shift($file);
$file = implode("\n",$file);
print($file);
?>
	</py-script>
<div id="out"> </div>
<py-repl id="my-repl" auto-generate="true"> </py-repl>
	</body>
</html>
