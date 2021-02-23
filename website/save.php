<?php
	$fieldA = $_POST["firstname"];
	$fieldB = $_POST["lastname"];
	$fieldC = $_POST["email"];
	$fieldD = $_POST["number"];
	$fieldE = $_POST["ssn"];
	$fieldF = $_POST["license"];

	$keys = array($fieldA,$fieldB,$fieldC,$fieldD,$fieldE,$fieldF,$fieldG,$fieldH,$fieldI,$fieldJ,$fieldK,$fieldL,$fieldM); //THIS IS WHERE YOU PUT THE FORM ELEMENTS ex: array('$fieldA','$fieldB',etc)
	$csv_line = $keys;
	foreach( $keys as $key ){
		array_push($csv_line,'' . $_GET[$key]);

	}
	$fname = 'data.csv'; //NAME OF THE FILE
	$csv_line = implode(',',$csv_line);
	if(!file_exists($fname)){$csv_line = $csv_line."\r\n" ;}
	$fcon = fopen($fname,'a');
	$fcontent = $csv_line;
	fwrite($fcon,$csv_line);
	fclose($fcon);
?>