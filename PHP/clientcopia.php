<?php

# Include Libraries
include("LIB_http.php");
include("LIB_parse.php");


$url="http://www.clientcopia.com/quotes.php";

$return_array = http_get_withheader($url,$url);

echo "<html><head></head><body>";
echo return_between($return_array['FILE'],"<p>","</p>",EXCL);
echo "</body></html>";


?>
