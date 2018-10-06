<?php
	$db = mysqli_connect('localhost', 'root', 'root', 'clon');
	//Usuario, contraseña y nombre de la BD.
	mysqli_set_charset($db,'utf8'); //Para que muestre bien los datos que tienen acento o ñ
?> 