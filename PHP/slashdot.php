<?php

# Include Libraries
include("webbot_libs\LIB_http.php");
include("webbot_libs\LIB_parse.php");

# Setup Vars
$ref="www.slashdot.org";
$return_array = http_get_withheader($ref,$ref);
$links = parse_array($return_array['FILE'], "<a" ,"</a>");

echo "<html><head></head><body><table border='0'>";
foreach ($links as $link) {
 $class = get_attribute($link, "class");
 if ($class == "datitle") {
        $href = get_attribute($link, "href");
        $title = return_between($link, 'class="datitle">' , "</a>", EXCL);
        echo "<tr><td><a href=http:$href>$title</a></td></tr>\n";
 }
}
echo "</table></body></html>";
?>
