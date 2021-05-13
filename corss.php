<?php

header('Content-type: application/jsonp');
header('Access-Control-Allow-Origin: *');
echo file_get_contents("https://github.com/ChrisScanlon/ArduinoWebPages/master/JSON2.JSON");

?>
